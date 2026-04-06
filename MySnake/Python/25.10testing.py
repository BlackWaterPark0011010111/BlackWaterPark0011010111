# from pprint import pprint 

# given string
l="GFA" 
# p =['1','2','3']
 
# using dictionary comprehension
dic = {
    x: {y: x + y for y in l} for x in l
}

print(dic) # output: {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}, 
# output prediction : {'G': {'G1': '2G', '2': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}, 
# output prediction Jeremiah : {'G': {'1': 'G1', 'F': 'F2'}, 'F': {'G': 'F1', '2': '22'}, 



# # Example for explaining 
# a = [x for x in l ]
# b = [y for y in l]
# print(a,b)# output ['G', 'F', 'G'] ['G', 'F', 'G']
   



 
# print(dic)

# output: {'G': {'G': 'GG', 'F': 'GF'}, 'F': {'G': 'FG', 'F': 'FF'}}

