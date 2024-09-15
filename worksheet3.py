def diff_from_17(num):
    """Finds the difference between the given number and 17.

    Args:
        num: The number to be compared.

    Returns:
        The modified difference.
    """
    diff = num - 17
    if num > 17:
        diff = diff * 2
    return diff


result = diff_from_17(20)
print(result)


def within_target_range(value):
    """Checks if the number is in the range of 100 to 1000 or exactly 2000.

    Args:
        value: The number to test.

    Returns:
        True if within range, False otherwise.
    """
    return 100 <= value <= 1000 or value == 2000


result = within_target_range(500)
print(result)


def reverse_text(text):
    """Returns the reverse of the input string.

    Args:
        text: The string to be reversed.

    Returns:
        The reversed string.
    """
    return text[::-1]


result = reverse_text("hello")
print(result)


def letter_case_count(text):
    """Counts the upper and lower case letters in a string.

    Args:
        text: The string to be checked.

    Returns:
        A tuple with the count of uppercase and lowercase letters.
    """
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower


result = letter_case_count("Hello, World!")
print(result)


def unique_elements(seq):
    """Removes duplicates from the provided list.

    Args:
        seq: The list to be processed.

    Returns:
        A list with unique elements.
    """
    return list(set(seq))


result = unique_elements([1, 2, 3, 2, 4, 1])
print(result)


def print_evens(nums):
    """Prints the even numbers from a list.

    Args:
        nums: The list of numbers.
    """
    for n in nums:
        if n % 2 == 0:
            print(n)


print_evens([1, 2, 3, 4, 5, 6, 7, 8, 9])


def wrapper_function():
    def inner():
        print("Executing inner function.")
    inner()


wrapper_function()


def student_info(name, age, level):
    """Displays student details.

    Args:
        name: Student's name.
        age: Student's age.
        level: Student's grade level.
    """
    print(f"Student Name: {name}")
    print(f"Student Age: {age}")
    print(f"Grade: {level}")


student_info("Emma", 18, "10th")


class Pupil:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name

    def show_info(self):
        print(f"ID: {self.id_num}")
        print(f"Name: {self.name}")
        print(f"Class: {self.grade}")


pupil1 = Pupil(123, "Liam Smith")
pupil1.grade = "10th"
pupil1.show_info()


class Pupil:
    def __init__(self, id_number, student_name):
        self.id_number = id_number
        self.student_name = student_name


pupil1 = Pupil(123, "Olivia")
pupil2 = Pupil(456, "Noah")

print(f"Pupil 1: ID={pupil1.id_number}, Name={pupil1.student_name}")
print(f"Pupil 2: ID={pupil2.id_number}, Name={pupil2.student_name}")


import math

class Sphere:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * (self.r ** 2)

    def get_circumference(self):
        return 2 * math.pi * self.r


sphere = Sphere(5)
print(f"Area: {sphere.get_area()}")
print(f"Circumference: {sphere.get_circumference()}")


class TextHandler:
    def input_text(self):
        self.text = input("Type a string: ")

    def display_uppercase(self):
        print(self.text.upper())


handler = TextHandler()
handler.input_text()
handler.display_uppercase()
