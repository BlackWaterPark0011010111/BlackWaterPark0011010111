"""Now use a similar technique to mock an
  animated progress bar like this one:

[50,41,56,.......]

Define a function that takes a percentage and 
a width to draw a static view of the bar.
You can use str * int to obtain the amount of hashe
s and empty spaces you should print according to the
 percentage passed.
Instead of concatenating strings, build an array with 
the different parts of the progress bar and then unpack
 them to pass them to the print function.
Once you have that, write an iteration from 0 to 100 
(included) to call your previous function and remember
 to print the \r to overwrite each bar and produce the 
 animation effect.
Use the sleep function from the time module to make
 the progress bar update every 10 milliseconds.
Your result should look like this:
$ python3 script.py
[                              ] 0%
$ python3 script.py
[#######                       ] 24%
$ python3 script.py
[############                  ] 43%
$ python3 script.py
[#########################     ] 86%
$ python3 script.py
[##############################] 100%"""


from redirect import redir

redir()
#simple len approach
list_of_nums=[]
with open(r'C:\Users\roxfo\OneDrive\PYTHON\Python\03.01.2024IOfiles\data\task6.txt') as f:
  for line in f.readlines():
    list_of_nums.append(len(line))
print(list_of_nums)





"""complicated tell() approach"""
list_of_nums=[]
with open(r'C:\Users\roxfo\OneDrive\PYTHON\Python\03.01.2024IOfiles\data\task6.txt') as file:
    num_of_lines = file.readlines()
    file.seek(0)
    previous = 0
    for  line in num_of_lines:
        file.readline()
        list_of_nums.append(file.tell()-previous)
        previous = file.tell()
print(list_of_nums)