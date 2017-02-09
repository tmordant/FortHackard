#! /usr/bin/python
from random import randint;


if __name__=="__main__":
	l = [13, 248, 176, 147, 167, 93, 193, 109, 52, 141, 225, 99, 189, 4, 130]
	lHex = list();
	lBin = list();
	for i in range(0, len(l)):
		lHex.append(hex(l[i]));
		lBin.append(bin(l[i]));
	print l;
	print lHex;
	print lBin;
