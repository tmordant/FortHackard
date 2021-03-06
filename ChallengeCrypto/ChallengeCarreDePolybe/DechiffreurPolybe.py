#! /usr/bin/python
from ChiffreurPolybe import recupererClef, invalidChar

def dechiffrer(laClef, contenuEntree):
	data = contenuEntree.read();
	l = list(data);
	listDechiffree = list();
	i = 0;
	for char in l:
		if not (invalidChar(char)):
			if not(estUnChiffre(char)):
				nextChar = l[i+1];
				char = getDechiffre(char, nextChar, laClef);
		if not(estUnChiffre(char)):
			listDechiffree.append(char);
		i = i+1;
	return ''.join(listDechiffree);
	
def estUnChiffre(char):
	return (char=='1' or char=='2' or char=='3' or char=='4' or char=='5');

def getIndexLigne(lettreCarre):
	indexLigne = 0;
	if(lettreCarre=='A'):
		indexLigne = 0;
	elif(lettreCarre=='B'):
		indexLigne = 1;
	elif(lettreCarre=='C'):
		indexLigne = 2;
	elif(lettreCarre=='D'):
		indexLigne = 3;
	else:
		indexLigne = 4;
	return indexLigne;
	
def getIndexColonne(chiffreCarre):
	indexLigne = 0;
	if(chiffreCarre=='1'):
		indexLigne = 0;
	elif(chiffreCarre=='2'):
		indexLigne = 1;
	elif(chiffreCarre=='3'):
		indexLigne = 2;
	elif(chiffreCarre=='4'):
		indexLigne = 3;
	else:
		indexLigne = 4;
	return indexLigne;

def getDechiffre(lettreCarre, chiffreCarre, laClef):
	indexLigne = getIndexLigne(lettreCarre);
	indexColonne = getIndexColonne(chiffreCarre);
	indexString = indexLigne*5+indexColonne;
	return laClef[indexString];

if __name__ == "__main__":
	contenuEntree = open("TestInputDechiffreurPolybe.txt");
	contenuSortie = open("TestOutputDechiffreurPolybe.txt", "w");
	
	clef = recupererClef();
	sortie = dechiffrer(clef, contenuEntree);
	contenuSortie.write(sortie);
	
	
	
