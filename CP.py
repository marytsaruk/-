def find_times(file_path, user_value):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            time, measurement = line.split()
            if float(measurement) > float(user_value):
                print(time)

while True:
    print("1. Вести значення")
    print("2. Вийти з програми")

    choice = input("Введіть свій вибір: ")

    if choice == '1':
        user_value = input('Введіть значення: ')
        find_times('file.txt', user_value)
    elif choice == '2':
        print("До побачення!")
        break
    else:
        print("Некоректний вибір. Будь ласка, спробуйте ще раз.")
