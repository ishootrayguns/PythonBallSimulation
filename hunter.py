# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    radius = 10
    def __init__(self,x,y,speed=5):
        self.counter_constant = 30
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self, x, y, (Hunter.radius*2), (Hunter.radius*2), 0, speed)
        self.randomize_angle()
        
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
    

