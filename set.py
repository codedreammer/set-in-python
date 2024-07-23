''' s = {2,4,5,2}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

for value in info:
    print(value)

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
print(s1 , s2)

#another example of union
class1 = {"akshay","anand","ram","shyam","aam","nam"}
class2 = {"kam","dham","akshay","alok","anand","dham"}
classcombined = class1.union(class2)
print(classcombined)

#intersection (this gives the comman of all the list)
class1 = {"akshay","anand","ram","shyam","aam","nam"}
class2 = {"kam","dham","akshay","alok","anand","dham"}
classcombined = class1.intersection(class2)
print(classcombined)
'''
#symmetric_difference
class1 = {"akshay","anand","ram","shyam","aam","nam"}
class2 = {"kam","dham","akshay","alok","anand","dham"}
classcombined = class1.symmetric_difference(class2)
print(classcombined)

call1 = {"akshay","anand","ok"}
call2 = {"akshay","anand","alok"}
callcombined = call1.symmetric_difference(call2)
print(callcombined)





