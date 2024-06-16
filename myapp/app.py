import requests
from flask import Flask, jsonify, request, send_from_directory, Response
import os

app = Flask(__name__)

# Definir un diccionario de nombres de contenedores y puertos correspondientes
container_ports = {
    "container_1": 5001,
    "container_2": 5002,
    "container_3": 5003,
    "container_4": 5004,
    "container_5": 5005,
    "container_6": 5006,
    "container_7": 5007,
    "container_8": 5008,
    "container_9": 5009,
    "container_10": 5010
}

# Saludo
@app.route('/')
def hello_world():
    return {'message': 'hola, Mundo!!!'}

# Despedida
@app.route('/despedirse')
def bye_world():
    return {'message': 'Adiós, mundo!!!'}

# Ruta para listar archivos de un contenedor
@app.route('/storage')
def list_files():
    return os.listdir('/usr/src/app/sync_files/private'), 200

# Ruta para listar archivos públicos
@app.route('/public')
def list_public_files():
    public_path = '/usr/src/app/sync_files/public'
    if not os.path.exists(public_path):
        return jsonify({'error': 'Public directory not found'}), 404
    files = os.listdir(public_path)
    return jsonify(files)

# Ruta para descargar un archivo específico
@app.route('/download/<name_ext>')
def download_file(name_ext):
    public_path = '/usr/src/app/sync_files/public'
    file_path = os.path.join(public_path, name_ext)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    return send_from_directory(public_path, name_ext)

# Ruta para subir un archivo a un contenedor específico
@app.route('/upload/<name_ext>', methods=['POST'])
def upload_file(name_ext):
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Guardar el archivo en el directorio deseado dentro del contenedor
    file.save(os.path.join('/usr/src/app/sync_files/private', name_ext))

    return jsonify({'message': 'File uploaded successfully'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)