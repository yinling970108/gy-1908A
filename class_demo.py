class ClassDemo():
    def bbb(self):
        print('我最漂亮')


    def ddd(self):
        print('我最好看')
        self.bbb()

if __name__ == '__main__':
    h = ClassDemo()
    h.bbb()
    h.ddd()