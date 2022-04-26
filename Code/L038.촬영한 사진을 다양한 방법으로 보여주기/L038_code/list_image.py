from http.server import BaseHTTPRequestHandler,HTTPServer
import glob
from urllib import parse
from pathlib import Path
import mimetypes
import os

class MyHandler(BaseHTTPRequestHandler):
    def run_GET_static(self, fullfilepath, mimetype):
        if not os.path.isfile(fullfilepath):
           return self.send_error(404);
        self.send_response(200)
        self.send_header('Content-type',mimetype)
        self.end_headers()
        f = open(fullfilepath, 'rb')
        self.wfile.write(f.read())
        f.close()

    def run_GET_root(self):
        self.send_response(200)
        self.send_header('Content-type',"text/html")
        self.end_headers()
        files = []
        for ext in ["*/*.jpg", "*/*.png" ]:
            files.extend( glob.glob(ext) )
        message = """<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>"""
        for f in files:
            message += "<a href=\"" + f + "\">"+f+"</a><br>\n"
        message += """</body>
</html>"""
        print(message)
        self.wfile.write(bytes(message, encoding='utf8'))
            
    def do_GET(self):
        #if self.path == "/favicon.ico" : return
        parsed_path = parse.urlparse(parse.unquote(self.path))
        fullfilepath = "." + parsed_path.path
        mimetype = mimetypes.MimeTypes().guess_type(parsed_path.path)[0]
        if self.path == "/":
            self.run_GET_root();
        else:
            self.run_GET_static(fullfilepath, mimetype)
        
        return
def run():
    server_addr = ('0.0.0.0', 8001)
    httpd = HTTPServer(server_addr, MyHandler)
    print('starting web server...')
    httpd.serve_forever()
run()
