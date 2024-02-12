FILE_NAME = "phone_book.txt"

def read_data(FILE_NAME):
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = [line for line in file if len(line) > 0]
            return data
    except FileNotFoundError:
        print("\nФайл не найден.")
        return []
  
def print_data(data):
    if len(data) == 0:
        print("Справочник пуст, необходимо его заполнить.\n")
        write_data(FILE_NAME)
        return

    for line in data:
        print(line)

def write_data(FILE_NAME):
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        contact_name = input("Введите имя: ")
        contact_surname = input("Введите отчество : ")
        contact_patronymic = input("Введите фамилию: ")
        phone_number = input("Введите номер телефона: ")
        file.write(f"{contact_name},{contact_surname},{contact_patronymic},{phone_number}\n")

def rewrite_file(FILE_NAME, data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for line in data:
            file.write(line)

def find_contact(data):
    user_choice = input("Введите данные для поиска: ")
    founded = []
    for idx, line in enumerate(data):
        if user_choice.lower() in line.lower():
            print(line)
            founded.append(idx)
    if len(founded) == 0:  
        print("Контакт не найден")
    return founded

def select(data, founded):
    if len(founded)>1:
        for i, idx in enumerate(founded):
            print(f"{i+1}. {data[idx]}")
        user_choice = int(input("Введите номер контакта: "))
        user_choice = founded[user_choice-1]
    else:
        user_choice = founded[0]
    return user_choice
        
def delete_contact(data, user_choice):
    deleted = data.pop(user_choice)
    print(f'Контакт {deleted} удален')
    return data

def edit_data(data, user_choice):
    choice_change = int(input(
        '''1 - изменить имя
        2 - изменить отчество
        3 - фамилию
        4 - номер телефона
        '''))
    line = data[user_choice].split(",")
    print("Старое значение: ", line[choice_change - 1])
    line[choice_change - 1] = input("Новое значение: ")

    data[user_choice] = ",".join(line)+"\n"

def export_contact(data, user_choice):
    FILE_NAME = input("Введите название файла: ")
    # FILE_NAME = f"{FILE_NAME}.txt"
    with open(f"{FILE_NAME}.txt", 'a', encoding="utf-8") as file:
        file.write(f"{data[user_choice]}")

def main():
    if len(read_data(FILE_NAME)) == 0:
        print("Справочник пуст, необходимо его заполнить.\n")
        write_data(FILE_NAME)
    flag = True
    while flag:
        print("\nГлавное меню телефонного справочника")
        print("1 - показать контакты")
        print("2 - добавить контакт")
        print("3 - найти контакт")
        print("4 - удалить контакт")
        print("5 - изменить контакт")
        print("6 - экспортировать контакт в другой файл")
        print("0 - выход")
        user_choice = input("Выберите действие: ")
        if user_choice == "0":
            flag = False
        elif user_choice == "1":
            print_data(read_data(FILE_NAME))
        elif user_choice == "2":
            write_data(FILE_NAME)
        elif user_choice == "3":
            find_contact(read_data(FILE_NAME))
        elif user_choice == "4":
            data = read_data(FILE_NAME)
            founded = find_contact(data)
            if len(founded)>0:
                rewrite_file(FILE_NAME, delete_contact(data, select(data, founded)))
        elif user_choice == "5":
            data = read_data(FILE_NAME)
            founded = find_contact(data)
            if len(founded)>0:
                edit_data(data, select(data, founded))
                rewrite_file(FILE_NAME, data)
        elif user_choice == "6":
            data = read_data(FILE_NAME)
            founded = [x for x in range(len(data))]
            export_contact(data, select(data, founded))

#______main_______

if __name__ == "__main__":
    main()
