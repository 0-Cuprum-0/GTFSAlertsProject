from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):


    def get_timestamp(self):

        with open("/home/cuprum/GTFSAlertsProject/json/data.json" , "r") as file:
            return json.load(file)["timestamp"]

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
            with open("/home/cuprum/GTFSAlertsProject/json/data.json" , "r") as file:
                body= json.load(file)

            response_body = json.dumps(body).encode("utf-8")

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
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
    
