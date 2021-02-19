# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, (Black_Hole.radius*2), (Black_Hole.radius*2))
        
    def update(self,model):
        for sim in model.find(lambda s: isinstance(s,Prey) and self.contains(s.get_location())):
            model.remove(sim)
    
    def contains(self,xy):
        return self.distance(xy) <= (self._width/2)
        
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius, 
                           self._y-self.radius,
                           self._x+self.radius,
                           self._y+self.radius,
                           fill='BLACK')