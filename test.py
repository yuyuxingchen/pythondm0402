#-*- coding: utf-8 -*-
class Isequal(object):
    def __init__(self,guess,value):
        self.guess = guess
        self.value = value


    def isequal(self):
        if self.value < self.guess:
            print('is too big!')
        elif self.value > self.guess:
            print('is too small!')
        else:
            print('you are right!')

if __name__ == '__main__':
    Isequal(int(2),int(4)).isequal()
