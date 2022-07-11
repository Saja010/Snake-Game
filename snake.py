
import pygame,math,random,sys

# CONSTANTS
WIDTH = 640
HEIGHT = 640
PIXELS = 32
SQUARES = int(WIDTH/PIXELS)

# COLORS
BG1 = (156, 210, 54)
BG2 = (147, 203, 57)
RED = (255, 0, 0)
BLUE = (0, 0, 50)
BLACK = (0, 0, 0)


class Background:

	def draw(self, surface):
		surface.fill( BG1 )
		counter = 0
		for row in range(SQUARES):
			for col in range(SQUARES):
				if counter % 2 == 0:
					pygame.draw.rect( surface, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS) )
				if col != SQUARES - 1:
					counter += 1

class Apple:
	def __init__(self):
		self.color=RED
		self.spawn()
	def spawn(self):
		self.posX=random.randrange(0,WIDTH,PIXELS)
		self.posY=random.randrange(0,HEIGHT,PIXELS)	

	def draw(self,surface):
		pygame.draw.rect(surface,self.color,(self.posX,self.posY ,PIXELS,PIXELS))	

class Snake:
	def __init__(self):
		self.color=BLUE
		self.headX=random.randrange(0,WIDTH,PIXELS)
		self.headY=random.randrange(0,WIDTH,PIXELS)
		self.bodys=[]
		self.body_color=50
		self.state="STOP"
		

	def move (self):
		if self.state== "UP":
			self.headY -= PIXELS

		elif self.state== "DOWN":
			self.headY += PIXELS

		elif self.state== "RIGHT":
			self.headX += PIXELS

		elif self.state== "LEFT":
			self.headX -= PIXELS

	def move_body(self):
		if len(self.bodys) > 0:
			for i in range(len(self.bodys)-1, -1, -1):
				if i == 0:
					self.bodys[0].posX = self.headX
					self.bodys[0].posY = self.headY
				else:
					self.bodys[i].posX = self.bodys[i-1].posX
					self.bodys[i].posY = self.bodys[i-1].posY		

	def add_body(self):
		self.body_color+=10
		body=Body((0,0,self.body_color),self.headX,self.headY)
		self.bodys.append(body)



	def draw(self, surface):
		pygame.draw.rect( surface, self.color, (self.headX, self.headY, PIXELS, PIXELS) )
		if len(self.bodys) > 0:
			for body in self.bodys:
				body.draw(surface)

	def die(self):
		self.headX=random.randrange(0,WIDTH,PIXELS)
		self.headY=random.randrange(0,WIDTH,PIXELS)
		self.bodys=[]
		self.body_color=50
		self.state="STOP"# STOP UP DOWN RIGHT LEFT
		

class Body:
	def __init__(self,color ,posX,posY):
		self.color=color
		self.posX=posX
		self.posY=posY

	def draw(self,surface):
		pygame.draw.rect(surface,self.color,(self.posX,self.posY ,PIXELS,PIXELS))		


class Collision:
    def between(self,snake,apple):
        distance=math.sqrt((snake.headX-apple.posX)**2+(snake.headY-apple.posY)**2)
        return distance<PIXELS
    def between_snake_and_walls(self, snake):
					if snake.headX < 0 or snake.headX > WIDTH - PIXELS or snake.headY < 0 or snake.headY > HEIGHT - PIXELS:
						return True
					return False
 


def main():
	pygame.init()
	screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
	pygame.display.set_caption( "SNAKE" )



	# OBJECTS
	background=Background()
	apple=Apple()
	snake=Snake()
	collision=Collision()

	

	# MainLoop
	while True:
		background.draw(screen)
		apple.draw(screen)
		snake.draw(screen)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


			if event.type==pygame.KEYDOWN:

				if event.key==pygame.K_UP:
					snake.state="UP"	

				if event.key==pygame.K_DOWN:
					snake.state="DOWN"

				if event.key==pygame.K_RIGHT:
					snake.state="RIGHT"

				if event.key==pygame.K_LEFT:
					snake.state="LEFT"

				if event.key==pygame.K_UP:
					snake.state="UP"

		if collision.between(snake,apple):
			apple.spawn()
			# incresing the length of the snake 
			snake.add_body()
		
		if collision.between_snake_and_walls(snake):
			snake.die()
			apple.spawn()
			# lose the game 
			
	 





		pygame.time.delay(125)
		snake.move_body()			
		snake.move()									
		pygame.display.update()

main()