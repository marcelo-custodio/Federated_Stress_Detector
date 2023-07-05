from flask import Flask, request, jsonify
import pandas as pd
import random

# carregar o arquivo CSV
dataset = pd.read_csv('dataset.csv')

app = Flask(__name__)

@app.route('/random_data', methods=['GET'])
def get_random_data():
    # selecionar um dado aleatório da coluna "Stress"
    random_data = dataset['Stress'].sample(n=1).iloc[0]
    
    return jsonify({'data': random_data})

@app.route('/other_endpoint', methods=['POST'])
def receive_data():
    data = request.get_json()
    value = data['value']
    print(f"Received data from ESP: {value}")

    # retorne uma resposta para o ESP, se necessário
    response = {'message': 'Data received successfully'}
    return jsonify(response), 200

# verifica se o dataset foi carregado corretamente
if not dataset.empty:
    print("Dataset loaded successfully")
else:
    print("Failed to load dataset")

# inicia servidor Flask
app.run(host='0.0.0.0', port=5000)
