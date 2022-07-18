class recipe:
    prop = True


recipe.cookingtime = 30

cookie = recipe()
print(cookie.prop)
print(cookie.cookingtime)
print(recipe.prop)
print('-'*50)


class animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def speak(self):
        print(f'hi my name is {self.name} and im a {self.type}')


dog = animal('fido', 'dog')
cat = animal('tom', 'cat')

print(dog.name)
dog.speak()
cat.speak()
print('-'*50)

# inheritance
class bird():
    def __init__(self) -> None:
        print('bird is initialized')
        self.color = 'grey'
        
    def flight(self):
        print('most birds can fly, but some cant')
        

class sparrow(bird):
    def __init__(self) -> None:
        super().__init__()
        self.color = 'reddish brown'
        print('sparrow is ready for flight')
        
    def flight(self):
        print('sparrow can take off')
        
henry = sparrow()
print(henry.color)
henry.flight()

class emu(bird):
    def __init__(self) -> None:
        super().__init__()
        print('emu is ready for takeoff')
    
    def flight(self):
        print('emu is too big and bones too heavy to fly')
        
luz = emu()
print(luz.color)
luz.flight()

