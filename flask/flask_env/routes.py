from app import app

@app.route('/', methods=['GET'])
def health_check():
    return 'Healthy Check is up!'

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello world!'