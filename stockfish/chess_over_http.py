#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import subprocess
import sys
import re
import time

engine = sys.argv[1]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        fen = params.get('fen', [''])[-1]
        timeout = int(params.get('time', ['500'])[-1])
        print('Params: {}'.format(params))
        process = subprocess.Popen(engine, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        def send_command(command):
            process.stdin.write((command + '\n').encode('utf-8'))
        if fen:
            send_command('position fen {}'.format(fen))
        send_command('go movetime {}'.format(timeout))
        time.sleep(0.2 + timeout/1000.)
        stdout, stderr = process.communicate(input=b'quit\n')
        output = stdout.decode('utf-8')
        print(output)
        match = re.search("bestmove ([^ ]*)", output)
        if not match:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'error')
            return
        move = match.group(1)
        print('Move: {}'.format(move))
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(move.encode('utf-8'))

port = 8080
print('Server listening on port {}'.format(port))
server_address = ('', port)
httpd = HTTPServer(server_address, Handler)
httpd.serve_forever()
