count = int(input("How many cookies do you want to make? "))

sugar = count*1.5/48
butter = count/48
flour = count*2.75/48
print("To make " + str(count) + " cookies, you will need:")
print(f"{sugar:7.2f} cups of sugar")
print(f"{butter:7.2f} cups of butter")
print(f"{flour:7.2f} cups of flour")
