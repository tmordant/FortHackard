#! /usr/bin/python

import sys
from random import *
import numpy
sys.path.append("/home/tom/Bureau/ProjetLong/ChallengeCrypto/ChallengeCarreDePolybe");
from ChiffreurPolybe import invalidChar

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

def getCouplePourChiffrement(laListe):
	liste = list();
	for char in laListe:
		if not invalidChar(char):
			liste.append(ALPHABET.index(char));
	return liste;
	
def separationEnPaires(lesCouples):
	if(len(lesCouples)%2==1):
		lesCouples.append(randint(0, 25));
	result = list();
	i = 0;
	while i < len(lesCouples):
		l = list();
		l.append(lesCouples[i]);
		l.append(lesCouples[i+1]);
		result.append(l);
		i=i+2;
	return result;
	
	
def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b
	
		
def genererMatrice():
	a=randint(0,25);
	while not(estInversible(a)):
		a=randint(0,25);
	b=randint(0,25);
	c=randint(0,25);
	d=randint(0,25);
	result = a*d-b*c;
	while not(estInversible(result)):
		d=randint(0,25);
		result=a*d-b*c;
	matrice = numpy.array([[a, b], [c, d]]);
	return matrice;
		

def estInversible(adbc):
	return (pgcd(adbc, 26)==1);
			
def produitToutesLesPaires(matriceChiffrement, paires):
	l = list();
	for couples in paires:
		couples = numpy.asarray(couples);
		result = numpy.dot(matriceChiffrement, couples);
		result[0] = result[0]%26;
		result[1] = result[1]%26;
		result = result.tolist();
		l.append(result);
	return l;

def couplesEnCaracteres(leProduit):
	string = "";
	for couples in leProduit:
		string = string + ALPHABET[couples[0]];
		string = string + ALPHABET[couples[1]];
	return string;

if __name__=="__main__":
	contenuEntree = open("InputChiffreurHill.txt");
	contenuSortie = open("OutputChiffreurHill.txt", "w");
	
	contenuEntree = contenuEntree.read();
	l = list(contenuEntree);
	couples = getCouplePourChiffrement(l);
	couples = separationEnPaires(couples);
	e = genererMatrice();
	prod = produitToutesLesPaires(e, couples);
	chiffre = couplesEnCaracteres(prod);
	
	contenuSortie.write(chiffre);
