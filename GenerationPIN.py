#! /usr/bin/python
from random import randint;

ALPHABETMDP = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&@#*,;:!=\"-_`'<>$+";

def genererMotDePasse():
	res = list();
	for i in range(0, 16):
		res.append(ALPHABETMDP[randint(0,len(ALPHABETMDP))]);
	return res;
