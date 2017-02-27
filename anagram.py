def build_dict():
    # Load in word file and sort each line.
    alpha = {}
    f = open('words.txt', "r")
    for line in f.readlines():
        line = line.strip()
        key = sorted_line(line)

        # Add each line to a dictionary based on its sorted key.
        if key in alpha:
            v = alpha.get(key) + "," + line
            alpha[key] = v
        else:
            alpha[key] = line
    return alpha

def sorted_line(line):
    # Sort the chars in this line and return a string.
    sortedlist = sorted(line)
    sortedtuple = tuple(sortedlist)
    return sortedtuple

def anagram(alpha):
   
   
   for key in alpha:
       values = (alpha[key])
       newValues = tuple(values)
       print values + '\n'
     
     
dictionary = build_dict()   
anagram(dictionary)