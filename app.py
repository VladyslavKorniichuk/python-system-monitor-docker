import json
import platform
import psutil
from http.server import BaseHTTPRequestHandler, HTTPServer


# HTTP server to provide real-time system metrics in JSON format
class MonitorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Gather real-time system metrics
        cpu_usage = psutil.cpu_percent(interval=0.1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        # Prepare the response data
        data = {
            "status": "success",
            "system_info": {
                "os": platform.system(),
                "release": platform.release(),
                "machine": platform.machine(),
            },
            "metrics": {
                "cpu_percent": cpu_usage,
                "ram_percent": ram.percent,
                "ram_total_mb": round(ram.total / (1024 * 1024), 2),
                "disk_percent": disk.percent,
            },
            "message": "Real-time system metrics from Docker container",
        }

        self.wfile.write(json.dumps(data).encode("utf-8"))


# Run the server
if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MonitorHandler)
    print("HTTP server runs on port 8000...")
    httpd.serve_forever()
