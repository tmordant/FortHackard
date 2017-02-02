#! /usr/bin/python
import numpy

def produit(A, B):
	a = A[0, 0]*B[0, 0] + A[0, 1]*B[1, 0];
	b = A[0, 0]*B[0, 1] + A[0, 1]*B[1, 1];
	c = A[1, 0]*B[0, 0] + A[1, 1]*B[1, 0];
	d = A[1, 0]*B[1, 0] + A[1, 1]*B[1, 1];
	return numpy.array([[a, b], [c, d]]);



if __name__ == "__main__":
	print("Veuillez entrer deux matrices A et B afin de calculer leur produit.");
	
	linputA = input("Veuillez entrer A sous la forme \"a b c d\" :\n");
	motsA = linputA.split();
	A = numpy.array([[int(motsA[0]), int(motsA[1])], [int(motsA[2]), int(motsA[3])]]);
	
	linputB = input("Veuillez entrer B sous la forme \"a b c d\" :\n");
	motsB = linputB.split();
	B = numpy.array([[int(motsB[0]), int(motsB[1])], [int(motsB[2]), int(motsB[3])]]);

	result = produit(A, B);
	print("\nLe produit matriciel est :");
	print(result);
