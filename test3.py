# Принцип подстановки Барбары Лисков (LSP, Liskov substitution Principle)

class Bird():
    def fly(self):
        print("эта птица летает")


class Duck(Bird):
    def fly(self):
        print("эта утка детает быстро")


def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()

fly_in_the_sky(b)
fly_in_the_sky(d)
