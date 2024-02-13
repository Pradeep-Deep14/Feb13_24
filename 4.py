class OSDevice:
    def printSize(self):
        print('medium')

class SmartTV(OSDevice):
    def printSize(self):
        print('large')

obj=SmartTV()
obj.printSize()