"""
# 1. Suma liczb od 1 do podanej liczby np. 150

def sum_numbers():
    n = int(input("Enter your number: "))
    total_sum = 0
    for number in range(1, n + 1):
        total_sum += number
    print(total_sum)

sum_numbers()
"""
"""
# 2. Zliczanie wystąpień danego znaku w ciągu znaków

def count_character_occurrences():
    string = input("Enter your string: ")
    char = input("Enter the character to count: ")
    total_count = 0

    for c in string:
        if c == char:
            total_count += 1

    print(f"The character '{char}' occurs {total_count} times in the string.")

count_character_occurrences()
"""
# 3. Wypisanie indeksów znaków w zdaniu
"""
def count_character_index():
    string = input("Enter your string: ")
    char = input("Enter the character to count: ")
    total_count = 0

    for i in range(len(string)):
        if string[i] == char:
            total_count += 1

    print(f"The character '{char}' occurs {total_count} times in the string.")

count_character_index()

#or

def find_character_indices():
    string = input("Enter your string: ")
    char = input("Enter the character to find: ")
    indices = []

    for index, c in enumerate(string):
        if c == char:
            indices.append(index)

    print(f"The character '{char}' occurs at indices: {indices}")


find_character_indices()
"""
"""
# 4. Wypisanie liczb podzielnych przez daną liczbę

def numbers_divisible_by():
    value = int(input("Enter value: "))
    brave = int(input("Enter value: "))

    if value % brave == 0:
        return print(f"{value} is divisible by {brave} ")
    else:
        return print(f"{value} is not divisible by {brave} ")

numbers_divisible_by()
"""
"""
# 5. Sprawdź czy podany tekst jest palindromem

def verify_text():
    text = input("Enter text: ")
    clear_text = text.replace(" ", "").lower()

    if clear_text == clear_text[::-1]:
        print("Text is palindrom")
    else:
        print("Text is not palindrom")

verify_text()
"""
"""
# 6. Wyświetl zdanie w odwrotnej kolejności

def sequence_reverse():
    text = input("Enter your text: ")
    view = text[::-1]
    print(view)

sequence_reverse()
"""
"""
# 7. Napisz program ktory konwertuje temperaturę z wartości w stopniach celsiusza na stopnie Kelvina

def convert_temp():
    amount_celcjus = float(input("Enter value in Celscjus: "))
    amount_celvin = amount_celcjus + 273.15
    print(amount_celvin)

convert_temp()
"""
"""
# 8. Wyświetl trójkąt z gwiazdek

def triangle():
    score = 7
    char = "*"
    for i in range(1, score + 1):
        print(char * i)

triangle()
# 9. Wyświetl całą choinkę (a nie tylko pół)
def triangle():
    score = 7
    char = "*"
    for i in range(1, score + 1):
        spaces = ' ' * (score - i)
        stars = char * (2 * i - 1)
        print(spaces + stars)

triangle()

"""
"""
# 10. Napisz program, który działa jako prosty kalkulator wykonujący podstawowe operacje matematyczne (+, -, *, /),
# na dwóch liczbach.

class Calculate():
    def __init__(self, first_number: float, second_number: float):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        if self.second_number == 0:
            return "Error: Division by zero"
        return self.first_number / self.second_number

def main():

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    calc = Calculate(first_number, second_number)

    print(f"Addition: {calc.addition()}")
    print(f"Subtraction: {calc.subtraction()}")
    print(f"Multiplication: {calc.multiplication()}")
    print(f"Division: {calc.division()}")


if __name__ == __name__:
    main()

"""
"""
# 11. Napisz program, który zlicza liczbę samogłosek i spółgłosek w danym tekście

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0,
             'A':0, 'E':0, 'I':0, 'O':0, 'U':0}

    for char in text:
        if char in vowels:
            count[char] += 1

    return count

user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)

for vowel in "aeiouAEIOU":
    print(f"The number of '{vowel}' in the given string is: {vowel_count[vowel]}")
"""