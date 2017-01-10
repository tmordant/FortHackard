#! /usr/bin/python
from ChiffreurHill import *
import numpy

def genererComatrice(laMatrice):
	laMatrice = laMatrice.tolist();
	
	cofacteurA = laMatrice[1][1];
	cofacteurB = -laMatrice[1][0];
	cofacteurC = -laMatrice[0][1];
	cofacteurD = laMatrice[0][0];
	
	comA = numpy.array([[cofacteurA, cofacteurB], [cofacteurC, cofacteurD]]);
	
	return comA;
	
	
def genererInverseMatrice(laComatrice, laMatrice):
	detLaMatrice = laMatrice[0][0]*laMatrice[1][1]-laMatrice[1][0]*laMatrice[0][1];
	if(estInversible(detLaMatrice)):
		transposeeComatrice = numpy.transpose(laComatrice);
		inverse = modinv(detLaMatrice, 26)*transposeeComatrice;
		inverse[0][0] = inverse[0][0]%26;
		inverse[0][1] = inverse[0][1]%26;
		inverse[1][0] = inverse[1][0]%26;
		inverse[1][1] = inverse[1][1]%26;
	return inverse;
	
	
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
 
def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m



if __name__ == "__main__":
	contenuEntree = open("InputDechiffreurHill.txt");
	contenuSortie = open("OutputDechiffreurHill.txt", "w");
	
	contenuEntree = contenuEntree.read();
	l = list(contenuEntree);
	couples = getCouplePourChiffrement(l);
	couples = separationEnPaires(couples);
	a = genererMatrice();
	comA = genererComatrice(a);
	e = genererInverseMatrice(comA, a);
	prod = produitToutesLesPaires(e, couples);
	chiffre = couplesEnCaracteres(prod);
	
	contenuSortie.write(chiffre);
