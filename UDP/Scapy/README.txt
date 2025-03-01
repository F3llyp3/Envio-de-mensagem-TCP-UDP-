Se o servidor não estiver recebendo mensagem,
execute o comando como admin:

netsh advfirewall firewall add rule name="Allow UDP 12345" dir=in action=allow protocol=UDP localport=12345
