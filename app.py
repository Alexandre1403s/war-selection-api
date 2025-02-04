from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Assurer que le dossier "replays" existe
UPLOAD_FOLDER = "replays"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

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
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    return jsonify({"message": f"Fichier {file.filename} reçu avec succès"}), 200

# Route pour lister les fichiers replay
@app.route("/api/list_replays", methods=["GET"])
def list_replays():
    files = os.listdir(app.config["UPLOAD_FOLDER"])
    return jsonify(files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
