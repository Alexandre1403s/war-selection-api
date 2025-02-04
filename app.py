from flask import Flask, request
import os

app = Flask(__name__)

# Assurer que le dossier 'replays' existe
os.makedirs("replays", exist_ok=True)

@app.route('/api/replay', methods=['POST'])
def receive_replay():
    if 'file' not in request.files:
        return {"error": "Aucun fichier reçu"}, 400
    
    file = request.files['file']
    file_path = os.path.join("replays", file.filename)
    file.save(file_path)  # Sauvegarde du fichier

    return {"message": f"Fichier {file.filename} reçu avec succès"}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
