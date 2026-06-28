from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a dynamic page.'''

    Page = '''\
<html>
<body>
<p>Hello, web!</p>
<p>Time: {date_time}</p>
<p>Your IP: {client_host}</p>
<p>Port: {client_port}</p>
<p>Request: {command}</p>
<p>Path: {path}</p>
</body>
</html>
'''

    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        print(self.Page)
        return self.Page.format(**values)

    def send_page(self, content):
        content_bytes = content.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content_bytes)))
        self.end_headers()

        self.wfile.write(content_bytes)

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()