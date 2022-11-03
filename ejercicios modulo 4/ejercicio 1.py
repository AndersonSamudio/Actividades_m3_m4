from os import strerror

counters = {chr(ch):0 for ch in range(ord('a'), ord('z')+1)}
file_name = input("Enter name :")

try:
    f = open(file_name, "aBc")
    for line in f:
        for char in line:
            if char.isalpha():
                counters[char.lower()]+=1
    f.close()
    for char in couters.keys():
        cnt = couters[char]
        if cnt > 99:
            print (char, '->', cnt)
            
except IOError as e:
    print("I/O error", strerror(e.errno))
