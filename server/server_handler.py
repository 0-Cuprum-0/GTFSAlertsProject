from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    with open("../json/data.json", "r") as file:

        json_obj = json.load(file)

    def get_timestamp(self):

        return self.json_obj["timestamp"]

    def do_GET(self):
        if self.path == "/hello_there":

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        elif self.path == "/timestamp":
            ts = self.get_timestamp()
            print(ts)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"{ts}".encode())
        elif self.path == "/data":


            response_body = json.dumps(self.json_obj).encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()

            self.wfile.write(response_body)

        else:
            body = {
                "error": "Route not found"
            }

            response_body = json.dumps(body).encode("utf-8")

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(response_body)))
            self.end_headers()

            self.wfile.write(response_body)


def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
    
