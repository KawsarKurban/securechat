import socket
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
private_key = RSA.generate(4096, random_generator)
public_key = private_key.publickey()

s = socket.socket()
host = "XXX.XXX.XXX.XXX"
port = XXXX
encrypt_str = "encrypted_message="

if host == "127.0.0.1":
    import commands
    host = commands.getoutput("Hostname -I")
print "host = " + host

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host, port))

s.listen(5)

c, addr= s.accept()

while True:
    data = c.recv(1024)
    data = data.replace("\r\n", '')

    if data == "Client: OK":
        c.send("public_key=" + public_key.exportKey() + "\n")
        print "Public key sent to client."
    ##
    elif encrypt_str in data:
        data = data.replace(encrypt_str, '')
        print "Received:\nEncrypted message = "+str(data)
        encrypted = eval(data)
        decrypted = private_key.decrypt(encrypted)
        c.send("Server: OK")
        print "Decrypted message = " + decrypted
    
    elif data == "Quit": break

c.send("Server stopped\n")
print "Server stopped"
c.close()
