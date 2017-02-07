#! /usr/bin/python
# -*-coding:Latin-1 -*
import sys;

listeBigramme = [];
listeLettre = [];

def verifierBigrammeInutilise(bigramme):

def verifierLettreInutilisee(lettre):

	


if __name__=="__main__":
	print("\n\n#### Bienvenue dans cet outil vous permettant de vous assister à déchiffrer, par dichotomie, des textes chiffrés à l'aide d'un carré de Polybe. ####\n \n");
	if(len(sys.argv) >= 3):
		contenuADechiffre = open(sys.argv[1]);
		contenuCarrePolybe = open(sys.argv[2]);
		print("Voici le contenu du fichier choisi : \n\n");
		contenuDec = contenuADechiffre.read();
		contenuCarrePolybe = contenuCarrePolybe.readlines();
		print contenuDec;
		print("\n\nLe contenu de votre carré de Polybe saisi est le suivant : ");
		print(contenuCarrePolybe);
		for couples in contenuCarrePolybe:
			couples = couples.split(", ");
			bigrammeChiffre = couples[0][1:];
			verifierBigrammeInutilise(bigrammeInutilise);
			lettreDechiffre = couples[1][0];
			verifierLettreInutilisee(lettreDechiffre);
			contenuDec = contenuDec.replace(bigrammeChiffre, lettreDechiffre);
		print("\n\nLe contenu du fichier après traduction donne donc ceci : ");
		print(contenuDec);
			
		
		
	else:
		print("!!! Utilisation : python OutilDechiffrementPolybe.py [nomFichierTexteChiffré] [nomFichierCarreDePolybe]");
		print("!!! Veuillez rentrer dans le [nomFichierCarreDePolybe] les couples (un par ligne) permettant le déchiffrement sous la forme (bigramme chiffré, lettre déchiffrée)\n\n");
