# Import necessary modules and classes
from operations_manager import OperationsManager
from utility import input_is_valid
from Employee import Employee


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        print('Enter employee data')
        name = input("Enter employee name: ")
        age = input_is_valid("Enter employee age: ")
        salary = input_is_valid("Enter employee salary: ")
        self.employees.append(Employee(name, age, salary))

    def list_employees(self):
        if not self.employees:
            print("\nEmployee list is empty!")
        else:
            for emp in self.employees:
                print(emp)

    def delete_employees_by_age_range(self, age_from, age_to):
        for emp in self.employees[:]:  # Use a slice copy to avoid modifying the list while iterating
            if age_from <= emp.age <= age_to:
                print(f"\tDeleting employee {emp.name}")
                self.employees.remove(emp)

    def find_employee_by_name(self, name):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None

    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print('Error: No employee found with that name.')
        else:
            emp.salary = salary
            print(f"Updated {emp.name}'s salary to {salary}")


class FrontendManager:
    def __init__(self):
        self.employees_manager = EmployeesManager()

    def print_menu(self):
        print("\nProgram Options:")
        options = [
            '1) Add a new employee',
            '2) List all employees',
            '3) Delete employees by age range',
            '4) Update employee salary by name',
            '5) End the program'
        ]
        print('\n'.join(options))
        msg = f'Enter your choice (1 to {len(options)}): '
        return input_is_valid(msg, 1, len(options))

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.employees_manager.add_employee()
            elif choice == 2:
                self.employees_manager.list_employees()
            elif choice == 3:
                age_from = input_is_valid("Enter age from: ")
                age_to = input_is_valid("Enter age to: ")
                self.employees_manager.delete_employees_by_age_range(age_from, age_to)
            elif choice == 4:
                name = input("Enter employee name: ")
                salary = input_is_valid("Enter new salary: ")
                self.employees_manager.update_salary_by_name(name, salary)
            else:
                print("Exiting the program.")
                break


def input_is_valid(msg, start=None, end=None):
    while True:
        inp = input(msg)
        if not inp.isdigit():
            print("Invalid input. Please enter a number.")
        elif start is not None and end is not None and not (start <= int(inp) <= end):
            print(f"Invalid range. Please enter a number between {start} and {end}.")
        else:
            return int(inp)


if __name__ == '__main__':
    app = FrontendManager()
    app.run()
