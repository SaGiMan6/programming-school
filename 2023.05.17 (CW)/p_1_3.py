# Задание: "Словарь 3_1"

sweet = {"id": "0001", "type": "donut", "name": "Cake", "ppu": 0.55, "calories": 125}


sweet["weight"] = 230
sweet["have_topping"] = True
sweet["name"] = "SuperCake"
sweet["calories"] = 350


for value in sweet:
    print(f"{value} - {sweet[value]}")
