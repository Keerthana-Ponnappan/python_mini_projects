f =open("sample.txt")
l = f.readline()
for j in l:
    if j[0] != 'T':
        print(f.readline())
f.close()

