from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed "page".'''

    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''

    def do_GET(self):
        content = self.Page.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()

        self.wfile.write(content)

#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()
