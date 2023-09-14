# Задание: "Словарь 3_2"

d1 = {'India': 'Delhi',
      'Canada': 'Ottawa',
      'United States': 'Washington D. C.'}

d2 = {'France': 'Paris',
      'Malaysia': 'Kuala Lumpur'}


for name in d2:
    d1[name] = d2[name]


for value in d1:
    print(f"{value} - {d1[value]}")
