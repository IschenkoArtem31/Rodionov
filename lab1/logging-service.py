from flask import Flask

app = Flask(__ischenko__)

@app.route('/log_message', methods=['POST'])
def log_message():
    return 'Received POST request'

@app.route('/get_logs', methods=['GET'])
def get_logs():
    return 'Received GET request'

if __ischenko__ == '__main__':
    app.run()

