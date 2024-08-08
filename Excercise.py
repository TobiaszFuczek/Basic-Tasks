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
import random

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
"""
# 12. Napisz program, który obliczy średnią ocenę oraz medianę.

def calculate_graduate(grades):
    total = sum(grades)
    return total

def calculate_average(grades):
    total = calculate_graduate(grades)
    average = total / len(grades)
    return average

def calculate_median(grades):
    sorted_grades = sorted(grades)
    n = len(sorted_grades)
    if n % 2 == 1:
        # Jeśli liczba ocen jest nieparzysta, mediana to środkowa wartość
        median = sorted_grades[n // 2]
    else:
        # Jeśli liczba ocen jest parzysta, mediana to średnia z dwóch środkowych wartości
        mid1 = sorted_grades[n // 2 - 1]
        mid2 = sorted_grades[n // 2]
        median = (mid1 + mid2) / 2
    return median

user_input = input("Enter grades separated by spaces: ")
grades = list(map(float, user_input.split()))

average_grade = calculate_average(grades)
median_grade = calculate_median(grades)

print(f"The average grade is {average_grade}")
print(f"The median grade is {median_grade}")

"""
"""
# 13. Napisz program, który odwróci listę elementów w miejscu, bez tworzenia nowej listy

def return_list():
    user_input = input("Enter value to list: ")
    list_input = user_input.split()
    list_input.reverse()

    print(list_input)
# or

    reverse_list = list_input[::-1]
    print(reverse_list)

return_list()
"""
"""
# 14. Napisz program, który przyjmie listę liczb i zwróci nową listę,
# zawierającą tylko liczby parzyste (lub nieparzyste) z pierwotnej listy


def count_even_number():
    list_input = input("Enter numbers: ")
    list_input = list(map(int, list_input.split()))

    numbers_even = []
    numbers_odd = []

    for i in list_input:
        if i % 2 == 0:
            numbers_even.append(i)
        else:
            numbers_odd.append(i)

    print(f"List of value even is {numbers_even} and list of value odd {numbers_odd}")

count_even_number()

"""
"""
# 15. Napisz program, który obliczy sumę cyfr w danej liczbie całkowitej, na przykład dla liczby 12345 suma będzie wynosiła 15

def sum_of_numbers():
    user_input = int(input("Enter number: "))
    amount = 0
    for digit in str(user_input):
        amount += int(digit)

    print(f"Sum all digit in numbers {user_input} is {amount}")

sum_of_numbers()
"""
"""
# 16. Napisz program, który zliczy ile liczb parzystych znajduje się w zadanym zakresie, na przykład od 1 do 50

def even_numbers_scope(a,b):
    amount = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            amount += 1
    return amount

scope = even_numbers_scope(1,50)
print(f"The number of even numbers between 1 and 50 is {scope}")
"""
"""
# 17. Napisz program, który wyświetli kwadrat o boku 7 z gwiazdek

def view_square():
    side = 7
    for i in range(side):
        if i == 0 or i == side - 1:
            print("*" * side)
        else:
            print("*" + " " * (side - 2) + "*")

view_square()
"""
"""
# 18. Napisz funkcję, która obliczy sumę wszystkich liczb w danej liście.

def sum_of_numbers_in_list():
    user_input = input("Enter numbers separated by spaces: ")
    user_input_list = user_input.split()

    user_input_list = list(map(int, user_input_list))

    sum_of_numbers = 0

    for i in user_input_list:
        sum_of_numbers += i

    print(f"The sum of all numbers in the list is {sum_of_numbers}")

sum_of_numbers_in_list()

"""
"""
# 19. Napisz funkcję, która odwróci kolejność elementów w danej krotce

def reverse_tuple():
    user_input = input("Enter numbers separated by spaces: ")
    list_user_input = user_input.split()
    list_user_input.reverse()
    tuple_user_input = tuple(list_user_input)

    print(f"The reverse tuple {user_input} is {tuple_user_input} ")

reverse_tuple()

"""
"""
# 20. Napisz funkcję, która zliczy liczbę wystąpień każdego elementu w danym słowniku

def verify_dict():
    keys = []
    values = []
    for i in range(5):
        key = input("Enter key: ")
        keys.append(key)
        value = input("Enter value: ")
        values.append(value)
    user_dict = dict(zip(keys, values))
    return user_dict

from collections import Counter

def count_elements(d):
    # Tworzymy listę wszystkich wartości ze słownika
    values = list(d.values())
    # Używamy Counter do zliczenia wystąpień każdego elementu
    counter = Counter(values)
    return counter

user_dict = verify_dict()
element_counts = count_elements(user_dict)
print(element_counts)

"""
"""
# 21. Napisz funkcję, która przyjmie listę liczb i zwróci nową listę zawierającą tylko parzyste liczby

def even_number_list():
    number_list = []
    for i in range(5):
        user_input = int(input("Enter number: "))
        number_list.append(user_input)

    even_numbers = []
    for number in number_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
print(even_number_list())

"""
"""
# 22. Napisz funkcję, która przyjmie dwie listy o jednakowej długości i zwróci słownik,
# gdzie elementy z pierwszej listy stanowią klucze, a z drugiej listy wartości.

def new_dict():
    list_one = []
    list_two = []

    for i in range(5):
        key = input("Enter key: ")
        list_one.append(key)
        value = input("Enter value: ")
        list_two.append(value)

    user_dict = dict(zip(list_one, list_two))
    print(user_dict)

new_dict()

"""
"""
# 23. Napisz funkcję, która usunie duplikaty z danej listy

def remove_duplicate():
    user_list = [1,2,3,4,5,1,2,3,4,5,1,2,3]
    new_list = set(user_list)
    new_new_list = list(new_list)

    print(new_new_list)

remove_duplicate()

#or 

def remove_duplicate(user_list):
    return list(set(user_list))

# Przykładowe wywołanie funkcji
user_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
print(remove_duplicate(user_list))

"""
"""
# 24. Napisz funkcję, która posortuje słownik według wartości

def sorted_dict():
    user_dict = {"24": "France", "301": "Germany", "22": "Great Britain"}

    # Sortowanie słownika według wartości
    sorted_user_dict = dict(sorted(user_dict.items(), key=lambda item: item[1]))

    # Wyświetlenie posortowanego słownika
    print(sorted_user_dict)


# Wywołanie funkcji
sorted_dict()

"""
"""
# 25. Napisz funkcję, która przyjmie krotkę, a następnie zwróci sumę i iloczyn jej elementów

from functools import reduce
import operator

def create_tuple():
    elements = []
    while True:
        user_input = input("If you want to add to the tuple, enter a value. To finish, type 'E': ")
        if user_input.lower() == 'e':
            break
        else:
            try:
                # Konwertujemy wejście na liczbę, jeśli to możliwe
                value = float(user_input)
                elements.append(value)
            except ValueError:
                print("Please enter a valid number.")

    return tuple(elements)

def sum_and_product(tpl):
    sum_of_elements = sum(tpl)
    product_of_elements = reduce(operator.mul, tpl, 1)  # 1 jest wartością początkową
    return sum_of_elements, product_of_elements

# Przykład użycia
user_tuple = create_tuple()
sum_result, product_result = sum_and_product(user_tuple)
print(f"Sum: {sum_result}, Product: {product_result}")

"""
"""
# 26. Napisz funkcję, która sprawdzi, czy dana wartość występuje w wartościach danego słownika

def verify_dict():
    value_verify = input("Enter value to verify: ")
    example_dict = {1: 22, 2: 23, 3: "dwa", 4: 25}

    try:
        if '.' in value_verify:
            value_verify = float(value_verify)
        else:
            value_verify = int(value_verify)
    except ValueError:
        pass

    if value_verify in example_dict.values():
        print(f"{value_verify} is in {example_dict} ")
    else:
        print(f"{value_verify} is not in {example_dict} ")

verify_dict()

"""
"""
# 27. Napisz funkcję, która połączy dwa słowniki.

def merge_dicts():
    user_dict_one = {"a": 1, "b":2}
    user_dict_two = {"c":3, "d":4}

    user_dict = {**user_dict_one,**user_dict_two}
    print(user_dict)

merge_dicts()

"""
"""
# 28. Napisz funkcję, która pobierze element z danej listy na podstawie indeksu, ale rzuci wyjątek,
# jeśli indeks przekroczy zakres listy

def download_index():
    user_list = ["abc", 11, 25, 465, "ugh", "tur23"]
    index = input("Enter index of list: ")

    try:
        index = int(index)

        value = user_list[index]
        print(f"Value at index {index}: {value}")

    except IndexError:
        print("Error: Index out of range.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


download_index()

"""
"""
# 29. Napisz funkcję, która sprawdzi, czy dany tekst jest palindromem (czyta się tak samo od przodu i od tyłu).

def verify_palindrom():
    user_text = input("Enter text: ")

    if user_text == user_text[::-1]:
        print(f"Text: {user_text} is Palindrom")
    else:
        print(f"Text:  {user_text} is not Palindrom")

verify_palindrom()
"""
"""
# 30. Napisz funkcję, która zliczy liczbę wystąpień każdego znaku w danym tekście.

def count_index():
    user_text = input("Enter text: ")
    count_dict = {}
    for char in user_text:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

print(count_index())

"""
"""
# 31. Napisz funkcję, która zamieni wszystkie litery duże na małe, a litery małe na duże w danym tekście.

def swap_case():
    user_text = input("Enter text: ")
    swapped_text = ''
    for char in user_text:
        if char.islower():
            swapped_text += char.upper()
        elif char.isupper():
            swapped_text += char.lower()
        else:
            swapped_text += char
    return swapped_text


print(swap_case())

"""
"""
# 32. Napisz funkcję, która usunie duplikaty z danej listy, zachowując jedynie unikalne elementy.

def remove_duplicates():
    user_list = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 34]
    unique_list = list(set(user_list))
    print(unique_list)

remove_duplicates()

"""
"""
# 33. Napisz funkcję, która połączy teksty z danej listy w jeden długi tekst, dodając między nimi spację.

def add_lists():
    user_list = ["abcd", "efgh", "ijkl"]
    combined_text = " ".join(user_list)
    print(combined_text)

add_lists()

"""
"""
# 34. Napisz funkcję, która sprawdzi, czy dwa dane słowa są anagramami (mają te same litery, ale w innej kolejności).

def check_anagrams():
    user_input_one = input("Enter first word: ")
    user_input_second = input("Enter second word: ")

    sorted_user_input_one = sorted(user_input_one.lower())
    sorted_user_input_second = sorted(user_input_second.lower())

    if sorted_user_input_one == sorted_user_input_second:
        print(f"{user_input_one} and {user_input_second} are anagrams")
    else:
        print(f"{user_input_one} and {user_input_second} are not anagrams")

check_anagrams()

"""
"""
# 35. Napisz funkcję, która zamieni liczbę na tekst, zachowując unikalne nazwy dla każdej cyfry

def number_to_text(number):
    digit_names = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    number_str = str(number)
    result = [digit_names[digit] for digit in number_str]
    return ' '.join(result)

print(number_to_text(12345))  # Output: one two three four five
print(number_to_text(9087))  # Output: nine zero eight seven

"""
"""
# 36. Napisz funkcję, która pobiera dwie liczby od użytkownika i dzieli pierwszą przez drugą.
# Złap błąd dzielenia przez zero i obsłuż go, wyświetlając stosowny komunikat.

def division_of_two_numbers():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    try:
        score = first_number / second_number
        print(f"{first_number} division {second_number} is {score}")
    except ZeroDivisionError:
        print("Can't division by Zero")

division_of_two_numbers()

"""
"""
# 37. Napisz funkcję, która pobiera listę i indeks, a następnie zwraca element o danym indeksie.
# Złap błąd indeksowania listy i obsłuż go, wyświetlając komunikat o przekroczeniu zakresu listy

def download_data():
    user_list = []
    while True:
        user_choice = input("If you want to stop entering data into the user_list, click 'E': ")
        if user_choice.upper() == 'E':
            break
        else:
            user_input_value = input("Enter data to user_list or click E: ")
            user_list.append(user_input_value)

    while True:
        try:
            index = int(input("Enter the index of the element you want to retrieve: "))
            element = user_list[index]
            print(f"Element at index {index} is {element}")
            break
        except IndexError:
            print("Index out of range. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")


download_data()

"""
"""
# 38. Napisz funkcję, która pobiera napis od użytkownika i zamienia go na liczbę całkowitą.
# Złap błąd, jeśli wprowadzony napis nie jest liczbą, i wyświetl odpowiedni komunikat.


def convert_subtitle():
    try:
        subtitle = input("Enter subtitle: ")
        int_subtitle = int(subtitle)
        print(int_subtitle)
    except ValueError:
        print("Introduced subtitle is not intiger")


convert_subtitle()

"""
"""
# 39. Napisz funkcję, która pobiera nazwę pliku i tekst od użytkownika, a następnie zapisuje ten tekst do pliku.
# Złap błąd, jeśli nie można otworzyć pliku do zapisu, i obsłuż go.

import os
import time
def write_text_to_file():
    file_name = input("Enter the file name: ")
    text_to_write = input("Enter the text to write to the file: ")

    try:
        with open(file_name, 'w') as file:
            file.write(text_to_write)
        print(f"Text successfully written to {file_name}")
    except IOError:
        print("An error occurred while trying to write to the file.")

    time.sleep(10)
    os.remove(file_name)


write_text_to_file()

"""
"""
#  40. Napisz prostą grę w Kamień-Papier-Nożyce. Poproś użytkownika o wybór i porównaj go z wyborem komputera.
#  Złap błąd, jeśli użytkownik wpisze coś innego niż kamień, papier lub nożyce, i obsłuż go.

import random


def stone_paper_scissors():
    choices = {"s": "stone", "p": "paper", "r": "scissors"}
    while True:
        try:
            user_input = input("Enter your choice: stone=S, paper=P, or scissors=R: ").lower()
            if user_input not in choices:
                raise ValueError("Invalid choice")

            computer_output = random.choice(list(choices.keys()))
            print(f"Computer chose: {choices[computer_output]}")

            if user_input == computer_output:
                print("It's a draw!")
            elif (user_input == 's' and computer_output == 'r') or \
                    (user_input == 'p' and computer_output == 's') or \
                    (user_input == 'r' and computer_output == 'p'):
                print("You win!")
            else:
                print("You lost!")
        except ValueError as e:
            print(e)
            print("Please enter 's' for stone, 'p' for paper, or 'r' for scissors.")


stone_paper_scissors()
"""
"""
#41. Napisz funkcję, która pobiera napis od użytkownika i znajduje indeks pierwszej dużej litery w tym napisie.
# Złap błąd, jeśli nie ma dużej litery, i obsłuż go.

def download_text():
    user_text = input("Enter text: ")
    return user_text

def bigest_index(user_index):
    try:
        for index,char in enumerate(user_index):
            if char.isupper():
                return index
        raise ValueError("No uppercase letter found in the text")
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    text = download_text()
    index = bigest_index(text)
    print("Index of the firs uppercase letter:", index)

"""
"""
#42. Napisz funkcję, która pobiera listę liczb i zwraca ich średnią arytmetyczną. Złap błąd, jeśli lista jest pusta,
# i obsłuż go.

def download_list_numbers():
    amount_numbers_in_list = 7
    user_list = []
    try:
        for _ in range(amount_numbers_in_list):
            number = int(input("Enter a number: "))
            user_list.append(number)
    except ValueError as e:
        print(f"Error: {e}")
    return user_list

def arithmetic_average(user_list):
    try:
        if not user_list:
            raise ValueError("The list is empty, cannot compute the average")
        average = sum(user_list) / len(user_list)
        return average
    except ValueError as e:
        return str(e)

if __name__ == "__main__":
    user_list = download_list_numbers()
    average = arithmetic_average(user_list)
    print(f"The arithmetic average is: {average}")

"""
"""
#43. Napisz funkcję symulującą rzut sześciościenną kością do gry. Złap błąd,
# jeśli wynik rzutu nie mieści się w zakresie od 1 do 6, i obsłuż go.

import random

def dice_roll():
    try:
        user_dice_roll = random.randint(1, 10)
        if user_dice_roll < 1 or user_dice_roll > 6:
            raise ValueError("The result is out of the valid range.")
        print(f"Dice Roll: {user_dice_roll}")
    except ValueError as e:
        print(f"An error occurred: {e}")

dice_roll()

"""
"""
#44.  Napisz funkcję, która pobiera datę od użytkownika w formacie "YYYY-MM-DD" i konwertuje ją na obiekt daty.
# Złap błąd, jeśli format daty jest nieprawidłowy, i obsłuż go


from datetime import datetime

def get_user_date():
    try:
        user_input = input("Enter date in YYYY-MM-DD format: ")
        user_date = datetime.strptime(user_input, "%Y-%m-%d").date()
        print(f"The date you entered is: {user_date}")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

if __name__ == "__main__":
    get_user_date()

"""
"""
#45. Napisz prostą kalkulatora, który wykonuje podstawowe operacje matematyczne (+, -, *, /).
# Złap błąd, jeśli użytkownik wpisze coś innego niż liczby, i obsłuż go.

def simple_calculator():
    user_operations = ["*", "/", "+", "-"]
    try:
        user_input = input("Enter action you want to perform (+, -, *, /): ")
        if user_input not in user_operations:
            raise ValueError("Invalid operation. Please enter one of +, -, *, /.")

        first_value = float(input("Enter first value: "))
        second_value = float(input("Enter second value: "))

        if user_input == "*":
            result = first_value * second_value
        elif user_input == "/":
            if second_value == 0:
                raise ValueError("Division by zero is not allowed.")
            result = first_value / second_value
        elif user_input == "+":
            result = first_value + second_value
        elif user_input == "-":
            result = first_value - second_value

        print(f"The result of {first_value} {user_input} {second_value} is {result}")

    except ValueError as e:
        print(f"Error: {e}")


simple_calculator()

"""
"""
#46. Napisz funkcję, która pobiera listę liczb od użytkownika i zwraca największą i najmniejszą liczbę w tej liście.
# Złap błąd, jeśli użytkownik wpisze coś innego niż liczby

def get_user_list():
    try:
        user_input = input("Enter numbers separated by spaces: ")

        user_list = [float(number) for number in user_input.split()]

        if not user_list:
            raise ValueError("The list is empty. Please enter at least one number.")

        highest_number = max(user_list)
        lowest_number = min(user_list)

        return highest_number, lowest_number
    except ValueError as e:
        print(f"Error: {e}")
        return None, None


if __name__ == "__main__":
    highest, lowest = get_user_list()
    if highest is not None and lowest is not None:
        print(f"The highest number is: {highest}")
        print(f"The lowest number is: {lowest}")

"""
"""
#47. Napisz funkcję, która pobiera napis od użytkownika i zwraca jego odwróconą wersję.
# Złap błąd, jeśli użytkownik nie poda żadnego napisu

def reverse_text():
    try:
        user_input = input("Enter text: ")
        if not user_input:
            raise ValueError("You have to enter text")
        reversed_text = user_input[::-1]
        print("Reversed text:", reversed_text)
    except ValueError as e:
        print(e)


reverse_text()
"""
"""
#48. Napisz funkcję, która pobiera od użytkownika dwie liczby: podstawę i wykładnik,
# a następnie zwraca wynik potęgowania. Złap błąd, jeśli użytkownik wpisze coś innego niż liczby

def score_compounding():
    try:
        basis = int(input("Enter basis: "))
        exponent = int(input("Enter exponent: "))
        score = basis **exponent
        return print(score)
    except ValueError:
        print("Enter correct data")

score_compounding()
"""
"""
# 49. Napisz funkcję, która sprawdza, czy podany napis jest palindromem.
# Złap błąd, jeśli użytkownik nie wpisze żadnego napisu

def verify_if_palindrom():
    try:
        user_input = input("Enter text: ")
        if not user_input:
            raise ValueError("You have to enter text")
        if user_input == user_input[::-1]:
            print(f"The {user_input} is a palindrom")
        else:
            print(f"The text: '{user_input}' is not a palindrom")

    except ValueError:
        print("Enter correct data")

verify_if_palindrom()
"""
"""
#50. Napisz funkcję, która pobiera listę słów i zwraca listę zawierającą tylko te słowa,
# które mają parzystą liczbę liter. Złap błąd, jeśli lista słów jest pusta.

def list_of_words_with_even_length():
    try:
        user_input = input("Enter words separated by spaces: ")
        if not user_input:
            raise ValueError("The list is empty")

        user_list = user_input.split()

        even_length_words = [word for word in user_list if len(word) % 2 == 0]

        return even_length_words
    except ValueError as e:
        print(e)
        return []


# Wywołanie funkcji
print(list_of_words_with_even_length())
"""
"""
#51. Napisz funkcję sortującą listę liczb. Złap błąd, jeśli lista zawiera elementy, które nie są liczbami.

def list_sort():
    list_of_numbers = [1,2,45,12,66, 25, 356]
    try:
        sorted_numbers = sorted(list_of_numbers)
        print(sorted_numbers)
    except TypeError:
        print("Char is not intiger")

list_sort()
"""
"""
#52. Napisz funkcję, która sprawdza, czy dana liczba jest liczbą pierwszą. Złap błąd, jeśli użytkownik nie poda liczby.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True 
    if n % 2 == 0:
        return False 
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def verify_number():
    try:
        user_input = float(input("Enter number: "))
        if user_input.is_integer():
            user_input = int(user_input)
            if is_prime(user_input):
                print(f"{user_input} is a prime number")
            else:
                print(f"{user_input} is not a prime number")
        else:
            print("You entered a non-integer number")
    except ValueError:
        print("You didn't enter a number")

verify_number()

"""
"""
#53. Napisz funkcję, która pobiera listę i element do wyszukania. Zwróć indeks pierwszego wystąpienia elementu w liście.
# Złap błąd, jeśli element nie znajduje się w liście

def index_list():
    try:
        list_input = input("Enter values for the list, separated by spaces: ").split()
        search_element = input("Enter the element to search for: ")

        if search_element not in list_input:
            raise ValueError("This element is not in the list")

        index = list_input.index(search_element)
        print(f"In the list {list_input}, the element '{search_element}' is at index {index}")

    except ValueError as e:
        print(e)


index_list()

"""
"""
#54. Napisz prostą grę, w której komputer losuje liczbę od 1 do 10, a użytkownik próbuje ją zgadnąć.
# Złap błąd, jeśli użytkownik wpisuje coś innego niż liczby.

import random

def game_game():
    try:
        user_choice = int(input("Enter a number to guess (1-10): "))
        if not 1 <= user_choice <= 10:
            raise ValueError("Number out of range")

        computer_choice = random.randint(1, 10)

        if user_choice == computer_choice:
            print("You guessed correctly!")
        else:
            print(f"Try again! The correct number was {computer_choice}.")
    except ValueError:
        print("Please enter a valid number between 1 and 10.")


game_game()

"""
"""
#55. Napisz funkcję, która pobiera od użytkownika napis reprezentujący liczbę całkowitą i zwraca tę liczbę.
# Złap błąd, jeśli użytkownik wpisze coś innego niż poprawną reprezentację liczby.

def user_input():
    try:
        user_value = int(input("Enter value: "))
        print(user_value)
    except ValueError:
        print("Value is not correct")

user_input()
"""
"""
#56. Napisz funkcję, która obliczy wskaźnik masy ciała (BMI) na podstawie masy (w kilogramach) i wzrostu (w metrach).
# Funkcja powinna zwrócić ocenę stanu odżywienia (np. "Niedowaga", "Waga normalna", "Nadwaga", "Otyłość").

def calculate_BMI():
    weight_input = float(input("Enter your weight: "))
    heigh_input = float(input("Enter your heigh in cm: "))
    height_meters = heigh_input /100
    rate_BMI = weight_input / (height_meters ** 2)
    rate_BMI = round(rate_BMI, 2)

    if rate_BMI < 20:
        print(f"You have underweight, you BMI it {rate_BMI}")
    elif 20 < rate_BMI < 25:
        print(f"You are in the norm, you BMI it {rate_BMI}")
    elif 25 < rate_BMI < 30:
        print(f"You have overweight, you BMI it {rate_BMI}")
    else:
        print(f"You have obesity, you BMI it {rate_BMI}")

calculate_BMI()
"""
"""
#57. Napisz funkcję, która przyjmie listę liczb i posortuje ją rosnąco lub malejąco, w zależności od przekazanego
# parametru. Domyślnie funkcja powinna sortować rosnąco.

def list_sort():
    list_input = input("Enter value to list, separated space: ")
    number_list = list(map(int, list_input.split()))

    operations_input = input("If you sort this list from lower value to higest value enter 'H'"
                             "or from from higest value to lower value click 'L' ").lower()

    if operations_input == "l":
        sorted_list = sorted(number_list, reverse=True)

    else:
        sorted_list = sorted(number_list)

    print(sorted_list)
list_sort()

"""
"""
#58. Napisz dwie funkcje: jedną do przeliczania temperatury z Celsiusza na Fahrenheita, a drugą z Fahrenheita
# na Celsjusza. Funkcje powinny przyjmować temperaturę jako argument i zwracać przeliczoną wartość.

def celsius_to_fahrenheit(temperature):

    return (temperature * 9 / 5) + 32


def fahrenheit_to_celsius(temperature):

    return (temperature - 32) * 5 / 9


celsius_temp = 20
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} degrees Celsius is equal to {fahrenheit_temp} degrees Fahrenheit.")

fahrenheit_temp = 68
celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} degrees Fahrenheit is equal to {celsius_temp} degrees Celsius.")

"""
"""
#59. Napisz funkcję, która sprawdzi, czy dany napis jest palindromem. Palindrom to ciąg znaków, który czyta się tak
# samo od lewej do prawej, jak i od prawej do lewej (np. "kajak").

def verify_palindrom(text):
    if text == text[::-1]:
        return f"This text {text} is a palindrom"
    else:
        return f"This text {text} is not a palindrom"

pali = "12321"
check = verify_palindrom(pali)
print(check)
"""
"""
#60. Napisz funkcję generującą losowe hasło o określonej długości. Funkcja powinna pozwalać na określenie,
# czy hasło powinno zawierać małe i duże litery, cyfry oraz znaki specjalne.

import random
import string


def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password



length = 6
use_lowercase = False
use_uppercase = False
use_digits = True
use_special = False

generated_password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special)
print(f"Generated password: {generated_password}")
"""
"""
#61. Napisz funkcję, która przyjmie rok urodzenia i zwróci aktualny wiek osoby.
# Wartość aktualnego roku możesz uzyskać za pomocą modułu datetime.

import datetime

def calculate_age(year_of_birth):
    today = datetime.date.today()
    age = today.year - year_of_birth
    if (today.month, today.day) < (datetime.date(year_of_birth, 1, 1).month, datetime.date(year_of_birth, 1, 1).day):
        age -= 1
    return age


user_input = int(input("Enter your year of birth: "))
age = calculate_age(user_input)
print("Your age is:", age)

"""
"""
#62. Napisz funkcję, która przyjmie listę słów i zwróci nową listę zawierającą tylko te słowa,
# które mają określoną liczbę liter (parametr przekazywany do funkcji).

def list_of_words_by_length(words, length):
    new_list = [word for word in words if len(word) == length]
    return new_list

user_input = input("Enter words separated by spaces: ")
user_list = user_input.split()

length = int(input("Enter the number of letters that words should have in the new list: "))


filtered_list = list_of_words_by_length(user_list, length)
print("Filtered list:", filtered_list)

"""
"""
#63. Napisz funkcję, która pozwoli dwóm graczom zagrać w grę w Kamień-Papier-Nożyce.
# Funkcja powinna przyjmować wybór każdego gracza jako argumenty i zwracać wynik rundy (np. "Gracz 1 wygrywa!")

def game_stone_paper_scissor(choice_1, choice_2):

    choice_1 = choice_1.lower()
    choice_2 = choice_2.lower()


    if choice_1 == choice_2:
        return "It's a draw!"
    elif (choice_1 == 's' and choice_2 == 'r') or \
         (choice_1 == 'p' and choice_2 == 's') or \
         (choice_1 == 'r' and choice_2 == 'p'):
        return "Gracz 2 wygrywa!"
    elif (choice_1 == 'r' and choice_2 == 's') or \
         (choice_1 == 's' and choice_2 == 'p') or \
         (choice_1 == 'p' and choice_2 == 'r'):
        return "Gracz 1 wygrywa!"
    else:
        return "Nieprawidłowy wybór. Użyj 's' dla kamienia, 'p' dla papieru, 'r' dla nożyczek."


player1_choice = input("Gracz 1, podaj swój wybór (s: kamień, p: papier, r: nożyczki): ")
player2_choice = input("Gracz 2, podaj swój wybór (s: kamień, p: papier, r: nożyczki): ")

result = game_stone_paper_scissor(player1_choice, player2_choice)
print(result)
"""
"""
#64. Napisz funkcję, która obliczy sumę cyfr danej liczby całkowitej.

def sum_of_digits(number):
    sum_number = 0
    for digit in str(number):
        if digit.isdigit():
            sum_number += int(digit)
    return sum_number

user_input = input("Enter number: ")
sums = sum_of_digits(user_input)
print(sums)

"""
"""
#65. Napisz funkcję, która przyjmie listę liczb i zwróci największy element tej listy

def higest_value(list_of_numbers):
    return max(list_of_numbers)


user_input = input("Enter value to list, separated by space:  ")
list_of_numbers = [int(number) for number in user_input.split()]

result = higest_value(list_of_numbers)
print("The highest value in the list is:", result)

"""
#66.Napisz funkcję kalkulatora podatkowego, która przyjmie dochód jako argument i zwróci obliczoną kwotę podatku.
# Możesz użyć prostego systemu podatkowego, np. 18% dla dochodów poniżej 50 000 i 25% dla dochodów powyżej 50 000

