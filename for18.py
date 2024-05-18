A = float(input("KIriting A "))
N = int(input("KIriting N "))

while N <= 0:
	N = int(input("KIriting N "))

summ = 1 - A

for i in range(1,N+1):
	print(summ)
	summ += pow(-1,i) * pow(A,i)