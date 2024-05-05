from flask import Flask

app = Flask(__ischenko__)

@app.route('/get_message', methods=['GET'])
def get_message():
    return 'not implemented yet'

if __ischenko__ == '__main__':
    app.run()

