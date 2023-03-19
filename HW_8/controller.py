import view
import model



def run():
    view.greetings()
    view.openPhoneBook()
    while True:
        view.menu()
        answer = str(input('Choose needed operation: '))
        if answer == '1':
            model.printList(view.list)
        elif answer == '2':
            model.addPerson(view.list)
        elif answer == '3':
            model.search(view.list)
        elif answer == '4':
            model.changePerson(view.list)
        elif answer == '5':
            model.removePerson(view.list)
        elif answer == '6':
            view.goodbye()
            return 0
           
       


