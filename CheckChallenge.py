#! /usr/bin/python
# -*-coding:Latin-1 -*
import random
import os.path

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def init():
	if not(os.path.isfile("/home/tom/Bureau/ProjetLong/.salés")):
		f = open('.salés', 'w');
		nbEpreuves = 1;
		for j in range(nbEpreuves):
			chars=[]
			for i in range(16):
				chars.append(random.choice(ALPHABET))
			salt = ''.join(chars);
			print salt;
	else :
		print 'héhé';
			
			

if __name__ == "__main__":
	init();
	fo = open('.salés', 'w');
	
	fi = open('.salés', 'r');
	#if sys.argv[0]==1:
		#hash = 
		#if
