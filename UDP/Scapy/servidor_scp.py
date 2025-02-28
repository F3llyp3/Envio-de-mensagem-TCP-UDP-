from scapy.all import sniff, IP, UDP, send

#funçao p processar pacotes
def process_pacote(pacote):
    if pacote.haslayer(UDP): #verifica se o pacote é UDP
        origem_ip = pacote[IP].src #captura o IP de origem do pacote 
        origem_port = pacote[UDP].sport #captura o porta de origem do cliente 
        mensagem = bytes(pacote[UDP].payload).decode(errors="ignore") # recebe e decodifica a mensagem

        print(f"mensagem recebida de {origem_ip}: {origem_port} -> {mensagem}")
        
        #pacote resposta
        resposta = IP(dst=origem_ip)/ UDP(dport=origem_port, sport=12345)/"Mensagem recebida!"
        send(resposta)
        print(f"Resposta enviada para {origem_ip}:{origem_port}")

#Iniciar captura de pacotes na porta 12345
print("Servidor aguardando mensagens UDP...")
sniff(filter="udp port 12345", prn=process_pacote, store=False)