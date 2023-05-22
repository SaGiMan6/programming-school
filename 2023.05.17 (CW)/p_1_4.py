# Задание: "Словарь 3_1"

sweet = {"id": "0001","type": "donut", "name": "Cake", "ppu": 0.55, "calories": 125}


sweet.pop("ppu")
sweet.pop("type")


for value in sweet:
    print(f"{value} - {sweet[value]}")
