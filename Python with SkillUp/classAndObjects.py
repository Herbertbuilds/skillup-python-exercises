class person:
    def __init__(self, n ,g, a):
        self.name = n
        self.gender = g
        self.age = a
    
    def talk(self):
        print("Hello, my name is", self.name)

    def vote(self):
        if self.age >= 18:
            print(self.name, "is eligible to vote.")
        else:
            print(self.name, "is not eligible to vote.")


obj1 = person("Herbert","Male", 19)
obj2 = person("Maggy","Female", 20)
obj1.talk()
obj2.vote()
              