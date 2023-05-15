students = ["Atrem", "Stepa", "Misha", "Anton", "Timofey", "Lesha", "Vlad", "Polina", "Sonya", "Anischenko", "Grekhov"]

hight = [185, 182, 198, 191, 187, 187, 188, 174, 175, 184, 187]


h = dict(zip(students, hight))


for i in h:
    print(f"{i} - {h[i]}")