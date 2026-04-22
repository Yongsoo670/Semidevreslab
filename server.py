#!/usr/bin/env python3
"""
SRDL Lab Website - Local Server
================================
사용법:
  python server.py          → http://localhost:8080 으로 실행
  python server.py 3000     → 포트 변경

외부 접속(연구실 PC → 인터넷):
  1. 공유기 포트포워딩: 외부 포트 80 → 이 PC의 IP:8080
  2. 방화벽에서 8080 포트 열기
  3. 공인 IP 또는 도메인으로 접속 가능
"""

import sys
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080

class LabHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] {self.address_string()} - {format % args}")

    def end_headers(self):
        # Enable CORS for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

def run():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = HTTPServer(('0.0.0.0', PORT), LabHandler)
    print("=" * 50)
    print(f"  SRDL Lab Website Server")
    print("=" * 50)
    print(f"  Local:   http://localhost:{PORT}")
    print(f"  Network: http://[이 PC의 IP]:{PORT}")
    print(f"  종료: Ctrl+C")
    print("=" * 50)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")
        server.shutdown()

if __name__ == '__main__':
    run()
