import socket, select, string, sys
from Crypto.Cipher import AES
import base64


def encrypt(raw):
	cipher = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
	return (cipher.encrypt(raw))
def decrypt(enc):
	cipher = AES.new('This is a key123', AES>MODE_CFB, 'This is an IV456')
	return (cipher.decrypt(enc))
def prompt():
	sys.stdout.write('<You> \n')
	sys.stdout.flush()

if __name__ == "__main__":

	if(len(sys.argv) <3):
		print 'Usage : python Client.py hostname port(default 4032)'
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	# Connect to the server
	try :
		s.connect((host, port))
	except :
		print 'Connection failed'
		sys.exit()

	print 'Connection established. Start sending messages'
	prompt()

	while 1:
		socket_list = [sys.stdin, s]

		# Get the list sockets
		read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

		for sock in read_sockets:
		# Read messages coming from server
			if sock == s:
				data = sock.recv(10000)
				if not data :
					print '\n Disconnected from server'
					sys.exit()
				else :
					# Print data
					data1 = str(data[24:])
			# Decrypt the message
					decoded_chat=decrypt(data1)
					sys.stdout.write(decoded_chat)
					prompt()
			# Enter your message
			else :
				msg = sys.stdin.readline()
			# Encrypt the message
				encrypted_chat=encrypt(msg)

				s.send(encrypted_chat)
				prompt()
