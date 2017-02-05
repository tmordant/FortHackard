#! /usr/bin/python
# -*-coding:Latin-1 -*
import socket
import random
from Crypto.Cipher import AES


if __name__ == "__main__":
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind(('', 15555))
	
	
	while True:
		socket.listen(5)
		client, address = socket.accept()
		print "{} connected".format( address )

		response = client.recv(255)
		if response != "":
		
			b = random.randint(1,100);
			p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
			g = 2;
		        A = response.split("= ")[1];
		        secretCommun = long(A)^b%p;
		        print secretCommun
		        B = g^b%p;
		        print("Envoi de la clé publique de Bob à Alice afin de procéder à l'échange de clés de Diffie-Hellman");
		        client.send("B = " + str(B));
		        vecteurInitialisationCommun = "C'est l'IVcommun";
		        chiffrement = AES.new(str(secretCommun).zfill(16), AES.MODE_CBC, vecteurInitialisationCommun);
		        texteChiffre = chiffrement.encrypt("Ceci est le vrai flag permettant de valider l'épreuve : MITMAttackResistance".zfill(80));
		        client.send("C = " + texteChiffre);
		        
	print "Close"
	client.close()
	socket.close()
