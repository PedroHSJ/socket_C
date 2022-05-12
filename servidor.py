#!/usr/bin/env python3
import socket
import os


HOST = '0.0.0.0'     # Endereco IP do Servidor
PORT = 40000           # Porta que o Servidor escuta

def processarCliente(con, cliente):
	print('Conectado com', cliente)
	while True:
		msg = con.recv(1024)
		if not msg: break
		print(cliente, 'mensagem:', msg.decode())
		con.send(msg)
	print('Desconectando do cliente', cliente)
	con.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv = (HOST, PORT)
sock.bind(serv)
sock.listen(50)
while True:
	try:
		con, cliente = sock.accept()
	except: break
	if os.fork() == 0:
		#processo filho
		sock.close()
		processarCliente(con, cliente)
		os.exit(0)
	else:
		#processo pai
		con.close()
sock.close()
