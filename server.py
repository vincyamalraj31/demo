#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple HTTP Server for 3D Penguin Viewer
Serves the viewer with proper CORS headers for local development
"""

import http.server
import socketserver
import os
import sys
import io

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        sys.stdout.write("%s - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format % args))

def main():
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print("Penguin 3D Viewer Server Started!")
        print("=" * 60)
        print(f"\nServer running at: http://localhost:{PORT}")
        print(f"Direct URL: http://localhost:{PORT}/index.html")
        print(f"\nServing from: {os.getcwd()}")
        print("\nTips:")
        print("   - Open the URL above in your browser")
        print("   - Press Ctrl+C to stop the server")
        print("   - Place your penguin.glb file in this directory")
        print("\n" + "=" * 60 + "\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped by user")
            sys.exit(0)

if __name__ == "__main__":
    main()

