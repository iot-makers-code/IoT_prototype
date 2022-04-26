from http.server import BaseHTTPRequestHandler,HTTPServer
import glob
from urllib import parse
from pathlib import Path
import mimetypes
import os
import re
MP4CHUCKSIZE = 1<<23

class MyHandler(BaseHTTPRequestHandler):
    def do_GET_stream(self, fullfilepath):
        #iOS requred Accept Ranges for HTML5
        # https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Range

        if not os.path.isfile(fullfilepath):
            return self.send_error(404);

        start = 0
        total = os.path.getsize(fullfilepath)
            
        range = self.headers['Range'];
        print("=Range [{}]".format(range));

        if range == None :
            start = 0
            end = total - 1;
            chunksize = 1<<16 #MP4CHUCKSIZE

            print("None check {},  bytes {}-{}/{}".format(chunksize, start,end,total))
            
            self.send_response(200)
            self.send_header('Content-Range', 
                      "bytes {}-{}/{}".format(start,end,total))
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Length',  chunksize)

            self.send_header('Content-Type', "video/mp4")
            self.end_headers()
            
            try:
                with open(fullfilepath, 'rb') as f:
                    f.seek(start)
                    self.wfile.write(f.read(chunksize))
                    f.close()
                    
            except AttributeError as e:
                print('Error :{}'.format(str(e)))
                traceback.print_exc()
                pass 

        else:
            ranges = re.findall('(\d+)-(\d*)', range)
            start, end = ranges[0]
            
            end = int(end) if end != '' else total - 1;
            start = int(start) if start != '' else 0;
            
            chunksize = (end - start) + 1;
            chunksize = MP4CHUCKSIZE \
                        if chunksize > MP4CHUCKSIZE else chunksize

            self.send_response(206)
            self.send_header('Content-Range', 
                      "bytes {}-{}/{}".format(start,end,total))
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Content-Length',  chunksize)

            self.send_header('Content-Type', "video/mp4")
            self.end_headers()

            try:
                with open(fullfilepath, 'rb') as f:
                    f.seek(start)
                    self.wfile.write(f.read(chunksize))
                    f.close()
            except AttributeError as e:
                print('Error :{}'.format(str(e)))
                traceback.print_exc()
                pass 
                    
    def run_GET_static(self, fullfilepath, mimetype):
    
        if not os.path.isfile(fullfilepath):
            print ("file is not found {}".format(fullfilepath))
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
        for ext in [ "*/*.mp4", "*/*.jpg", "*/*.png" ]:
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
        elif 'mp4' in self.path:
            self.do_GET_stream(fullfilepath)
        else:
            self.run_GET_static(fullfilepath, mimetype)        
            
        return
def run():
    server_addr = ('0.0.0.0', 8001)
    httpd = HTTPServer(server_addr, MyHandler)
    print('starting web server...')
    httpd.serve_forever()
run()
