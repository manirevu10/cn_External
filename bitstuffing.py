st = input("Enter the frame: ")
count = 0
res = ""
for i in st:
    if i == '1' and count < 5:
        res += '1'
        count += 1
    else:
        res += i
        count = 0
    if count == 5:
        res += '0'
        c = 0
    print(res)

print("Frame after bit stuffing: ",res)
