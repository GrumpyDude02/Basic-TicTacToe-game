from random import randrange
import pygame
import sys

pygame.init()
WIDTH=600
HEIGHT=600
bg_color=(13, 161, 146)
line_color=(0, 167, 124)
WHITE=(255,255,255)
GREY=(75,75,75)
x_color=(84, 84, 84)
O_color=(245,245,245)
BLACK=(0,0,0)
clock=pygame.time.Clock()
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
window.fill(bg_color)
font=pygame.font.SysFont("arialblack",40)
textwin = font.render('YOU WON!',True,WHITE)
textlost= font.render('YOU LOST!',True,WHITE)
textdraw = font.render('    TIE!',True,WHITE)
textdiff=font.render("Choose Difficulty",True,WHITE)
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]
textpos=(200,90)
textpos2=(100,90)

class buttons:
    def __init__(self,text,width,height,posx,posy) :
        gui_font=pygame.font.SysFont("arialblack",40)
        self.lrect=pygame.Rect(posx-5,posy-5,width+10,height+10)
        self.rectangle=pygame.Rect(posx,posy,width,height)
        self.color=(0,0,0)
        self.tex_surf=gui_font.render(text,True,(255,255,255))
        self.text_rect=self.tex_surf.get_rect(center=self.rectangle.center)
        self.clicked=False
        
    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.lrect)
        pygame.draw.rect(screen,self.color,self.rectangle)
        screen.blit(self.tex_surf,self.text_rect)
        self.chckclick(screen)
    
    def chckclick(self,screen):
        mouse_pos=pygame.mouse.get_pos()  
        if self.rectangle.collidepoint(mouse_pos):
            self.color=(2, 32, 29)
            if pygame.mouse.get_pressed()[0] and self.clicked==False:
                self.clicked=True
            if pygame.mouse.get_pressed()[0]==False:
                self.clicked=False
        else:
            self.color=(0,0,0)

play=buttons("PLAY",200,90,200,150)
exit=buttons("EXIT",200,90,200,350) 
retry=buttons("RETRY",200,90,50,350)
exit2=buttons("EXIT",200,90,350,350)
hard=buttons("IMPOSSIBLE",300,90,150,400)
easy=buttons("EASY",300,90,150,250)

def draw_lines(window):  
    pygame.draw.line(window,WHITE,(200,0),(200,600),15)
    pygame.draw.line(window,WHITE,(400,0),(400,600),15)
    pygame.draw.line(window,WHITE,(0,200),(600,200),15)
    pygame.draw.line(window,WHITE,(0,400),(600,400),15)

def setmark(row,col):
    pygame.draw.circle(window,WHITE,(int(row*200+100),int(col*200+100)),60,15)
                            
def checkGame(board):
    c=9
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=0:
            if board[i][0]==1:
                return -10
            if board[i][0]==2:
                return 10
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=0:
            if board[0][i]==1:
                return -10
            if board[0][i]==2:
                return 10
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=0:
        if board[0][0]==1:
            return -10
        if board[0][0]==2:
            return 10
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0:
        if board[0][2]==1:
            return -10
        if board[0][2]==2:
            return 10
    for i in range(3):
        for j in range(3):
            if board[i][j]!=0:
                c=c-1
    if(c==0):
        return 0
    else:
        return 30
    
def drawwinninglines(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=0:
            pygame.draw.line(window,BLACK,(i*200+100,15),(i*200+100,HEIGHT-15),15)
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=0:
            pygame.draw.line(window,BLACK,(15,i*200+100),( WIDTH-15,i*200+100),15)
    if board[0][0]!=0 and board[0][0]==board[1][1]==board[2][2] :
        pygame.draw.line(window,BLACK,(15,15),(WIDTH-15,HEIGHT-15),15) 
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=0:
        pygame.draw.line(window,BLACK,(WIDTH-15,15),(15,HEIGHT-15),15)
          
def drawbot(board):
    for row in range(3):
        for col in range(3):
            pygame.draw.line(window,WHITE,(int(row*200+200-30),int(col*200+30)),(int(row*200+30),int(col*200+200-30)),20)
            pygame.draw.line(window,WHITE,(int(row*200+30),int(col*200+30)),(int(row*200+200-30),int(col*200+200-30)),20)    

def AImove(board,difficulty):
    if difficulty==1:
        bestscore=-1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]==0):
                    board[i][j]=2
                    score=minimax(board,False)
                    board[i][j]=0
                    if(score>bestscore):
                            bestscore=score
                            bestmovex=i
                            bestmovey=j
        
        board[bestmovex][bestmovey]=2
        pygame.draw.line(window,x_color,(int(bestmovex*200+200-30),int(bestmovey*200+30)),(int(bestmovex*200+30),int(bestmovey*200+200-30)),20)
        pygame.draw.line(window,x_color,(int(bestmovex*200+30),int(bestmovey*200+30)),(int(bestmovex*200+200-30),int(bestmovey*200+200-30)),20)
    elif difficulty==0:
        while True:
            a=randrange(0,3)
            b=randrange(0,3)
            if board[a][b]==0:
                board[a][b]=2
                pygame.draw.line(window,x_color,(int(a*200+200-30),int(b*200+30)),(int(a*200+30),int(b*200+200-30)),20)
                pygame.draw.line(window,x_color,(int(a*200+30),int(b*200+30)),(int(a*200+200-30),int(b*200+200-30)),20)
                break
            
def minimax(board,IsMax):   
        result=checkGame(board)
        if(result!=30):
            return result
        if(IsMax):
            bestscore=-1000000
            for i in range(3):
                for j in range(3):
                    if(board[i][j]==0):
                        board[i][j]=2
                        point=minimax(board,False)
                        board[i][j]=0
                        if(point> bestscore):
                            bestscore=point
            return bestscore
        else:
            bestscore=1000000
            for i in range(3):
                for j in range(3):
                    if(board[i][j]==0):
                        board[i][j]=1
                        point=minimax(board,True)
                        board[i][j]=0
                        if(point<bestscore):
                            bestscore=point
            return bestscore
  
def resetboard(board):
    for i in range(3):
        for j in range(3):
            board[i][j]=0
    window.fill(bg_color)
    draw_lines(window)
  
def timedelay():
    global delay
    if delay==1 and checkGame(board)!=30 :  
        delay=0
        pygame.time.delay(500)
    
def gamestate(board,game_over,player,diffc):
    global delay
    global difficultysc
    global running
    if checkGame(board)!=30 :
        game_over=True  
        player = True
    if game_over :
        window.fill(bg_color)
        retry.draw(window)
        exit2.draw(window)
        match checkGame(board):
            case 10:
                window.blit(textlost,textpos)
                if retry.clicked:
                    retry.clicked=False
                    game_over=False
                    difficultysc=True
                    running=False
                    delay=1
                if exit2.clicked:
                    sys.exit()
            case 0:
                window.blit(textdraw,textpos)
                if retry.clicked:
                    retry.clicked=False
                    game_over=False
                    difficultysc=True
                    running=False
                    delay=1
                if exit2.clicked:
                    sys.exit()
            case -10:
                window.blit(textwin,textpos)
                if retry.clicked:
                    retry.clicked=False
                    game_over=False
                    difficultysc=True
                    running=False
                    delay=1
                if exit2.clicked:
                    sys.exit()
               
 
           
game_over=False
human=True
window.fill(bg_color)
running=False
delay=1
difficulty=0
mainscreen=True
difficultysc=True

while(True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        if running==False and mainscreen:
            play.draw(window)
            exit.draw(window)
            if exit.clicked:
                sys.exit()
            if play.clicked:
                window.fill(bg_color)
                mainscreen=False
                difficultysc=True
        if mainscreen==False and difficultysc:
            window.fill(bg_color)
            window.blit(textdiff,textpos2)
            easy.draw(window)
            hard.draw(window)
            if easy.clicked:
                difficulty=0
                resetboard(board)
                running=True
                difficultysc=False
                easy.clicked=False
            elif hard.clicked:
                difficulty=1
                resetboard(board)
                running=True
                difficultysc=False
                hard.clicked=False
        elif(running and difficultysc==False):  
            if(human):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_x=event.pos[0]
                    mouse_y=event.pos[1]
                    clicked_row=int(mouse_x // 200)
                    clicked_col=int(mouse_y // 200)
                    if(board[clicked_row][clicked_col]==0 and checkGame(board)==30):
                        board[clicked_row][clicked_col]=1
                        setmark(clicked_row,clicked_col)
                        drawwinninglines(board)
                        if checkGame(board)==30 and human==True:
                            human=not human
            elif checkGame(board)==30 and human==False:
                AImove(board,difficulty)
                drawwinninglines(board)
                human=not human
        pygame.display.flip()
    timedelay()
    gamestate(board,game_over,human,difficulty)
    clock.tick(15)
        
    
            
        
        