from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class ContactHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Обрабатываем только путь /contacts или /
        if self.path == "/contacts" or self.path == "/":
            try:
                with open("contacts.html", "r", encoding="utf-8") as f:
                    html_content = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html_content.encode("utf-8"))
            except FileNotFoundError:
                self.send_error(404, "Файл contacts.html не найден")
        else:
            self.send_error(404, "Страница не найдена")

    def do_POST(self):
        # Обрабатываем POST-запрос на /contacts
        if self.path == "/contacts":
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            # Декодируем данные формы
            data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            print("Получены POST-данные:")
            for key, value in data.items():
                print(f"  {key}: {value[0]}")
            # Отправляем ответ
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            response = "<h1>Спасибо! Ваше сообщение отправлено.</h1><a href='/contacts'>Вернуться</a>"
            self.wfile.write(response.encode("utf-8"))
        else:
            self.send_error(404)

def run(server_class=HTTPServer, handler_class=ContactHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущен на http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()