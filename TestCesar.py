#! /usr/bin/python
import sys;
import filecmp;


def testFichiersEgaux(entreeChiffrement, sortieDechiffrement):
	assert(filecmp.cmp(entreeChiffrement, sortieDechiffrement));


if __name__ == "__main__":
	sys.argv = ['TestInputEncryption.txt', 'TestOutputEncryption.txt'];
	execfile('Encryption.py');
	sys.argv = ['TestOutputEncryption.txt', 'TestOutputDecryption.txt'];
	execfile('Decryption.py');
	testFichiersEgaux('TestInputEncryption.txt', 'TestOutputDecryption.txt');
