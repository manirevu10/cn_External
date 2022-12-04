head = input("Enter character that represents the starting delimiter: ")
tail = input("Enter character that represents the ending delimiter: ")
st = input("Enter the characters to be stuffed: ")

res = head
for i in st:
    if i == head or i == tail:
        res += (i * 2)
    else:
        res += i 

res += tail 

print("Frame after character stuffing: ",res)
