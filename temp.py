x = 5
def ha():
	from __main__ import x
	if x<6:
		x=8
	print(x)

print(x)
ha()
print(x)