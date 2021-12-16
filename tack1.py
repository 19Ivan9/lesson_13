class Animal:
    def talk(self):
        return 'hallo'


class Dog(Animal):
    def talk(self):
        return 'woof'


class Cat(Animal):
    def talk(self):
        return 'meow'


def sey_hallo(animal):
    print(animal.talk())
