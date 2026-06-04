entry_number = int(input("Wpisz liczbę od 1 do 100: "))

collatz_conjecture = []

x = entry_number

if 0 <= x <= 100: # walidator czy user nie wypisał liczy spoza zakresu
    while x != 1:

        if x % 2 == 0:
            x = x / 2
            collatz_conjecture.append(x)
        else:
            x = (3 * x) + 1
            collatz_conjecture.append(x)

    print(collatz_conjecture)
else:
    print("Liczba spoza zakresu 1-100...")



