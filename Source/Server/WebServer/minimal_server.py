# Webserver with the minimal functionality needed
# to test the Client Code
#
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello Galaxy')


httpd = HTTPServer(('localhost', 8999), SimpleHTTPRequestHandler)
httpd.serve_forever()
