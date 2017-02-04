#! /usr/bin/python
import sys;
import os
import filecmp;


def testFichiersEgaux(entreeChiffreur, sortieDechiffreur):
	entree = "";
	sortie = "";
	with open(entreeChiffreur, 'r') as myfile:
    		entree=myfile.read().replace('\n', '')
    	with open(sortieDechiffreur, 'r') as myfile:
    		sortie=myfile.read().replace('\n', '')
    	assert(entree==sortie);
	


if __name__ == "__main__":
	sys.argv = ['TestInputChiffreurPolybe.txt', 'TestOutputChiffreurPolybe.txt'];
	execfile('ChiffreurPolybe.py');
	sys.argv = ['TestOutputChiffreurPolybe.txt', 'TestOutputDechiffreurPolybe.txt'];
	execfile('DechiffreurPolybe.py');
	testFichiersEgaux('TestInputChiffreurPolybe.txt', 'TestOutputDechiffreurPolybe.txt');
	
