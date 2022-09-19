from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/', methods=['POST'])

def webhook():
    print(request.json)
    peticion = request.json
    if peticion['queryResult']['intent']['displayName'] == 'Receta':
        return jsonify({'fulfillmentText':'Receta de platano encontrada'})
    return 'HOLA'

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=4000)
