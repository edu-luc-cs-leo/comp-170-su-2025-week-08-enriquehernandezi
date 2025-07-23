from Birthday import Birthday

class Person: #defines new class

    def __init__(self, first_name, last_name): #defines person's first and last name
        self.first_name = first_name
        self.last_name = last_name
        self._birthday = None #birthday is private
        self.city = None #can be added later

    def introduce(self):
        print(f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}") #prints introduction person saying their first name and their birthday

    def set_birthday(self, month, day): #creates birthday object, with month and day
        self._birthday = Birthday(month, day)

    def set_city(self, city): #creates person's city
        self.city = city

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __str__(self): #person's full name defined and returned
        return f"[ {self.first_name} {self.last_name}]"

    def say_birthday(self): #defines the actual day and month number of the person's birthday
        day = self._birthday.get_day()
        month = self._birthday.get_month()

        # Determines suffix for lets say if the persons birthday is on the 21 it will say 21st
        if day in [1, 21, 31]: #st suffix including the days 1, 21, and 31
            suffix = "st"
        if day in [2, 22]:
            suffix = "nd"
        if day in [3, 23]:
            suffix = "rd"
        else:
            suffix = "th" #any other number of day not defined above will end with th

        month_names = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]

        return f"{day}{suffix} of {month_names[month - 1]}" #this will return actual birthday like "21st of December"

    def __lt__(self, other): #one person is less than another if their first name is first alphabetically and redefines operator <
        return self.first_name < other.first_name

from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
