from scapy.all import IP, UDP, send

#endereço
server_ip = "192.168.100.253" #IP do servidor
server_port = 12345 #porta do servidor

#cria o pacote UDP
pacote = IP(dst=server_ip)/UDP(dport=server_port, sport=54321)/"Ativar Lora"

#envia o pacote
send(pacote, verbose=True)
print(f"Mensagem enviada para {server_ip}:{server_port}")