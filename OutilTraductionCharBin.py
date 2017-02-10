#! /usr/bin/python
# -*-coding:Latin-1 -*
from GenerationPIN import *;
from OutilDivideAndConquer import *;


if __name__=="__main__":
	print("\n\n################################################################################################################################################");
	print("#### Bienvenue dans cet outil vous permettant de traduire des caractères d'ASCII vers le binaire afin de réaliser plus facilement l'attaque ####");
	print("################################################################################################################################################\n\n");
	print("L'alphabet considéré est donc le suivant : " + ALPHABETMDP +"\n");
	print("Nous allons procéder à son analyse...\n");
	for i in range(0, len(ALPHABETMDP)):
		print("Le caractère " + ALPHABETMDP[i] + " a la représentation binaire ASCII suivante : " + str(padding(bin(ord(ALPHABETMDP[i]))[2:])));
