from string import digits, punctuation, ascii_letters
import itertools

attempt = 0

def main():
    global possible_symbols, password_lenght
    print("hi")

    try:
        password_lenght = input("Введите длину пароля, от сколько - до скольки символов, например 3-7:")
        password_lenght = [int(item) for item in password_lenght.split('-')]
    except:
        print('Проверьте введенные данные')
    print('Если пароль содержит только цифры, введите: 1\n Если пароль содержит только буквы, введите: 2\n '
          'Если пароль содержит буквы и цифры, введите: 3\n Если пароль содержит буквы,цифры и спецсимволы введите: 4\n')

    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits

        elif choice == 2:
            possible_symbols = ascii_letters

        elif choice == 3:
            possible_symbols = digits + ascii_letters

        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation

        else:
            possible_symbols = 'O.o, такого выбора нет)'
        print(possible_symbols)
    except:
        print("O.o, такого выбора нет")

def go_to_passwords():
    global attempt
    for pass_lenght in range(password_lenght[0], password_lenght[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_lenght):
            attempt += 1
            password = "".join(password)
            print("Attempt", attempt,":",password)

if __name__ == '__main__':
    main()
    go_to_passwords()
    print('Пароль подобран ;)')
