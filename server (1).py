import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or not os.path.exists(self.path[1:]):
            self.path = '/index.html'
        return super().do_GET()

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Server safely launched and listening on port {PORT}")
    httpd.serve_forever()