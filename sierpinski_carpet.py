from pygame import *
from random import *

white=(255,255,255)
black=(0,0,0)
colors = [(255,0,0),(0,128,255),(255,128,0),(255,0,128),(128,255,0),(128,0,255),(0,255,0),(0,0,255),(204,153,77),(204,77,204),(153,255,0)]

		
def carpet(x,y,a,n):
	draw.rect(window, (randint(0,255),randint(0,255),randint(0,255)),Rect(x-0.5*a,y-0.5*a,a,a))
	if n>0:
		carpet(x,y+a,a/3,n-1)
		carpet(x,y-a,a/3,n-1)
		carpet(x+a,y,a/3,n-1)
		carpet(x-a,y,a/3,n-1)
		carpet(x-a,y-a,a/3,n-1)
		carpet(x-a,y+a,a/3,n-1)
		carpet(x+a,y+a,a/3,n-1)
		carpet(x+a,y-a,a/3,n-1)
		
		
		

init()
window=display.set_mode((700,700))
clock = time.Clock()

end = False 
i=0
while not end:
	for z in event.get():
		if z.type ==QUIT:
			end=True
	
	window.fill(black)

	carpet(350,350,81*3,4)
	
	'''tosave = Surface( (700,700) )
	tosave.blit(window,(0,0),(0,0,700,700))
	image.save(tosave,"image"+str(i)+".png")
	i=i+1
	'''
	clock.tick(2)
	display.flip()