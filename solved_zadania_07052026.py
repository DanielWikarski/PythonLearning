# Zadanie 1
from traceback import print_tb

print("=== Zadanie 1 ===")

keyboard_net_price = 450
mouse_net_price = 300
monitor_net_price = 1200
headphones_net_price = 400

tax_rate_23 = 0.23

print(f"Klawiatura kosztuje: {keyboard_net_price + (keyboard_net_price * tax_rate_23)} złotych brutto \n"
      f"Myszka kosztuje: {mouse_net_price + (mouse_net_price * tax_rate_23)} złotych brutto \n"
      f"Monitor kosztuje: {monitor_net_price + (monitor_net_price * tax_rate_23)} złotych brutto \n"
      f"Słuchawki kosztują: {headphones_net_price + (headphones_net_price * tax_rate_23)} złotych brutto")

print(f"Łączna suma wszystkich produktów brutto: {(keyboard_net_price + (keyboard_net_price * tax_rate_23))
    + (mouse_net_price + (mouse_net_price * tax_rate_23))
    + monitor_net_price + (monitor_net_price * tax_rate_23)
    + headphones_net_price + (headphones_net_price * tax_rate_23)} złotych brutto")

# Zadanie 2

print("=== Zadanie 2 ===")

name = "Daniel"
age = 26
height = 176

print("Cześć, mam na imię " + name + ", mam " + str(age) + " lat i " + str(height) + "cm wzrostu.")
print(f"Cześć, mam na imię {name}, mam {age} lat i {height}cm wzrostu.")

# Zadanie 3

print("=== Zadanie 3 ===")

value_a = 15
value_b = 4

print(f"Dane są liczby: A = {value_a} i B = {value_b}")

print(f"Wynik dodawania A i B to: {value_a + value_b}")

print(f"Wynik odejmowania A i B to: {value_a- value_b}")

print(f"Wynik mnożenia A i B to: {value_a * value_b}")

print(f"Wynik dzielenia A i B to: {value_a / value_b}")

print(f"Wynik potęgowania A i B to: {value_a ** value_b}")

print(f"Wynik dzielenia całkowitego A i B to: {value_a // value_b}")

print(f"Wynik modulo A i B to: {value_a % value_b}")

# Zadanie 4

print("=== Zadanie 4 ===")

checking_number = 17

is_number_even = 17 % 2 == 0
is_number_odd = 17 % 2 != 0

print(f"Liczba {checking_number} jest... \n"
      f"Parzysta:  {is_number_even} \n"
      f"Nieparzysta: {is_number_odd}")


# Zadanie 5

print("=== Zadanie 5 ===")

PI = 3.14159265359

print(f"Liczba PI zaokrąglona do 2 miejsc po przecinku: {round(PI, 2)} \n"
      f"Liczba PI zaokrąglona do 4 miejsc po przecinku: {round(PI, 4)} \n"
      f"Liczba PI jako integer: {int(PI)}")

# Zadanie 6

print("=== Zadanie 6 ===")

user_name = "Daniel"
user_surname = "Wikarski"
user_birth_year = 1999

print("Login użytkownika to: "+ user_name.lower()+"_"+user_surname.lower()+"_"+str(user_birth_year))

# Zadanie 7

print("=== Zadanie 7 ===")

city = "Kraków"

print(f"{city} zapisane wielkimi literami: {city.upper()}\n"
      f"{city} zapisane małymi literami: {city.lower()}\n"
      f"{city} zapisane z pierwszej dużej litery: {city.title()}")


# Zadanie 8

print("=== Zadanie 8 ===")

celsius_temperature = 28

print(f"{celsius_temperature}℃ w przeliczeniu na stopnie Fahrenheita to: "
      f"{celsius_temperature * 9/5 + 32}F")

# Zadanie 9

print("=== Zadanie 9 ===")

player_nickname = "danielek"
player_points = 21
player_level = 37
player_health_value = 10

print(f">>> Profil gracza <<< \n"
      f"Nazwa gracza: {player_nickname}\n"
      f"Punkty gracza: {player_points}\n"
      f"Poziom gracza: {player_level}\n"
      f"Liczba żyć gracza: {player_health_value}")

# Zadanie 10

print("=== Zadanie 10 ===")

number_x = 12
number_y = 20

print(f"Czy {number_x} jest większa od {number_y}?: {number_x > number_y} \n"
      f"Czy {number_x} jest równa {number_y}?: {number_x == number_y} \n"
      f"Czy {number_x} jest różne od {number_y}?: {number_x != number_y} \n"
      f"Czy {number_x} jest mniejsze lub równe {number_y}?: {number_x <= number_y} \n")


# Zadanie 11

print("=== Zadanie 11 ===")

item_pizza_price = 55
item_bewerage_price = 20
item_desert_price = 25

print(f"Suma całego zamówienia: {item_pizza_price + item_bewerage_price + item_desert_price}zł. \n"
      f"Napiwek dla kelnera: {(item_pizza_price + item_bewerage_price + item_desert_price)* 0.1}zł \n"
      f"Końcowa kwota do zapłaty: {(item_pizza_price + item_bewerage_price + item_desert_price)+
      (item_pizza_price + item_bewerage_price + item_desert_price)* 0.1}zł")

# Zadanie 12

print("=== Zadanie 12 ===")

message = "Python jest super "

print(f"Wiadomośc zapisana dużymi literami: {message.upper()}\n")
print(f"Długość wiadomości: {len(message)} znaków (w tym spacje)\n")
print(f"Wiadomość powtórzona 3 razy: {message*3}")

# Zadanie 13

print("=== Zadanie 13 ===")

hollydays_budget = 2500

price_hotel = 1200
price_transport = 600
price_food = 400

print(f"Budżet wynosi {hollydays_budget} złotych,"
      f" koszt hotelu to {price_hotel} złotych, "
      f"koszt transportu to {price_transport} złotych, koszt jedzenia "
      f"to {price_food} złotych. \n"
      f"Łącza suma wydatków to: {price_hotel+price_transport+price_food}zł.\n"
      f"Czy budżet wystarczy na wakacje? {hollydays_budget >= price_hotel + price_transport + price_food} \n"
      f"Po wakacjach pozostanie nam się: {hollydays_budget - (price_hotel + price_transport + price_food)} złotych.")

# Zadanie 14

print("=== Zadanie 14 ===")

weight = 75
height_declared_in_meters = 1.75

print(f"Wskażnik BMI dla wagi {weight}kg i {height}cm wzrostu to: {round((weight / (height_declared_in_meters ** 2)), 2) }")

# Zadanie 15

print("=== Zadanie 15 ===")

age = "25"
result = int(age) + 5

print(result)