class Animal:
    # name = "jerry"
    # color = "white"
    # age = 10
    # sex = "male"
    def __init__(self,name):
        self.name = name
        self.color = "white"
        self.age = 10
        self.sex = "male"
    def run(self):
        print(f"{self.name}会跑")
    def speak(self):
        print(f"{self.name}会叫")
if __name__ == '__main__':
    animal = Animal("Jerry")
    animal.run()