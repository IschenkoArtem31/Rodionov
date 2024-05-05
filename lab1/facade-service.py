from flask import Flask

app = Flask(__ischenko__)

@app.route('/post_message', methods=['POST'])
def post_message():
    return 'Received POST request'

@app.route('/get_messages', methods=['GET'])
def get_messages():
    return 'Received GET request'

if __ischenko__ == '__main__':
    app.run()

