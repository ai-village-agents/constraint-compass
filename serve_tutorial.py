#!/usr/bin/env python3
"""
Simple HTTP server for Constraint Compass tutorial
"""

import http.server
import socketserver
import os

PORT = 9001  # Using port 9001

class TutorialHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.getcwd(), **kwargs)
    
    def log_message(self, format, *args):
        # Suppress default logging
        pass

def main():
    with socketserver.TCPServer(("", PORT), TutorialHandler) as httpd:
        print(f"Constraint Compass tutorial serving at http://localhost:{PORT}/")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
