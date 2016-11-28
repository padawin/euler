import math
import operator
import functools

def getPrimesTo(n):
	maxK = int(math.sqrt(n))
	primes = [2, 3, 5]
	toContinue = True
	k = 0
	while toContinue:
		for i in [1, 7, 11, 13, 17, 19, 23, 29]:
			prime = 30 * k + i
			if prime > maxK:
				toContinue = False
				break
			elif prime == 1:
				continue
			primes.append(prime)
		k += 1
	return primes

def divisors(n):
	orig = n
	sqrtOrig = math.sqrt(orig)
	multiples = []
	primes = getPrimesTo(n)
	found = False
	while not found:
		for p in primes:
			if n == 1:
				found = True
				break
			if (n % p) == 0:
				multiples.append(p)
				n = n // p
	print(multiples)

divisors(600851475143)
