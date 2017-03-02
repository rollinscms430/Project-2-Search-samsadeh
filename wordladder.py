#Word Ladder
#Sam Sadeh

def ladder(start_word, end_word):
    
    # Open file
    file = open('words.txt')
    
    # This build the dictionary with keys and values
    word_dict = {}
    for word in file:
        if len(word) == len(start_word) + 1:
            # Removes whitespace
            word = word.strip()
            
            # determines length of start size to determine similarity with word 
            startsize = len(start_word)
            word_dict[word[:startsize]] = start_word
    
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    queue = [start_word]

    # Breadth first search approach
    
    while len(queue):
        curr_word = queue[0]
        queue.pop(0)
        
        if curr_word == end_word:
            return word_dict[curr_word]
            
        for i in range(len(start_word)):
            for letter in alpha:  
                if curr_word[i] != letter:              
                    nxt = list(curr_word)            
                    nxt[i] = letter              
                    new_word = str(''.join(nxt))
                    if new_word in word_dict and word_dict[new_word] == start_word:
                        queue.append(new_word)
                        word_dict[new_word] = word_dict[curr_word] + ' ' + new_word

# Main
if __name__ == '__main__':
    print ladder('snakes', 'brains')