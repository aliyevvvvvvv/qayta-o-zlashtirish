N = int(input("kiriting N "))

while N <= 0:
	N = int(input("kiriting N "))

mul = 1.

for i in range(1,N+1):
	mul *= i

print(mul)
	