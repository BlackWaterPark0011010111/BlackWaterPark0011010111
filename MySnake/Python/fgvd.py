import re
string = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

char = ""
for i in string:
    if i.isalpha():
        char = "".join([char, i])
print(str(char))


#str1 = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']
#charr = "".join(re.findall([1-9], str1))
#numbers = "".join(re.findall("\d+", str1))
#print(str1(charr))