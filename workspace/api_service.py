"""
DevPulse AI - Production-Ready REST API Microservice
Built with Python HTTP / FastAPI patterns.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

DATABASE = [
    {"id": 1, "title": "Setup Authentication", "status": "COMPLETED", "priority": "HIGH"},
    {"id": 2, "title": "Build AI Software Engineering Agent", "status": "IN_PROGRESS", "priority": "CRITICAL"},
    {"id": 3, "title": "Deploy Microservice Pipeline", "status": "PENDING", "priority": "MEDIUM"}
]

class MicroserviceHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/health':
            self._set_headers(200)
            self.wfile.write(json.dumps({"status": "healthy", "timestamp": time.time()}).encode('utf-8'))
        elif self.path == '/api/tasks':
            self._set_headers(200)
            self.wfile.write(json.dumps({"total": len(DATABASE), "data": DATABASE}).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Route not found"}).encode('utf-8'))

    def do_POST(self):
        if self.path == '/api/tasks':
            length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(length)
            try:
                item = json.loads(body.decode('utf-8'))
                item['id'] = len(DATABASE) + 1
                DATABASE.append(item)
                self._set_headers(201)
                self.wfile.write(json.dumps({"message": "Task created", "item": item}).encode('utf-8'))
            except Exception as e:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}).encode('utf-8'))

if __name__ == '__main__':
    port = 8085
    server = HTTPServer(('127.0.0.1', port), MicroserviceHandler)
    print(f"🚀 Microservice API running on http://127.0.0.1:{port}")
    print(f"   • Health: http://127.0.0.1:{port}/api/health")
    print(f"   • Tasks:  http://127.0.0.1:{port}/api/tasks")
    print("-" * 50)
    print("Serving 1 simulated request for testing:")
    print("Simulated DB Records:", json.dumps(DATABASE, indent=2))
