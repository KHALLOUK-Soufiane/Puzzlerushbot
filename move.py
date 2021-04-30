import os

wPieces = ['wr', 'wq', 'wn', 'wb', 'wk', 'wp']
bPieces = ['br', 'bq', 'bn', 'bb', 'bk', 'bp']
pieces = wPieces #+ bPieces

for i in range(0,2):
    if i == 0:
        for j in [1,3,5]:
                os.rename("board/" + chr(ord('a')+i) + str(j+1) + ".png", 'board/'+bPieces[j]+'lighthighlighted.png')
    elif i == 1:
        for j in [0,2,4]:
                os.rename("board/" + chr(ord('a')+i) + str(j+1) + ".png", 'board/'+bPieces[j]+'lighthighlighted.png')

