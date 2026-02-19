import json
import platform
from http.server import BaseHTTPRequestHandler, HTTPServer

class MonitorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        data = {
            "status": "success",
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "message": "Hello from Dockerized Python API!"
        }
        
        self.wfile.write(json.dumps(data).encode('utf-8'))

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MonitorHandler)
    print("HTTP server runs on port 8000...")
    httpd.serve_forever()