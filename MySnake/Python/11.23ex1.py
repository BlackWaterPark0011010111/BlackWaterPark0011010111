txt = """ i dont kjnjuywetgoijiohuv k kmnkniw evw ejiuhwferkfc
pijiuhfvkmnloihkluhlfgv
;kiudfgvkjnkjnhiuefv
kjnher
kjed]] hbjhblh jfh jfjbg dkj """

print("Text: \n", txt)
n = 0
to_find = input("What shoud be found?: ")
while n < len(txt):
    if to_find ==txt[n]:
        print("The caracter: ", to_find, "Found at index", n)
    n+=1
print(txt.find("gh"))