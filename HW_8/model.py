from person import Person



def printList(list):
    for p in list:
        p.toConsole()
        


def savePhoneBook(list):
    with open('PhoneBook.txt', 'w') as f:
        for p in list:
            f.write(f'{str(p)}\n')


def search(list):
    searchText = input('Write a word or number to search:\n')
    option = int(
        input('Choose an option: \n1.Name\n2.Surname\n3.Middle name\n4.Number\n'))
    if option == 1:
        found = 0
        for p in list:
            if p.name == searchText:
                p.toConsole()
                found = 1
        if not found:
            print('Not found')

    elif option == 2:
        found = 0
        for p in list:
            if p.surname == searchText:
                p.toConsole()
                found = 1
        if not found:
            print('Not found')

    elif option == 3:
        found = 0
        for p in list:
            if p.middle == searchText:
                p.toConsole()
                found = 1
        if not found:
            print('Not found')

    elif option == 4:
        found = 0
        for p in list:
            if p.number == searchText:
                p.toConsole()
                found = 1
        if not found:
            print('Not found')
    else:
        print('Wrong option')


def removePerson(list):
    searchText = input('Write a word or number to delete:\n')
    option = int(
        input('Choose an option: \n1.Name\n2.Surname\n3.Middle name\n4.Number\n'))
    if option == 1:
        found = 0
        count = -1
        for p in list:
            count += 1
            if p.name == searchText:
                p.toConsole()
                print('This person was deleted')
                list.pop(count)
                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    elif option == 2:
        found = 0
        count = -1
        for p in list:
            count += 1
            if p.surname == searchText:
                p.toConsole()
                print('This person was deleted')
                list.pop(count)
                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    elif option == 3:
        found = 0
        count = -1
        for p in list:
            count += 1
            if p.middle == searchText:
                p.toConsole()
                print('This person was deleted')
                list.pop(count)
                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    elif option == 4:
        found = 0
        count = -1
        for p in list:
            count += 1
            if p.number == searchText:
                p.toConsole()
                print('This person was deleted')
                list.pop(count)
                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    else:
        print('Wrong option')


def addPerson(list):
    name = input('Write a name:\n')
    surname = input('Write a surname:\n')
    middle = input('Write a middle name:\n')
    number = input('Write a number:\n')

    list.append(Person(name, surname, middle, number))
    savePhoneBook(list)


def changePerson(list):
    searchText = input('Write a word or number to edit:\n')
    option = int(
        input('Choose an option: \n1.Name\n2.Surname\n3.Middle name\n4.Number\n'))

    if option == 1:
        found = 0
        for p in list:
            if p.name == searchText:
                p.toConsole()
                print('This person will be edited\n')
                name = input('Write a name:\n')
                surname = input('Write a surname:\n')
                middle = input('Write a middle name:\n')
                number = input('Write a number:\n')

                p.name = name
                p.surname = surname
                p.middle = middle
                p.number = number

                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    elif option == 2:
        found = 0
        for p in list:
            if p.surname == searchText:
                p.toConsole()
                print('This person will be edited\n')
                name = input('Write a name:\n')
                surname = input('Write a surname:\n')
                middle = input('Write a middle name:\n')
                number = input('Write a number:\n')

                p.name = name
                p.surname = surname
                p.middle = middle
                p.number = number

                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    elif option == 3:
        found = 0
        for p in list:
            if p.middle == searchText:
                p.toConsole()
                print('This person will be edited\n')
                name = input('Write a name:\n')
                surname = input('Write a surname:\n')
                middle = input('Write a middle name:\n')
                number = input('Write a number:\n')

                p.name = name
                p.surname = surname
                p.middle = middle
                p.number = number

                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)

    elif option == 4:
        found = 0
        for p in list:
            if p.number == searchText:
                p.toConsole()
                print('This person will be edited\n')
                name = input('Write a name:\n')
                surname = input('Write a surname:\n')
                middle = input('Write a middle name:\n')
                number = input('Write a number:\n')

                p.name = name
                p.surname = surname
                p.middle = middle
                p.number = number

                found = 1
        if not found:
            print('Not found')

        savePhoneBook(list)
    else:
        print('Wrong option')
