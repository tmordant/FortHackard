#! /usr/bin/python
# -*-coding:Latin-1 -*
import time;
import binascii;
from GenerationPIN import *;
from random import *;

motDePasse = ['O', 'n', 'M', 't', 'Z', 'k', '*', '@', 'I', 'W', ';', '=', '#', 'y', 'x', 'n'];

def comparerBits(octetEntree, octetMdp):
	for i in range(0, len(octetEntree)):
		if(octetEntree[i]!=octetMdp[i]):
			break;
		else:
			delaiAttente(i);
			
			
def delaiAttente(indice):
	time.sleep(dureeAleatoire[indice]);

		
def comparer(entree, mdp):
	for j in range(0, len(entree)):
		comparerBits(entree[j], mdp[j]);
	
def str2bool(v):
	return v.lower() in ("yes", "y", "oui", "o", "true", "t", "1");

def padding(binaire):
	while(len(binaire)<8):
		binaire = '0' + binaire;
	return binaire;

if __name__=="__main__":
	#motDePasse = genererMotDePasse();   utilisation et stockage une fois pour que l'utilisateur puisse predire
	dureeAleatoire = list();
	for i in range(0,8):
		dureeAleatoire.append(random());
	print("\n\n################################################################################################################################################");
	print("#### Bienvenue dans cet outil vous permettant d'obtenir des informations sur le temps mis pour comparer votre entrée au mot de passe requis ####");
	print("################################################################################################################################################\n\n");
	choix = raw_input("Voulez-vous saisir votre entrée en binaire ou sous forme de caractères ? (0 : saisie binaire, 1 : saisie caractère) \n\n");
	if (str2bool(choix)):
		entree = raw_input("\nVeuillez entrer votre mot de passe : ");
		lEntree = list();
		lMdp = list();
		for char in entree:
			lEntree.append(padding(bin(ord(char))[2:]));
		for char in motDePasse:
			lMdp.append(padding(bin(ord(char))[2:]));
		print("\n\nDémarrage du timer !");
		debut = time.time();
		comparer(lEntree, lMdp);
		fin = time.time();
		temps = fin-debut;
		print("\n\nLe temps que vous avez mis afin d'exécuter ce script est de " + str(temps) + " secondes.");
	else:
		entree = raw_input("\nVeuillez entrer votre mot de passe : ");
		lMdp = list();
		tailleOctet = 8;
		entree = [entree[i:i+tailleOctet] for i in range(0, len(entree), tailleOctet)];
		for char in motDePasse:
			lMdp.append(padding(bin(ord(char))[2:]));
		print("\n\nDémarrage du timer !");
		debut = time.time();
		comparer(entree, lMdp);
		fin = time.time();
		temps = fin-debut;
		print("\n\nLe temps que vous avez mis afin d'exécuter ce script est de " + str(temps) + " secondes.\n");
