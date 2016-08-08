from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver
import socket

class MyHandler(SimpleHTTPRequestHandler):
  def do_GET(self):
    if self.path == '/ip':
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      self.wfile.write('Your IP address is %s' % self.client_address[0])
      return
    else:
        return SimpleHTTPRequestHandler.do_GET(self)

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6

server_ipv4 = HTTPServer(('', 8080), MyHandler)
server_ipv6 = HTTPServerV6(('::1', 8080), MyHandler)
