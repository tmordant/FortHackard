#! /usr/bin/python
# -*-coding:Latin-1 -*
import time;
import binascii

motDePasse = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

def comparerBits(octetEntree, octetMdp):
	print octetEntree
	for i in range(0, 7):
		if(octetEntree[i+2]!=octetMdp[i+2]):
			break;
		print octetEntree[i+2]

def comparer(entree, mdp):
	for j in range(0, len(entree)):
		comparerBits(entree[j], mdp[j]);
		
	

if __name__=="__main__":
	print("\n\n#### Bienvenue dans cet outil vous permettant d'obtenir des informations sur le temps mis pour comparer votre entrée au mot de passe requis ####\n\n");
	choix = raw_input("Voulez-vous saisir votre entrée en binaire ou sous forme de caractères ? (0 : saisie binaire, 1 : saisie caractère ) \n\n");
	if (choix):
		entree = raw_input("\nVeuillez entrer votre mot de passe : ");
		lEntree = list();
		lMdp = list();
		for char in entree:
			lEntree.append(bin(ord(char)));
		for char in motDePasse:
			lMdp.append(bin(ord(char)));
		print("\n\nDémarrage du timer !");
		debut = time.clock();
		comparer(lEntree, lMdp);
		fin = time.clock();
		temps = fin-debut;
		print("\n\nLe temps que vous avez mis afin d'exécuter ce script est de " + str(temps) + " secondes.");
	else:
		entree = raw_input("\nVeuillez entrer votre mot de passe : ");
		lEntree = list();
		lMdp = list();
		for char in entree:
			lEntree.append(bin(ord(char)));
		for char in motDePasse:
			lMdp.append(bin(ord(char)));
		print("\n\nDémarrage du timer !");
		debut = time.clock();
		comparer(lEntree, lMdp);
		fin = time.clock();
		temps = fin-debut;
		print("\n\nLe temps que vous avez mis afin d'exécuter ce script est de " + str(temps) + " secondes.\n");
