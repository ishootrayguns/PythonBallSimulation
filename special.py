from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2
from random import randint
from blackhole import Black_Hole

#class starts off as a small ball and increases size and prey is eaten
#it starts to change into different colors and will occasionally disspear
#once it has reached a certain size it will stop and spawn another special and a black hole
class Special(Mobile_Simulton):
    radius = 2
    def __init__(self,x,y,speed = 6):
        Mobile_Simulton.__init__(self, x, y, (self.radius*2), (self.radius*2), 0, speed)
        self.randomize_angle()
        self.counter = 50
        
    def update(self,model):
        if self.radius >= 9:
            x,y = self.get_location()
            self.counter-= 1
            self._speed = 0
            self._angle = 0
            if self.counter == 0:
                model.remove(self)
                model.add(Black_Hole(x,y))
                model.add(Special(x,y)) 
                               
        for sim in model.find(lambda s: isinstance(s,Prey) and self.contains(s.get_location()) or isinstance(s,Pulsator) and self.contains(s.get_location())):
            model.remove(sim)
            if self.radius <= 8.5:
                self.set_dimension(self._width+1, self._height+1)
                self.radius += .5
        target = None
        if target == None:
            target_dict = {}
            for s in model.find(lambda s: isinstance(s,Prey)):
                if self.distance((s._x,s._y)) < 200:
                    target_dict[self.distance((s._x,s._y))] = s
            if len(target_dict) > 0:
                target = target_dict[min(target_dict)]
        if target != None:
            x = (target._x - self._x)
            y = (target._y - self._y)
            self._angle = atan2(y,x)
            if self.contains(target.get_location()):
                model.remove(target)
                target = None
        self.move()
    def display(self,canvas):
        if self.radius <= 5:
            canvas.create_oval(self._x-self.radius, 
                               self._y-self.radius,
                               self._x+self.radius,
                               self._y+self.radius,
                               fill='yellow')
        elif self.radius == 6 :
            x = randint(1,10)
            if x <=5:
                color = 'purple'
            else:
                color = 'white'
            canvas.create_oval(self._x-self.radius, 
                               self._y-self.radius,
                               self._x+self.radius,
                               self._y+self.radius,
                               fill=color)
        elif self.radius <= 7:
            canvas.create_oval(self._x-self.radius, 
                               self._y-self.radius,
                               self._x+self.radius,
                               self._y+self.radius,
                               fill='orange')
        elif self.radius >= 8:
            x = randint(1,10)
            if x <=5:
                color = '#800000'
            else:
                color = '#666699'
            canvas.create_oval(self._x-self.radius, 
                               self._y-self.radius,
                               self._x+self.radius,
                               self._y+self.radius,
                               fill=color)
            
        

