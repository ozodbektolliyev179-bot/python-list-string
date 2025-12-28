


data = "Ism:Ali, Familiya:Valiyev, Yil:2002"

i  = data.split(", ")

for n in i:
    key, value = n.split(":")
    print(f"{key}: {value}")
