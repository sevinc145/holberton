class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}."

    def add_skill(self, skill):
        self.skills.append(skill)


class Student(Person):
    def __init__(self, firstname, lastname, age, country, city, gender):
        super().__init__(firstname, lastname, age, country, city)
        self.gender = gender

    def person_info(self):
        gender_text = "He" if self.gender == "male" else "She"
        return f"{self.firstname} {self.lastname} is {self.age} years old. {gender_text} lives in {self.city}, {self.country}."


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')

print(s1.person_info())
print(s2.person_info())
