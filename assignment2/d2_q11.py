Cricket = [ "PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"]
Football = [ "PKM", "ALN","RMZ","CS", "MCS"]
Badminton = [ "PKM", "ALN", "NV", "KM","RMV"]
all_3 = []
def is_Football(per):
    if per in Football:
        return True
    else:
        return False

def is_Badminton(per):
    if per in Badminton:
        return True
    else:
        return False

def is_Cricket(per):
    if per in Cricket:
        return True
    else:
        return False

for i in Cricket:
    if is_Football(i):
        if is_Badminton(i):
            all_3.append(i)
print(all_3)

one = []
for i in Cricket:
    if (is_Football(i) or is_Badminton(i)) == False:
        one.append(i)
for i in Football:
    if (is_Cricket(i) or is_Badminton(i)) == False:
        one.append(i)
for i in Badminton:
    if (is_Football(i) or is_Cricket(i) )== False:
        one.append(i)
print(one)