'''3.	Write a program to determine the work hours of the day entered based on the timetable provided below.

Mon	Tue	Wed	Thu	Fri	Sat	Sun
3	3	3	3	3	3	0
2	2	2	2	2	1	0
2	2	2	1	1	0	0
	
Example:
Input: Thu
		Output: [3,2,1]
	
Input: Sat
Output: [3,1,0]
'''
tab = {"mon":[3,2,2],"tue":[3,2,2],"wed":[3,2,2],"thu":[3,2,1],"fri":[3,2,1],"sat":[3,1,0],"sun":[0,0,0]}
print(tab)
inp = input("enter the day:")
for key,val in tab.items():
    if inp == key:
        print(val)