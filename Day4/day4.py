import numpy as np

with open('/home/oceane/Documents/Personel/AdventOfCode2024/Day4/data.txt', 'r') as file:
    data = file.read()

    table = [list(line) for line in data.splitlines()]


#Part 1
word_to_search='XMAS'
count_word = 0

     
def search_word(table, word_to_search, i, j, k, dir):
    global count_word
    #i, j are coordinates of the previous letter in the table
    #k is the index of the letter in the word
    #dir is the direction to search in, 0 is up, 1 is up right, 2 is right, 3 is down right, 4 is down, 5 is down left, 6 is left, 7 is up left
    
    #compute the next coordinates according to the direction
    if dir==0:
        j-=1
    elif dir==1:
        i+=1
        j-=1
    elif dir==2:
        i+=1
    elif dir==3:
        i+=1
        j+=1
    elif dir==4:
        j+=1
    elif dir==5:
        i-=1
        j+=1
    elif dir==6:
        i-=1
    elif dir==7:
        i-=1
        j-=1

    #check if the coordinates are valid
    if i<0 or j<0 or i>=len(table) or j>=len(table[i]):
        return 
    #check if the letter is the one we are looking for
    if table[i][j] != word_to_search[k]:
        return 
    #check if we have found the word
    if k==len(word_to_search)-1:
        count_word +=1
        return 
    #recursive call to search the next letter in the same direction
    return search_word(table, word_to_search, i, j, k+1, dir)


#loop over the table to find the first letter of the word
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == word_to_search[0]:
            for n in np.arange(8):
                search_word(table, word_to_search, i, j, 1, n)       

print(count_word)


#Part 2

count_word = 0
word_to_search=['SAM', 'MAS']

def search_word_diag(table, word_to_search, i, j):
    global count_word
    ok = 0
    #select the letter around the starting letter 
    diag_1 = ([i-1, j-1], [i,j], [i+1, j+1])
    diag_2 = ([i-1, j+1], [i,j], [i+1, j-1])    
    #check if coordinates are valid
    for coord in diag_1 + diag_2:
        if coord[0] < 0 or coord[0] >= len(table) or coord[1] < 0 or coord[1] >= len(table[0]):
            return
    #select the letters around the starting letter
    for diag in [diag_1, diag_2]:
        letters = [table[coord[0]][coord[1]] for coord in diag]
        letters = ''.join([table[coord[0]][coord[1]] for coord in diag])
        print(letters)
        #check if the letters are the ones we are looking for
        if letters in word_to_search:
            ok += 1
        # if both diagonals are found, we have found the word
        if ok == 2:
            print('found')
            count_word += 1
            return  
        
#loop over the table to find the first letter of the word
for i in range(len(table)):
    for j in range(len(table[i])):
        if table[i][j] == 'A':
            search_word_diag(table, word_to_search, i, j)       

print(count_word)
