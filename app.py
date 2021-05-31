import flask
from flask import Flask, render_template
from flask import request
import predict_qa as predict

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    print ("iniciando")
    #return "<h1>Olá Mundo</h1><p>Teste WS com python</p>"
    return render_template('index.html')

@app.route("/respostas")
def respostas():
    print ("chamou QA")
    pergunta = request.args.get('pergunta')
    contexto = request.args.get('contexto')
    result = predict.predict(pergunta, contexto)
    print ("resposta")
    print (result)
    return result

#app.run()
app.run(host="0.0.0.0", port=int("5000"), debug=False)#map port to 5000
