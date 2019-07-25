inp = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3"
ls = dict()
words = inp.split(" ")
#print(t)
for word in words:
    if word in ls:
        ls[word] += 1
    else:
        ls[word] = 1
print(ls) 

max = 0
min = 999
for v in ls.values():
    if max < v:
        max = v 
    if min > v:
        min = v
        
print(f"{max},{min}")
for key,value in ls.items():
    if ls[key] == max:
        print(f"{key}:{value}")
for key,value in ls.items():
    if ls[key] == min:
        print(f"{key}:{value}")
    
