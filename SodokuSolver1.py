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
        if it returns, true, return true
        if it returns falce, undo all changes made
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
    global board #convert every line of text into a list
    for idx,line in enumerate(board):
    #gives the index of the current line as well as contents
        board[idx] = list(line) 
        #Converts every character into an actual array item
        
main()