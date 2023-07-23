from typing import Any


class Humanoid(object):
    #class variable, all objects can share this variable
    humanoids = 0
    def __init__(self, age=0):
        self.age = age
        self.name = None
        Humanoid.humanoids +=1
    #safer method of getting variable data out of class
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    #safer method to set values
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname):
        self.name = newname
    #string representationf of class
    def __str__(self):
        return "humanoid: "+str(self.name)+", age: "+str(self.age)

#subclasses of Humanoid
class Elf(Humanoid):
    def __str__(self):
        return "Elf: "+str(self.name)+", age: "+str(self.age)
    def fight(self):
        print(str(self.name)+" use bow")
    
class Dwarf(Humanoid):
    def __str__(self):
        return "Dwarf: "+str(self.name)+", age: "+str(self.age)
    def fight(self):
        print(str(self.name)+" use axe")
        
class Human(Humanoid):
    def __init__(self, age, name=None):
        #use inity from parent class, alternative: Humanoid.__init__(self, age)
        super().__init__(age)
        self.set_name(name)
    def __str__(self):
        return "Human: "+str(self.name)+", age: "+str(self.age)
    def fight(self):
        print(str(self.name)+" use magic spell")
      
x = Humanoid()
print(Elf.humanoids)
e = Elf(200)
print(Elf.humanoids)
h = Human(20, "Mark")
d = Dwarf()
print(Elf.humanoids)
print(x, e, h, d)

e.set_name("Legolas")
d.set_name("Gimil")

e.set_age(2931)
d.set_age(140)

print(e, "\n"+str(d))

e.fight()
d.fight()