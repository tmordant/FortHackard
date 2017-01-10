#! /usr/bin/python
from ChiffreurHill import getCouplePourChiffrement, produitToutesLesPaires, couplesEnCaracteres
from DechiffreurHill import genererComatrice, genererInverseMatrice
import numpy

def genererMatrice():
	a = 3;
	b = 5;
	c = 6;
	d = 17;
	matrice = numpy.array([[a, b],  [c, d]]);
	return matrice;
	
def separationEnPaires(lesCouples):
	if(len(lesCouples)%2==1):
		lesCouples.append(6);
	result = list();
	i = 0;
	while i < len(lesCouples):
		l = list();
		l.append(lesCouples[i]);
		l.append(lesCouples[i+1]);
		result.append(l);
		i=i+2;
	return result;

if __name__ =="__main__":
	entree = "TEXTEACRYPTER";
	
	l = list(entree);
	couples = getCouplePourChiffrement(l);
	couples = separationEnPaires(couples);
	e = genererMatrice();
	prod = produitToutesLesPaires(e, couples);
	
	sortie = couplesEnCaracteres(prod);
	assert(sortie=="ZAITMYNPRJZADW");
	
	
	entree = "ZAITMYNPRJZADW";
	
	l = list(entree);
	couples = getCouplePourChiffrement(l);
	couples = separationEnPaires(couples);
	
	comE = genererComatrice(e);
	invE = genererInverseMatrice(comE, e);
	prod = produitToutesLesPaires(invE, couples);
	
	sortie = couplesEnCaracteres(prod);
	sortie = sortie[:-1];
	assert(sortie=="TEXTEACRYPTER");
