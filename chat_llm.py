from flask import Flask, request, jsonify
import json
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/generate": {"origins": "*"}})

# Mock list of responses
responses = [
    "Sure, I can help with that!",
    "I'm not sure about that, can you ask something else?",
    "That's an interesting question!",
    "Let me think about it...",
    "Can you provide more details?",
    "That's beyond my knowledge at the moment.",
    "I will need more information to answer that.",
    "What do you think about it?",
    "Let's find out together!",
    "That's a tough one, but I'll do my best!"
]

@app.route('/generate', methods=['POST', 'OPTIONS'])
def send_message():
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        print(response)
        return response
    
    # Handle actual POST request
    data = request.get_json()
    print(f"Received data: {data}")  # Debug print

    if isinstance(data, str):
        data = json.loads(data)
        print(data)

    query = data.get('message', '')  # Use .get to avoid KeyError
    response = random.choice(responses)
    print( query)
    
    return jsonify({'message': response})

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
