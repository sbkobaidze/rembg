from flask import Flask,request,jsonify
from rembg import remove
import base64

app = Flask(__name__)

@app.route("/rembg",methods=['POST'])
def removeBackground():
    if request.method != 'POST':
        return jsonify({'error': 'Invalid request method'}), 500
    
    try:
        data = request.get_json()
        input_base64 = data.get('base64')

        if not input_base64:
            return jsonify({'error': 'Missing or invalid "image_base64" in JSON payload'}), 400

        input_data = base64.b64decode(input_base64)
        output_data = remove(input_data)
        output_base64 = base64.b64encode(output_data).decode()

        return jsonify({'output_base64': output_base64})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500




if __name__ == "__main__":
    app.run(debug=True)