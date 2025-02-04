from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS  # Ajout de Flask-CORS

app = Flask(__name__)
CORS(app)  # Active CORS pour toutes les routes

# Assurer que le dossier "replays" existe
UPLOAD_FOLDER = "replays"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route pour tester si l'API fonctionne
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API War Selection en ligne"}), 200

# Route pour recevoir un fichier replay
@app.route('/api/replay', methods=['POST'])
def upload_replay():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return jsonify({"message": f"Fichier {file.filename} reçu avec succès"}), 200

# Route pour lister les replays
@app.route("/api/list_replays", methods=["GET"])
def list_replays():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files)

# Route pour télécharger les fichiers replays
@app.route("/replays/<filename>", methods=["GET"])
def get_replay(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
