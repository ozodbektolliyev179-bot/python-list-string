faoliyatlar = input("Faoliyat turlarini kiriting: ")

items = faoliyatlar.split(",")

snake_case_items = []

for item in items:
    item = item.strip().lower()     
    item = item.replace(" ", "_")   
    snake_case_items.append(item)

result = "_".join(snake_case_items)
print(result)

