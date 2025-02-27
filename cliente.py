import requests

# Envia a mensagem para o servidor
def send_message():
    url_fate = "http://127.0.0.1:5000/receives_message"  # Endereço do servidor
    data = {"mensagem": "Ativar Lora"}

    # Envia a requisição POST para o servidor destino
    response = requests.post(url_fate, json=data)

    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print("Falha ao enviar mensagem!")

# Chama a função para enviar a mensagem
send_message()
