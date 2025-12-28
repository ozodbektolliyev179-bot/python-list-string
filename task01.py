ism = input("Ism Sharifingizni kiriting: ")

i = ism.split()

familiya = i[0]
ism_sharif = " ".join(i[1:])

result = f"{ism_sharif}, {familiya}"
print(result)
