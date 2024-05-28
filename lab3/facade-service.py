from flask import Flask, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/post_message', methods=['POST'])
def post_message():
    data = request.json
    messages.append(data)
    return 'Received POST request'

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/', methods=['GET'])
def view_messages():
    return str(messages) + "\n"

if __name__ == '__main__':
    app.run()

