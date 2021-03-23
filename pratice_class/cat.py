# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_demo.pratice_class.animal import Animal


class Cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = 'short_hair'

    def catch(self):
        print(f"{self.name}会捉老鼠")

    def shout(self):
        print(f"{self.name}喵喵叫")


if __name__ == '__main__':
    cat_1 = Cat('tom', 'red', 4, 'male')
    print(cat_1.hair)
    cat_1.catch()
    cat_1.shout()
    cat_1.run()
