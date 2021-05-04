# owned: meme generator
# ns, ll
from random import random # do you need this??

size('Letter')
diag = False
h = height()
w = width()

pasta = "I won't try to cover it up. Young Stalin is the hottest man I have seen, in textbook or life. No fictional anime character could amount to the absolute beauty and masculinity in this sexy man. I want my first time to be with Stalin. The way his hair is done. The way his moustache bends down to meet the ends of his lips. His smile. Oh my god. His smile. That small revolutionary smirk. That expression of slight amusement, but also of appreciation. I want science to revive Stalin so that I could have a chance with such perfect sexual arousal. I would do anything. I would starve myself to the simple diet of potatoes if it is able to give me the opportunity of seeing young Stalin give his small smirk to me. To make him happy with me. To have his embrace. That is what I live for."
words = pasta.split(" ")
# print(words)

# latin 1 instead of utf-8?? 


# each box is a part of it

# randomly generate composition, randrow randcol

# maybe: 2x2 political compass


# 1x1 top/bottom text
# 3x3 alignment
# expanding brain/drake (if 2x2)

def getGrid():
    
    # outer box for trimming
    fill(None)
    stroke(0)
    strokeWidth(1)
    rect(0,0,w,h)
    
    # set up grid
    numRows = round(random()*4+1) 
    if numRows == 3: 
        if random() < 0.5:
            numCols = 2 # basic hot line bling before/after 2x2 setup
        else:
            numCols = 3 # for alignment chart
            
    elif numRows == 1:
        numCols = 1 # single macro
    
    else: # 2, 4, 5 rows: 2 columns
        numCols = 2            
    
    if diag == True:
        print(numRows,' rows ',numCols,' cols')
    
    # get modules
    modW = int(w/numCols)
    modH = int(h/numRows)
    
    for x in range (0,w,modW):
        for y in range (0,h,modH):
            fill(None)
            stroke(0)
            strokeWidth(1)
            rect(x,y,modW,modH)
    
    return numRows, numCols, modW, modH
    


# =========== PSEUDO CODE !? ================
# 1-10 h*rny/cursed spectrum
# each option correlates to a certain level/vibe
# image text spatial arrangements.
# building system



def layout():
    rows, cols, modW, modH = getGrid()
    
    # test image to play around with
    ipath = "temp.png"
    i = ImageObject(ipath)
    # temp image: 1084 × 1146
    
    # IMAGE
    i.dotScreen()
    
    # how to scale?
    
    
    # 1x1
    if rows == 1 & cols == 1:
        image(i,(0,0))
    
    # 3x3
    elif rows == 3 & cols == 3:
        for r in range(0,w,modW):
            for c in range(0,h,modH):
                image(i,(r,c))
                
    # 2xn
    else:
        i.lanczosScaleTransform((modW/1084),(modW/modH))
        for x in range(0,rows,1):
            
            # 2x2 before and after 
            if rows == 2 & cols == 2:
                image(i,(0,modH*x))
            
            # 2x3, 2x4, 2x5
            else:
                image(i,(w/2,modH*x))
            


# for t in range(10):
#     layout()
#     newPage()
# saveImage('testLayouts.gif')

layout()


# =============== QUESITONS ===================
# should glitch function be the same and vary based on input type

