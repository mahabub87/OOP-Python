class SimpleCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def sub(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def multiply(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def divide(self):
        if self.num2 != 0:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"
        else:
            return "Error: Division by zero is not allowed."

    def modulo(self):
        return f"{self.num1} % {self.num2} = {self.num1 % self.num2}"

    def area_triangle(self):
        return f"The area of the triangle is = {0.5 * self.num1 * self.num2}"

    def cm_to_inches(self):
        return f"{self.num1} cm to inches is = {self.num1 / 2.54}\n{self.num2} cm to inches is = {self.num2 / 2.54}"

    def inches_to_cm(self):
        return f"{self.num1} inches to cm is = {self.num1 * 2.54}\n{self.num2} inches to cm is = {self.num2 * 2.54}"


def menu():
    options = """
    Please select one of the following: 
        =======================================
        + for addition
        - for subtraction 
        * for multiplication 
        / for division
        % for modulus
        tr to find the area of a triangle
        in to convert cm to inches 
        cm to convert inches to cm 
        0 to exit
        ========================================
    """
    print(options)


def main():
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    calc = SimpleCalculator(num1, num2)

    while True:
        menu()
        user_input = input("Enter operator: ")

        if user_input == "+":
            print(calc.add())
        elif user_input == "-":
            print(calc.sub())
        elif user_input == "*":
            print(calc.multiply())
        elif user_input == "/":
            print(calc.divide())
        elif user_input == "%":
            print(calc.modulo())
        elif user_input == "tr":
            print(calc.area_triangle())
        elif user_input == "cm":
            print(calc.cm_to_inches())
        elif user_input == "in":
            print(calc.inches_to_cm())
        elif user_input == "0":
            print("Goodbye! See you again soon!")
            break
        else:
            print("You have not typed in a valid operator, please run the program again.")


# Running the calculator
if __name__ == "__main__":
    main()
