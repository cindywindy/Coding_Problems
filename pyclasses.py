class User:
    pass #classes need at least one line. pass is a line that does nothing.

user1 = User() #"constructor" to initiate instance of object
user1.first_name="Karlie" #classes can be given fields, even if not declared in class
print(user1.first_name)

#methods, initialization, help text
import datetime 

class Person:
    """if you use help(classname), you will see this DocString"""
    #the initialization method called for new object
    #once you say it needs variables, it will throw an error if you don't give it the right amount
    #init needs two _ at beginning and end
    def __init__(self, full_name, birthday):
        #self. is needed to attach variable to object
        self.name = full_name
        self.birthday = birthday #yyyymmdd
        #Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
        """Returns age in years"""
        today = datetime.date(2021, 4, 6)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob). days
        age_in_years = age_in_days / 365 #excluding leap years
        return int(age_in_years)


person1 = Person("Sarah Lopez", "19990811")
print(person1.name, person1.first_name, person1.birthday)
print(person1.age()) #no need to type self in the parameters)