import http.server
import json

stored_value = ""

class CORSRequestHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))  # Decodifica il payload JSON

        if 'cookies' in data and isinstance(data['cookies'], str):
            global stored_value
            stored_value = data['cookies']
            print(f"Received cookies: {stored_value}")  # Stampa i cookie ricevuti a terminale
            self._set_headers()
            response = {'status': 'success', 'message': 'Cookies received'}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._set_headers(400)
            response = {'status': 'error', 'message': 'Invalid cookies'}
            self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=http.server.HTTPServer, handler_class=CORSRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
