# Output:
# 1.Harry Potter And The Sorcerer's Stone: 1241100000
# 2.Harry Potter And The Deathly Hallows : 652200000
# 3.Harry Potter And The Goblet Of Fire: 645600000


def most_sold(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
    sorted_dictionary = dict(sorted_dictionary)
    for i in range(3):
        print( str(i+1)+'.', str(list(sorted_dictionary.keys())[i])+':',list(sorted_dictionary.values())[i])

books = {
  'Harry Potter And The Sorcerer\'s Stone':    1241100000,
  'Harry Potter And The Chamber Of Secrets':   771300000,
  'Harry Potter And The Prisoner Of Azkaban':  65210000,
  'Harry Potter And The Goblet Of Fire':       645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince':    661300000,
  'Harry Potter And The Deathly Hallows ':     652200000,
}

most_sold(books)


