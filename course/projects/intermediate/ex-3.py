class InvalidSalaryException(Exception):
    """Raised when the salary is invalid"""

    pass


class Employee:
    min_salary = 1000

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        if salary < 0:
            raise InvalidSalaryException("Salary cannot be negative")
        self.salary = salary

    def __str__(self):
        return f"{self.name} is a {self.position} with a salary of {self.salary}"


class Manager(Employee):
    min_salary = 10000

    def __init__(self, name, position, salary):
        if salary < self.min_salary:
            raise InvalidSalaryException(
                f"Salary cannot be less than {self.min_salary}"
            )
        super().__init__(name, position, salary)

    def hire(self, employee):
        print(f"{self.name} Hiring new employee: {employee}")

    def fire(self, employee):
        print(f"{self.name} Firing employee: {employee}")


class Developer(Employee):
    min_salary = 9000

    def __init__(self, name, position, salary):
        if salary < self.min_salary:
            raise InvalidSalaryException(
                f"Salary cannot be less than {self.min_salary}"
            )
        super().__init__(name, position, salary)

    def code(self):
        print(f"{self.name} is coding")


manager = Manager("John", "Junior Manager", 10000)
developer = Developer("Jane", "Senior Developer", 9000)

manager.hire(developer)

developer.code()

manager.fire(developer)

# developer = Developer("Monke", "Wizard Developer", -1000)

# manager.hire(developer)
# manager.fire(developer)
