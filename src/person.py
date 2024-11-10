class Person:
    # Constructor untuk inisialisasi atribut
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method untuk menyapa
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    # Method untuk memperbarui usia
    def set_age(self, new_age):
        self.age = new_age
        print(f"{self.name}'s age has been updated to {self.age}.")

    # Method untuk mendapatkan usia
    def get_age(self):
        return self.age
