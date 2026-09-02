import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Always serve index.html for root path or missing paths to mimic SPA routing if needed
        if self.path == '/' or not os.path.exists(self.path[1:]):
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server safely launched and listening on port {PORT}")
    httpd.serve_forever()
