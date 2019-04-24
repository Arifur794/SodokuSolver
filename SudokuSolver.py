import copy
#git push 1
#recursive brute-force approach

#Project Architecture:

''' 
board setup with an array of strings

board =[ "6..874.1.", 
         "..9.36...",
         "...19.8..",
         "7946.....",
         "..1.894..",
         "...41..69",
         ".7..5..9.",
         ".539.76..",
         "9.2.61.47"   ]

dots representing open squares


Strategy:

proc Solve:
    fill in all the "obvious cells until we run out"
    if the puzzle is solved, return true
    if there is a contradiction, return false


    #Landing here means we start guessing
    Find the first empty cell
    possibilities < get all possibilities at empty cell

    for each possibility in possibilities:
        fill in the possibility at the cell
        recursively run Solve()
        if it returns, True, return True
        if it returns Fasce, undo all changes made
    return false

'''

board =[ 
        "6..874.1.", 
         "..9.36...",
         "...19.8..",
         "7946.....",
         "..1.894..",
         "...41..69",
         ".7..5..9.",
         ".539.76..",
         "9.2.61.47"   ]



def main():
    global board #convert every line of text into a list since python strings are immutable
   
    for idx,line in enumerate(board):
    #gives the index of the current line as well as contents
        board[idx] = list(line) 
        #Converts every character into an actual array item
        
    solve()
    printBoard()



def solve():
    global board
    
    try:
        fillAllObvious()
    except:  
        return False  
    if isComplete():
        return True


    i,j = 0,0
    for rowIdx,row in enumerate(board):
        for colIdx,col in enumerate(row):
            if col == ".":
                i,j = rowIdx, colIdx

    possibilites = getPossibilities(i,j)
    for value in possibilites:
        snapshot = copy.deepcopy(board)
        
        board[i][j] = value
        result = solve()
        if result == True:
            return True
        else:
            board = copy.deepcopy(snapshot)

    return False       
    
    
def fillAllObvious():
    global board             #nested for loop gives different values of i and j we will use this to check each cell   
    
    while True:
        somethingChanged = False
        for i in range(0,9):
            for j in range(0,9):
                possibilites = getPossibilities(i,j) #func checks possibilites in cell with coordinates then return the items back
                if possibilites == False:
                    continue
                if len(possibilites) == 0:
                    raise RuntimeError("NO moves left")
                if len(possibilites) == 1:
                    board[i][j] = possibilites[0]
                    somethingChanged = True

        if somethingChanged == False:
            return        



def getPossibilities(i,j):
    global board
    if board[i][j] != ".":
        return False

                                                      #using {} to create a set
    possibilites = {str(n) for n in range(1,10)}  #using conveinient python comprehension 
        
    for val in board[i]:
        possibilites -= set(val)  #rows

    for idx in range(0,9):
        possibilites -= set( board[idx][j] ) #columns


    iStart = (i // 3) * 3
    jStart = (j // 3) * 3
 
    subboard = board[iStart:iStart+3]
    for idx,row in enumerate(subboard):
        subboard[idx] = row[jStart:jStart+3]

    for row in subboard:
        for col in row:
            possibilites -= set(col)
        
    return list(possibilites)


#Clean print function
def printBoard():
    global board
    for row in board:
        for col in row:
            print(col, end = "")
        print("")


def isComplete():
    for row in board:
        for col in row:
           if (col == "."):
                return False 

    return True
              
main()
        #print(list(line))
        #So printing this returns
        
''' 
    ['6', '.', '.', '8', '7', '4', '.', '1', '.']
    ['.', '.', '9', '.', '3', '6', '.', '.', '.']
    ['.', '.', '.', '1', '9', '.', '8', '.', '.']
    ['7', '9', '4', '6', '.', '.', '.', '.', '.']
    ['.', '.', '1', '.', '8', '9', '4', '.', '.']
    ['.', '.', '.', '4', '1', '.', '.', '6', '9']
    ['.', '7', '.', '.', '5', '.', '.', '9', '.']
    ['.', '5', '3', '9', '.', '7', '6', '.', '.']
    ['9', '.', '2', '.', '6', '1', '.', '4', '7']

    We now have lists, allowing us to modify contents
    Main Idea: Convert List of Strings into a Lists of Lists
'''
       
