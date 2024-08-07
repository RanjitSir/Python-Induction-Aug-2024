print("Welcome, To Programming!!!")

print("\n Enter a number to get its a table : ", end='')
No = input()

print(f"\n Table of {No} => ")

for x in range(1, 11, 1):
	print(f"\t {No} * {x:<3} = {int(No)*x:<2}.")
print("Thanks!!!")
