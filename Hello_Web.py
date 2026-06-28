from http.server import HTTPServer, BaseHTTPRequestHandler
import os

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
        try:
            # Figure out what exactly is being requested
            full_path = os.getcwd() + self.path

            # if it does not exist,
            if not os.path.exists(full_path):
                raise Exception("'{0}' not found".format(self.path))
            
            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
            
            # ...it's something we don't handle.
            else:
                raise Exception("Unknown object '{0}'".format(self.path))
            
        except Exception as msg:
            self.handle_error(msg)

    def handle_file(self, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            self.send_content(content.decode("utf-8"))
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def create_page(self):
        values = {
            'date_time': self.date_time_string(),
            'client_host': self.client_address[0],
            'client_port': self.client_address[1],
            'command': self.command,
            'path': self.path
        }
        return self.Page.format(**values)

    def send_page(self, content):
        content_bytes = content.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(content_bytes)))
        self.end_headers()

        self.wfile.write(content_bytes)
    
        Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """

    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content.encode("utf-8"))

    # Handle unknown objects.
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)

    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))
#----------------------------------------------------------------------

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    print("Server running on http://localhost:8080")
    server.serve_forever()
