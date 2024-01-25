# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1

class Cat(Animal):
    def __init__(self, word):
        print(f'{word} !')

    def meow(self):
        pass


cat1 = Cat("야옹")
cat1.meow()
