#! /usr/bin/python


def recupererClef():
	carreDePolybe = open("CarreDePolybe.txt");
	contenu = carreDePolybe.read().replace('\n', '');
	contenu = contenu.replace(' ', '');
	l = list(contenu);
	for i in range(1, 7):
		del(l[0]);
	for i in range(1, 5):
		del(l[i*5]);
	return ''.join(l);
	

def chiffrer(laClef, leContenu):
	data = leContenu.read();
	data = data.upper();
	l = list(data);
	listChiffree = list();
	for char in l:
		if not(invalidChar(char)):
			leIndex = laClef.index(char);
			ligne = getLigne(leIndex);
			colonne = getColonne(leIndex);
			char = ligne+colonne;
		listChiffree.append(char);
	return ''.join(listChiffree);
		

def invalidChar(char):
	return (char=='\'' or char =='?' or char == '!' or char == '.' or char == '-'  or char == ' ' or char=='\n' or char == ',' or char == '`');

def getColonne(index):
	index = index%5;
	if (index == 0):
		return '1';
	elif (index == 1):
		return '2';
	elif (index == 2):
		return '3';
	elif (index == 3):
		return '4';
	else:
		return '5';

def getLigne(index):
	if (index>=0 and index<=4):
		return 'A';
	elif (index>4 and index<=9):
		return 'B';
	elif (index>9 and index<=14):
		return 'C';
	elif (index>14 and index<=19):
		return 'D';
	else:
		return 'E';

if __name__ == "__main__":
	contenuEntree = open("TestInputChiffreurPolybe.txt");
	contenuSortie = open("TestOutputChiffreurPolybe.txt", "w");
	clef = recupererClef();
	sortie = chiffrer(clef, contenuEntree);
	contenuSortie.write(sortie);
	
	
