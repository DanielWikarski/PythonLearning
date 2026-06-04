import string
import random





password_len = int(input("Podaj długośc hasła: "))
has_punctuation = str(input("Czy hasło ma zawierać znak specjalny? \n"
                             "[TAK/NIE]")).upper().strip()

def generate_password(password_len: int, has_punctuation: str) -> str:
        generated_password = ""

        for letter in range(password_len):
            random_letter = random.choice(string.ascii_letters)
            generated_password += random_letter
        if has_punctuation == "TAK":
            generated_password = generated_password[0:password_len-1]
            generated_password += random.choice(string.punctuation)
        elif has_punctuation == "NIE":
            pass

        else:
            print("[Wpisano błędną komendę! - Hasło zostanie stworzone bez "
                  "użycia znaku specjalnego]")



        generated_password_as_list = list()
        # robię listę, żeby móc zrobić shuffle na niej
        for symbol in generated_password:
            generated_password_as_list.append(symbol)

        random.shuffle(generated_password_as_list)

        generated_password = "".join(generated_password_as_list)
        # zshufflowaną listę łączę ponownie w stringa
        return generated_password



password = generate_password(password_len, has_punctuation)

print(f"Twoje utworzone hasło to: {password}")


