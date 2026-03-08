import json
import platform
import psutil
from http.server import BaseHTTPRequestHandler, HTTPServer


class MonitorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.serve_html()
        elif self.path == "/data":
            self.serve_json_data()
        elif self.path == "/static/style.css":
            self.serve_css()
        else:
            self.send_error(404, "Page Not Found")

    def serve_html(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        metrics = self.get_system_metrics()

        with open("templates/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        html_content = html_content.replace("{os}", platform.system())
        html_content = html_content.replace("{release}", platform.release())
        html_content = html_content.replace("{cpu}", str(metrics["cpu_percent"]))
        html_content = html_content.replace("{ram}", str(metrics["ram_percent"]))
        html_content = html_content.replace("{ram_mb}", str(metrics["ram_mb"]))
        html_content = html_content.replace("{disk}", str(metrics["disk_percent"]))

        self.wfile.write(html_content.encode("utf-8"))

    # Serve JSON data for AJAX requests
    def serve_json_data(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Collect system metrics
        metrics = self.get_system_metrics()

        # Create a JSON response
        data = {"metrics": metrics}
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def serve_css(self):
        try:
            with open("static/style.css", "r", encoding="utf-8") as f:
                css_content = f.read()
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            self.wfile.write(css_content.encode("utf-8"))
        except FileNotFoundError:
            self.send_error(404, "CSS not found")

    # Function to get system metrics
    def get_system_metrics(self):
        cpu_usage = psutil.cpu_percent(interval=0.1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        return {
            "cpu_percent": cpu_usage,
            "ram_percent": ram.percent,
            "ram_mb": round(ram.total / (1024 * 1024), 2),
            "disk_percent": disk.percent,
        }


if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MonitorHandler)
    print("HTTP server runs on port 8000...")
    httpd.serve_forever()
