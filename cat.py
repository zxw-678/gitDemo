from python_homework.animal import Animal

class Cat(Animal):

    def __init__(self):
        super().__init__("Jerry")
        # print(self.sex)
        self.hair = "short"

    def catch(self):
        print(f"{self.name}会捉老鼠")
    def speak(self):
        print(f"{self.name}喵喵叫")

if __name__ == '__main__':
    cat = Cat()
    cat.catch()
    cat.speak()





