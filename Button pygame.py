import pygame
pygame.init()
from gpiozero import LED


window = pygame.display.set_mode ((0, 0),pygame.FULLSCREEN)
window.fill((0,0,255))
led = LED(17)

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 50)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

green_button = button((0, 255, 0), 50, 140, 200, 200, text="ON")
red_button = button((255, 0, 0), 550, 140, 200, 200, text="OFF")
yellow_button = button((255, 255, 0), 10, 10, 100, 100, text="QUIT")

while True:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if green_button.isOver(pos) == True:
                led.on()
            if red_button.isOver(pos) == True:
                led.off()
            if yellow_button.isOver(pos) == True:
                pygame.display.quit()


                
    pygame.display.update()
    green_button.draw(window, (0, 0, 0))
    red_button.draw(window, (0, 0, 0))
    yellow_button.draw(window, (0, 0, 0))
