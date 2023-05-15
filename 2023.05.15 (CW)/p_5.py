# Задание: "Словарь 3"

s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange ' \
    'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry' \
    'apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon ' \
    'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple ' \
    'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
    'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
    'barley '

words = s.split()

result = {}

mx, fin_value = 0, ""


for word in words:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

for value in sorted(result):
    if result[value] > mx:
        mx = result[value]
        fin_value = value


print(fin_value)
