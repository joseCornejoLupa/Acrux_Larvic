import pygame

pygame.init()

j = pygame.joystick.Joystick(0)

j.init()
print 'Initialized Joystick : %s' % j.get_name()

def get():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	it = 0 #iterator
    pygame.event.pump()
    #Read input from the two joysticks    
    for i in range(0, j.get_numaxes()):
        #print it
        out[it] = j.get_axis(i)
        it+=1
    #Read input from buttons
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    return out
