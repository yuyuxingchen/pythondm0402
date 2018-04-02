# /usr/bin/env python
# coding=utf-8


class Fa(object):
    def gen(self, line):
        for i in range(1,line+1):
            for j in range(1,i+1):
                print('%d*%d=%d  ' % (j,i,j*i),end="")
            print(end='\n')

if __name__ == '__main__':
    fa = Fa()
    fa.gen(9)


