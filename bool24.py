
A = int(input("Kiriting A: "))
B = int(input("Kiriting B: "))
C = int(input("Kiriting C: "))

flag = True

while A == 0:
	A = int(input("Kiriting A: "))

D = B*B - (4 * A * C)

if D >= 0:
	pass
else:
	flag = False



print(flag)