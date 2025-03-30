import pygame
from random import *
from time import *
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((500,500))
a = (200, 255, 255)
window.fill(a)
BLACK = (0,0,0)
class TextArea():
    def __init__(self,x = 0,y = 0,high = 10,width = 10,color =None):
        self.rect = pygame.Rect(x,y,high,width)
        self.fill_color = color
    def color1(self,new_color):
        self.fill_color = new_color        
    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)
class Label(TextArea):
    def draw(self,x1 = 0,y1 = 0):
        self.fill()
        window.blit(self.image,(self.rect.x + x1,self.rect.y + y1))
    def set_text(self,text, fsize=12, text_color=BLACK):
        self.image = pygame.font.SysFont('Arial', fsize).render(text, True, text_color)
red = (255,0,0)
lightpink = (255, 0, 94)
pink = (255, 0, 183)
purple = (127, 0, 255)
orange= (255, 93, 0)
blue = (0, 132, 255)
yellow = (255, 247, 0)
green = (21, 255, 0)
cardslist = []
cards = 4
x = 70
start_time = time()
cur_time = start_time
timetxt = Label(0,0,50,50,blue)
timetxt.set_text('ВРЕМЯ:',40,BLACK)
timetxt.draw(20,20)
time1 = Label(50,55,50,50,blue)
time1.set_text('0',40,BLACK)
time1.draw(0,0)
points = Label(370,0,50,50,blue)
points.set_text('СЧЁТ:',40,BLACK)
points.draw(20,20)
pointsN = Label(430,55,50,50,blue)
pointsN.set_text('0',40,BLACK)
pointsN.draw(0,0)
for i in range(cards):
    newcrad = Label(x,170,70,100,yellow)
    newcrad.outline(red,10)
    newcrad.set_text('ИГРАТЬ ДОТА',25)
    cardslist.append(newcrad)
    x += 100
zadershka = 0 #в развитии
point = 0
while True:
  if zadershka == 0:
    zadershka = 20
    click = randint(1, cards)
    for i in range(cards):
        cardslist[i].color1(yellow)
        if (i + 1) == click:
            cardslist[i].draw(10, 40)
        else:
            cardslist[i].fill()
  else:
    zadershka -= 1
  for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
          x, y = event.pos
          for i in range(cards):
            if cardslist[i].collidepoint(x,y):
             if i + 1 == click:
                cardslist[i].color1(lightpink)
                point += 1
             else:
                 point -= 1
                 cardslist[i].color1(red)
            cardslist[i].fill()
            pointsN.set_text(str(point),40,BLACK)
            pointsN.draw(0,0)
  new_time = time()
  if new_time - start_time >= 10:
     win = Label(0,0,500,500,red)
     win.set_text('ПУДЖ НЕДОВОЛЕН!',60,BLACK)
     win.draw(110,180)
     break
  if int(new_time) - int(cur_time) == 1:
       time1.set_text(str(int(new_time - start_time)), 40, orange)
       time1.draw(0,0)
       cur_time = new_time
  if point >= 5:
      win = Label(0,0,500,500,green)
      win.set_text('ПУДЖ ДОВОЛЕН!',60,BLACK)
      win.draw(140,180)
      speedrun = Label(100,300,250,250,purple)
      speedrun.set_text('Время прохождения Доты:'+str(int(new_time-start_time)),70,red)
      speedrun.draw(0,0)
      break
  pygame.display.update()
  clock.tick(120)


pygame.display.update()





