inp = "How much wood would a woodchuck chuck if the woodchuck could chuck wood ?"
words = inp.split(" ")
ls = dict()
count = 0
c = 0
for word in words:
    if word in ls:
        ls[word] += 1
        c += 1
    else:
        ls[word] = 1
        count += 1
print(f"total {count - c} unique words")
for key,value in ls.items():
    print(f"{key}:{value} times")
