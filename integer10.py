A = int(input("kiriting А: "))

while A > 999 or A < 100:
	print(A)
	A = int(input("kiriting А: "))

a,b = divmod(A,100)

a,b = divmod(b,10)

print(b)

print(a)