from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para receber dados via solicitação POST
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    sensor = data['sensor']
    value = data['value']

    # Processar os dados recebidos conforme desejado
    # Por exemplo, você pode armazenar os dados em um banco de dados ou realizar alguma ação com base neles

    print(f"Received data from {sensor}: {value}")

    return 'Data received'

# Rota para obter dados via solicitação GET
@app.route('/data', methods=['GET'])
def get_data():
    # Lógica para retornar os dados em formato JSON
    # Certifique-se de que os dados estejam sendo retornados corretamente

    data = {
        'sensor': 'ESP32',
        'value': 42
    }

    return jsonify(data)

# Rota para imprimir "Hello, World!"
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)