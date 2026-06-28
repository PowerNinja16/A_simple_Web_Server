from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
<<<<<<< HEAD
    '''Handle HTTP requests by returning a fixed "page".'''
=======
    '''Handle HTTP requests by returning a dynamic page.'''
>>>>>>> b438d09bbbbcbdc65e0de2fb7608b57bd0b33b13

    Page = '''\
<html>
<body>
<p>Hello, web!</p>
<<<<<<< HEAD
=======
<p>Time: {date_time}</p>
<p>Your IP: {client_host}</p>
<p>Port: {client_port}</p>
<p>Request: {command}</p>
<p>Path: {path}</p>
>>>>>>> b438d09bbbbcbdc65e0de2fb7608b57bd0b33b13
</body>
</html>
'''

    def do_GET(self):
<<<<<<< HEAD
        content = self.Page.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()

        self.wfile.write(content)
=======
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
>>>>>>> b438d09bbbbcbdc65e0de2fb7608b57bd0b33b13

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server running on http://localhost:8080")
<<<<<<< HEAD
    server.serve_forever()
=======
    server.serve_forever()
>>>>>>> b438d09bbbbcbdc65e0de2fb7608b57bd0b33b13
