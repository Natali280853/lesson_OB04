#Принцип разделения интерфейсов (ISP, Interface Segregation Principle)


class Light():
    def turn_on_light(self):
        print("Свет включен")


class Food():
    def heat_food(self):
        print("Еда разогревается")


class Music():
    def turn_on_music(self):
        print("Включаю ваш плейлист")

        