from flask import Flask, jsonify, request
import requests
#cria o servidor
app = Flask(__name__)
#rota
@app.route('/receives_message', methods=['POST'])
def receives_message():
    #recebe dados
    dados_recebidos = request.get_json()
    if dados_recebidos:
        mensagem = dados_recebidos.get('mensagem', 'Mensagem teste')
        print(f"Mensagem recebida: {mensagem}")
        #respondendo
        return jsonify({"status": "Mensagem recebida com sucesso!", "mensagem": mensagem}), 200
    else:
        return jsonify({"erro": "Nenhuma mensagem encontrada!"}), 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

