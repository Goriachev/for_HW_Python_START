from person import Person
import model

list = []

def greetings():
    print('Welcome to our phonebook!')
      

def openPhoneBook():
    with open('PhoneBook.txt','r') as f:
        for line in f:
            data = line.split()
            list.append(Person(data[0],data[1],data[2],data[3]))

 
def menu():
    print('Operations:')
    print('1 - Print full phonebook')
    print('2 - Add new person')
    print('3 - Search person')
    print('4 - Edit person')
    print('5 - Remove person')
    print('6 - Exit')

def goodbye():
    print("Thank you for using our phonebook!")
        
    