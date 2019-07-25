ls = []
lst = [[0,1,2,3],
 [3,4,5,5],
 [6,7,8,8],
 [9,0,1,9]]
for i in lst:
    ls.extend(i)
print(ls)
print(f"minimum value element in the array: {min(ls)}")
print(f"maximum value element in the array: {max(ls)}")

print(f"elements with minimum values row-wise: {list(map(lambda x:min(x) ,lst))}")
print(f"elements with minimum values row-wise:{list(map(lambda x:max(x) ,lst))}")
print(f"elements with minimum values column-wise: {list(min(map(lambda x:x[i],lst)) for i in range(4))}")
print(f"elements with maximum values column-wise:  {list(max(map(lambda x:x[i],lst)) for i in range(4))}")
