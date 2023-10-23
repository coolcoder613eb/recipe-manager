from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os
import export_to_folder
import convert_to_html

FOLDER = os.path.abspath("./recipes/html")


def run_server(
    url="http://localhost:8086",
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
):
    os.chdir(FOLDER)
    server_address = ("127.0.0.1", 8086)
    httpd = server_class(server_address, handler_class)
    open_browser(url)
    httpd.serve_forever()


def open_browser(url):
    webbrowser.open_new_tab(url)


if __name__ == "__main__":
    run_server()
