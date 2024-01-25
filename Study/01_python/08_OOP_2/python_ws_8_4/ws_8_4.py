# 아래 클래스를 수정하시오.
class Dog:
    def bark(self):
        print('멍멍!')


class Cat:
    def __init__(self, word):
        print(f'{word} !')

    def meow(self):
        pass


class Pet(Dog, Cat):

    def __init__(self, word):
        super().__init__(word)
        print(word)

    def play(self):
        print('애완동물과 놀기')

    def make_sound(self):
        pass



pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark() #멍멍
pet1.meow() #
pet1.play()
