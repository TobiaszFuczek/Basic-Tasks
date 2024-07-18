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



