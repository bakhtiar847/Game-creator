import http.server
import ssl
import socketserver

class HTTPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True):
        self.allow_reuse_address = True
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
        self.socket = context.wrap_socket(self.socket, server_side=True)

if __name__ == "__main__":
    server = HTTPServer(('localhost', 8000), http.server.SimpleHTTPRequestHandler)
    print("Serving HTTPS on https://localhost:8000")
    server.serve_forever()