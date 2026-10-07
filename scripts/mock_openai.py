#!/usr/bin/env python3
"""Minimal OpenAI-compatible chat server for install tests.

It records every request body to the file given as argv[2] and answers with a
short streamed reply, so a CLI can run one prompt without a real model or key.
Usage: mock_openai.py PORT CAPTURE_FILE
"""
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT, CAPTURE = int(sys.argv[1]), sys.argv[2]


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        with open(CAPTURE, "ab") as f:
            f.write(body + b"\n")
        chunk = {"id": "mock", "object": "chat.completion.chunk", "model": "mock",
                 "choices": [{"index": 0, "delta": {"role": "assistant", "content": "ok"}, "finish_reason": None}]}
        done = {"id": "mock", "object": "chat.completion.chunk", "model": "mock",
                "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}}
        payload = f"data: {json.dumps(chunk)}\n\ndata: {json.dumps(done)}\n\ndata: [DONE]\n\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *args):
        pass


HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
