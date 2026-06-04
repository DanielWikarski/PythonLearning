# Zadanie 1

print("=== Zadanie 1 ===")

filename = "raport_finansowy_2026_final.csv"

print(filename[-4:] == '.csv')
print(filename[:-4])
print(filename[filename.find(".")-3:filename.find(".")])


# Zadanie 2

print("=== Zadanie 2 ===")

text = "ProgramowaniePython"

text_halved_index = len(text) // 2
print(text_halved_index)

is_text_even = len(text) % 2 == 0
print(is_text_even)

print(text[text_halved_index])


# Zadanie 3

print("=== Zadanie 3 ===")

sentence = "Python jest super"

sentence_splited = sentence.split(" ")

first_word = sentence_splited[0]
print(first_word[::-1]) # pierwsze słowo od tyłu

last_word = sentence_splited[-1]
print(last_word[::-1]) # ostatnie słowo od tyłu


print(sentence[::-1]) # cały napis backwards
print(sentence[::2]) # co drugi znak całego napisu


# Zadanie 4

print("=== Zadanie 4 ===")
product_code = "LAPTOP-DELL-2026-PRO"

first_separator = product_code.find("-") # pierwszy separator
second_separator = product_code.find("-", first_separator + 1) # drugi separator
                    # argumenty: czego szukam, od kiedy szukam (po pierwszym myślniku) +1 bo idę za myślnik

third_separator = product_code.find("-", second_separator + 1)


print(product_code[first_separator+1:second_separator]) # DELL
print(product_code[second_separator+1:third_separator]) # 2026
print(product_code[third_separator+1:]) # PRO
print(product_code[third_separator+1:]== "PRO")

# Zadanie 5

print("=== Zadanie 5 ===")
phone = "123456789"

last_four_phone_digits = phone[-4:] # ostatnie cyfry, które mają być odkryte
masked_phone_digits = phone.replace(phone[:-4], "*" * (len(phone)-4)) # zamiana wszystkich liczb poza
                                                                      # 4 ostatnimi na gwiazdki, mnożę liczbę
                                                                      # gwiazdek razy liczbę pozostałych liczb, -4
                                                                      # bo 4 ostatnie są widoczne

print(masked_phone_digits)

# Zadanie 6

print("=== Zadanie 6 ===")

email = "jan.kowalski@example.com"

login = email[:email.find("@")] # login (szukam co jest przed @)
print(login)

domain = email[email.find("@")+1:] # domena (szukam co jest po @)
print(domain)

print(email.endswith(".com")) # sprawdzam za pomocą endswith czy email kończy się na .com

print(login[:3]) # pierwsze 3 znaki loginu

print(domain[::-1]) # domena od tyłu



