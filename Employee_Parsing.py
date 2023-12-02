class Employee:

    def __init__(self, _firstname, _lastname, _salary):
        self.firstname = _firstname
        self.lastname = _lastname
        self.salary = _salary

    @staticmethod
    def from_string(_str):
        _firstname, _lastname, _salary = _str.split('-')
        return Employee(_firstname, _lastname, int(_salary))