from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_data():
    try:
        # Получение данных, отправленных C++ кодом
        data = request.get_data().decode('utf-8')
        print(f"Received data: {data}")
        
        # Обработка данных (например, запись в файл)
        with open("received_data.txt", "a") as file:
            file.write(data + "\n")
        
        return "Data received", 200
    except Exception as e:
        print(f"Error receiving data: {e}")
        return "Error", 500

if __name__ == '__main__':
    # Запуск HTTPS-сервера с использованием SSL сертификатов
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'))
