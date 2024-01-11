from flask import Flask, request, jsonify
from rembg import remove
import base64
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if request.method != 'POST':
        return jsonify({'error': 'Invalid request method'}), 500

    try:
        data = request.get_json()
        url = data.get('url')
        response = requests.get(url)
        if response.status_code != 200:
            return jsonify({'error': 'Failed to fetch image from URL'}), 400

        # Read the image data
        image_data = response.content





        output_data = remove(image_data)
        output_base64 = base64.b64encode(output_data).decode()

        return jsonify({'output_base64': output_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000),debug=True,host='0.0.0.0')
