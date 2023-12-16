
# def area_of_cylinder(radius, height):
#     pi = 3.14
#     base_area = 2 * pi * radius ** 2
#     lateral_area = 2 * pi * radius * height
#     total_area = base_area + lateral_area
#     return total_area
# radius = float(input('Enter radius: '))
# height = float(input('Enter height: '))
# result = area_of_cylinder(radius, height)
# print("Cylinder area:", result)

# double = lambda x: x*2
# print(double(12345678900987654321132435465768798097867564534231))
#
# def double_function(x):
#     return x * 2
# result = double_function(12345678900987654321132435465768798097867564534231)
# print(result)


# from functools import reduce
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# summa = reduce((lambda x, y: x + y), my_list)
# print(summa)
# new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# new_list = list(map(lambda x: x*2 , my_list))
# print(new_list)


# tables = [lambda x = i: x*10 for i in range(1, 101)]
# for table in tables:
#     print(table())

# class Person:
#     def say_age(self, age):
#         print(f"My age is: {age}!")
# Tim = Person()
# Tim.say_age(13)


# class Person:
#     def say(self, message):
#         print(message)
#     def say_hello(self):
#         self.say("Hello work")  # обращаемся к выше определенному методу say
# # tom = Person()
# # tom.say_hello()  # Hello work
#
#
#     def __init__(self):
#
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
# tom = Person("Tom")
# print(tom.name)
# print(tom.age)
# tom.age = 37
# print(tom.age)
# tom.company = "Microsoft"
# print(tom.company)  # Microsoft
#
#
# class Person:
#
#     def __init__(self, name):
#         self.name = name  # имя человека
#         self.age = 25  # возраст человека
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom")
# tom.display_info()  # Name: Tom  Age: 25

#
# class Person:
#
#     def __init__(self, name, age, magical):
#         self.name = name  # имя человека
#         self.age = age  # возраст человека
#         self.magic = magical
#
#
# tom = Person("Tom", 12, "air")
#
# print(tom.name)  # Tom
# print(tom.age)  # 1
# print(tom.magic)


class Calculator:
    def operate(self, x, y, operation):
        try:
            result = self._perform_operation(x, y, operation)
            print(f"{x} {operation} {y} = {result}")
            return result
        except (ValueError, ZeroDivisionError):
            print("Error: Invalid input or division by zero")
            return None

    def add(self, x, y):
        return self.operate(x, y, '+')

    def subtract(self, x, y):
        return self.operate(x, y, '-')

    def multiply(self, x, y):
        return self.operate(x, y, '*')

    def divide(self, x, y):
        return self.operate(x, y, '/')

    def _perform_operation(self, x, y, operation):
        if operation == '+':
            return x + y
        elif operation == '-':
            return x - y
        elif operation == '*':
            return x * y
        elif operation == '/':
            return x / y if y != 0 else None
        else:
            raise ValueError("Invalid operation")

    def calculate_area(self, shape):
        try:
            if shape == "1":
                base, height = map(float, input("Enter base and height separated by a space: ").split())
                area = 0.5 * base * height
                print(f"Area of the triangle: {area}")
            elif shape == "2":
                side = float(input("Enter the side length: "))
                area = side ** 2
                print(f"Area of the square: {area}")
            elif shape == "3":
                radius = float(input("Enter the radius: "))
                area = 3.14159 * radius ** 2
                print(f"Area of the circle: {area}")
            else:
                print("Invalid choice. Supported choices: 1, 2, 3.")
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")


def main():
    calculator = Calculator()

    print("Choose a calculator:")
    print("1. Regular Calculator")
    print("2. Area Calculator")

    calculator_choice = input("Enter your choice (1 or 2): ")

    if calculator_choice == "1":
        try:
            x, y = map(float, input("Enter two numbers separated by a space: ").split())
            operation_choice = input("Choose an operation (+, -, *, /): ")

            if operation_choice in ['+', '-', '*', '/']:
                calculator.operate(x, y, operation_choice)
            else:
                print("Invalid operation. Supported operations: +, -, *, /.")
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
    elif calculator_choice == "2":
        print("Choose a shape for area calculation:")
        print("1. Triangle")
        print("2. Square")
        print("3. Circle")

        shape_choice = input("Enter your choice (1, 2, or 3): ")
        calculator.calculate_area(shape_choice)
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
