# REMOVE
class MyList:
    def __init__(self):
        self.data = []

    def remove(self, value):
        topildi = False

        for i in range(len(self.data)):
            if self.data[i] == value:
                self.data = self.data[:i] + self.data[i+1:]
                topildi = True
                break

        if not topildi:
            print("❌ Element topilmadi")

    def show(self):
        print(self.data)

lst = MyList()

lst.data = [1, 2, 3, 2, 4]

lst.show()       
lst.remove(2)
lst.show()      

lst.remove(5)     
