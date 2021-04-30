from module import *
#big dickus
while keyboard.is_pressed('s') == False:
    fen = ""
    colorindicator = getPixelColor(1194,152)
    colorToMove = getMoveColor(colorindicator)
    pic = pyautogui.screenshot(region=puzzleRushRegion)
    width, height = pic.size

    if colorToMove == 'w':
        rang = [0,1,2,3,4,5,6,7]
    elif colorToMove == 'b':
        rang = [7,6,5,4,3,2,1,0]

    for i in rang:
        number = 0
        for j in rang:
            croppedSquare = pic.crop(box=(j*width/8, i*height/8, (j*width/8)+(width/8), (i*height/8)+(height/8)))
            if colorToMove == 'w':
                croppedSquare.save('board/'+ chr(ord('a')+j) + str(8-i)+'.png')
            elif colorToMove == 'b':
                croppedSquare.save('board/'+ chr(ord('h')-j) + str(i+1)+'.png')
            hashPiece = imagehash.average_hash(croppedSquare)
            for piece in pieces:
                for l in lightness:
                    for color in colors:
                        hashRef = imagehash.average_hash(Image.open('pieces/'+ piece + l + color + ".png"))
                        hashEmpty = imagehash.average_hash(Image.open('pieces/blank'+ l + color + ".png"))
                        hashRef2 = hashRef
                        if piece=='wk' and l=='light' and color=='':
                            hashRef2 = imagehash.average_hash(Image.open('pieces/wklight2.png'))
                        if hashPiece - hashRef < 2 or hashPiece - hashRef2 < 2:
                            flag = 1
                            if piece[0] == "w":
                                fenPiece = piece[1].upper()
                            elif piece[0] == "b":
                                fenPiece = piece[1].lower()

                            if number != 0:
                                fen = fen + str(number) + fenPiece
                            else:
                                fen = fen + fenPiece
                            number = 0
                            #print('I see ' + fenPiece + ' in ' + chr(ord('a')+j) + str(8-i))
                        elif hashPiece - hashEmpty < 2.5:
                            number +=1
                            flag = 1
                        if flag == 1:
                            break
                    if flag == 1:
                        break
                if flag == 1:
                    break
            
            flag = 0
        if number != 0:
            fen = fen + str(number)+ "/"
        else:
            fen = fen + "/"
    fen = fen[:-1] + " " + colorToMove + " - - 0 1" 
    result = analyze(fen, engine).uci()
    print(result)
    play(result, width, height, puzzleRushRegion, colorToMove)
