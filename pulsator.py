# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole
from turtledemo.nim import COLOR
from simulton import Simulton
from prey import Prey


class Pulsator(Black_Hole):
    radius = 10
    def __init__(self,x,y):
        self.counter_constant = 30
        Simulton.__init__(self, x, y, (Pulsator.radius*2), (Pulsator.radius*2))
        
    def update(self,model):
        self.counter_constant -= 1
        if self.radius == 0:
            model.remove(self)
        if self.counter_constant == 0:
            self.reset()
            self.set_dimension(self._width-1, self._height-1)
            self.radius += -.5
        for sim in model.find(lambda s: isinstance(s,Prey) and self.contains(s.get_location())):
            model.remove(sim)
            self.set_dimension(self._width+1, self._height+1)
            self.radius += .5
            
    def reset(self):
        self.counter_constant = 30