from pyautogui import *
from PIL import Image
import imagehash
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import subprocess
import chess
import chess.engine

flag = 0
fen = ""
fenPiece = ""
puzzleRushRegion = (397,119,600,600)
analysisRegion = (497,119,600,600)
liveGameRegion = (397,169,600,600)
puzzleRegion = (397,119,600,600)
engine = chess.engine.SimpleEngine.popen_uci("stockfish-x64.exe")

wPieces = ['wr', 'wq', 'wn', 'wb', 'wk', 'wp']
bPieces = ['br', 'bq', 'bn', 'bb', 'bk', 'bp']
pieces = wPieces + bPieces
lightness = ["dark", "light"]
colors = ["red", "blue", "highlighted", ""]

def getPixelColor(x,y):
    try:
        colorindicator = pyautogui.pixel(x,y)
    except:
        try:
            colorindicator = pyautogui.pixel(x,y)
        except:
            try:
                colorindicator = pyautogui.pixel(x,y)
            except:
                try:
                    colorindicator = pyautogui.pixel(x,y)
                except:
                    try:
                        colorindicator = pyautogui.pixel(x,y)
                    except:
                        try:
                            colorindicator = pyautogui.pixel(x,y)
                        except:
                            try:
                                colorindicator = pyautogui.pixel(x,y)
                            except:
                                try:
                                    colorindicator = pyautogui.pixel(x,y)
                                except:
                                    colorindicator = pyautogui.pixel(x,y)
    return colorindicator

def getMoveColor(color):
    if color == (49, 46, 43):
        return 'b'
    elif color == (255,255,255):
        return "w"
    
def analyze(fenS, engine):
    print(fenS)
    board = chess.Board(fen=fenS)
    result = engine.play(board, chess.engine.Limit(depth=20))
    return result.move

def Click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def play(move, width, height, screenCoor, colorToMove): 
    if colorToMove == 'w':
        x1 = screenCoor[0] + round((width/8)*(ord(move[0]) - ord('a')) + (width/16))
        y1 = screenCoor[1] + round((height/8)*(8-int(move[1])) + (height/16))
        Click(x1,y1)
        time.sleep(0.1)
        x2 = screenCoor[0] + round((width/8)*(ord(move[2]) - ord('a')) + (width/16))
        y2 = screenCoor[1] + round((height/8)*(8-int(move[3])) + (height/16))
        Click(x2,y2)
    elif colorToMove == 'b':
        x1 = screenCoor[0] + round((width/8)*(ord('h') - ord(move[0])) + (width/16))
        y1 = screenCoor[1] + round((height/8)*(int(move[1])-1) + (height/16))
        Click(x1,y1)
        time.sleep(0.1)
        x2 = screenCoor[0] + round((width/8)*(ord('h') - ord(move[2])) + (width/16))
        y2 = screenCoor[1] + round((height/8)*(int(move[3])-1) + (height/16))
        Click(x2,y2)
    
    if len(move)==5:
        if move[4]=='q':
            click(x2,y2)
        elif move[4]=='n':
            click(x2,y2+(height/8))
        elif move[4]=='r':
            click(x2,y2+2*(height/8))
        elif move[4]=='b':
            click(x2,y2+3*(height/8))
    time.sleep(0.6)