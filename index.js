// OpenCode plugin entry for ai-agent-skills. It only registers the bundled
// skills/ directory. It injects no prompt text and adds no tools.
//
// V1 (opencode 1.x): named export with a config hook that adds the skills path.
// V2 (opencode 2.0.4+): default export { id, setup } that registers each skill.
// V2 requires a directory-form plugin, so this file stays at the repo root.

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const skillsDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "skills");

// Reads name and description from SKILL.md frontmatter. Handles plain values and
// folded (>) or literal (|) block scalars, which the skills in this repo use.
export function parseFrontmatter(text) {
  const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/);
  if (!match) return { frontmatter: {}, content: text };
  const frontmatter = {};
  let key = null;
  for (const raw of match[1].split("\n")) {
    const line = raw.replace(/\r$/, "");
    const top = line.match(/^([A-Za-z][\w-]*):\s*(.*)$/);
    if (top) {
      key = top[1];
      frontmatter[key] = /^[>|][+-]?$/.test(top[2]) ? "" : top[2].trim();
    } else if (key && /^\s+\S/.test(line)) {
      frontmatter[key] = `${frontmatter[key]} ${line.trim()}`.trim();
    }
  }
  for (const k of Object.keys(frontmatter)) {
    frontmatter[k] = frontmatter[k].replace(/^(["'])([\s\S]*)\1$/, "$2");
  }
  return { frontmatter, content: match[2] };
}

export function listSkills(dir = skillsDir) {
  if (!fs.existsSync(dir)) return [];
  const skills = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name.startsWith(".")) continue;
    const skillPath = path.join(dir, entry.name, "SKILL.md");
    if (!fs.existsSync(skillPath)) continue;
    const { frontmatter, content } = parseFrontmatter(fs.readFileSync(skillPath, "utf8"));
    skills.push({
      id: entry.name,
      name: frontmatter.name || entry.name,
      ...(frontmatter.description ? { description: frontmatter.description } : {}),
      path: skillPath,
      content,
    });
  }
  return skills;
}

export const AiAgentSkillsPlugin = async () => ({
  config: async (config) => {
    // V2 uses a flat skills array and is handled by setup() below.
    if (Array.isArray(config.skills)) return;
    config.skills = config.skills || {};
    config.skills.paths = config.skills.paths || [];
    if (!config.skills.paths.includes(skillsDir)) config.skills.paths.push(skillsDir);
  },
});

async function setup(ctx) {
  // V1 also calls default.setup with a ctx that lacks these APIs.
  if (!ctx || !ctx.skill || typeof ctx.skill.transform !== "function") return;
  try {
    const skills = listSkills();
    await ctx.skill.transform((draft) => {
      for (const skill of skills) {
        try {
          draft.add(skill);
        } catch (err) {
          console.error(`[ai-agent-skills] host rejected skill "${skill.id}":`, err);
        }
      }
    });
  } catch (err) {
    console.error("[ai-agent-skills] skill registration failed:", err);
  }
}

export default { id: "ai-agent-skills", server: AiAgentSkillsPlugin, setup };
