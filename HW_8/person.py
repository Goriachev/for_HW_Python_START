class Person:
  def __init__(self,name,surname,middle,number):
    self.name = name  
    self.surname = surname
    self.middle = middle
    self.number = number

  def toConsole(self):
    print(self.name,self.surname,self.middle,self.number)

  def __str__(self):
        return f'{self.name} {self.surname} {self.middle} {self.number}'