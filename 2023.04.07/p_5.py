files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']


for i in range(len(files)):
    files[i] = files[i].lower()

files = list(set(files))
png_files = set()


for i in range(len(files)):
    if files[i][-4:] == ".png":
        png_files.add(files[i])


print(*sorted(png_files))
