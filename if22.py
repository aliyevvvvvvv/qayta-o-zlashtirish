x = int(input("kiriting x: "))
y = int(input("kiriting y: "))

result = 0

if x == y == 0 or x == 0 or y == 0:
	pass
elif x > 0 and y > 0:
	result = 1
elif x < 0 and y > 0:
	result = 2
elif x < 0 and y < 0:
	result = 3
elif x > 0 and y < 0:
	result = 4

print(result)