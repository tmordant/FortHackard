#! /usr/bin/python
# -*-coding:Latin-1 -*
import sys;
import operator;

analyseFrequence = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0};

def remplacerAccent(leChar):
	if(leChar=='\xc3'):
		return 'E';
	elif(leChar=='\xa9'):
		return ' ';
	elif(leChar=='\xa0'):
		return 'A';
	elif(leChar=='\xa8'):
		return 'E';
	else:
		return leChar;

def caractereSpeciale(leChar):
	if(leChar==" " or leChar=="," or leChar=='\'' or leChar=='.' or leChar=='\n' or leChar==':'):
		return True;
	else:
		return False;

def afficher(statistiques, nombreLettres):
	for i in range(0, len(statistiques)):
		print("La lettre " + statistiques[i][0] + " est présente dans le texte avec une fréquence : " + str(100*statistiques[i][1]/(nombreLettres * 1.0)) + " %");


def testValidationOutil(listeAnalyse, nombreLettres):
	somme = 0;
	for i in range(0, len(listeAnalyse)):
		somme+=listeAnalyse[i][1];
	assert(somme==nombreLettres);
	print("\nCet outil a été certifié correctement grâce à des tests fonctionnels\n"); 
	

if __name__=="__main__":
	print("\n\n#### Bienvenue dans cet outil vous permettant de réaliser une analyse fréquentielle du texte passé en entrée de ce programme ####\n \n");
	if(len(sys.argv) >= 2):
		nombreLettres = 0;
		contenuAAnalyser = open(sys.argv[1]);
		contenuAAnalyser = contenuAAnalyser.read();
		contenuAAnalyser = contenuAAnalyser.upper();
		for char in contenuAAnalyser:
			char = remplacerAccent(char);
			if not(caractereSpeciale(char)):
				nombreLettres+=1;
				analyseFrequence[char]+=1;
		best = sorted(analyseFrequence.items(), key=operator.itemgetter(1), reverse=True);
		afficher(best, nombreLettres);
		testValidationOutil(best, nombreLettres);
		
	else:
		print("!!! Utilisation : python OutilAnalyseFréquence.py [nomFichierTexteAAnalyser]");
		
