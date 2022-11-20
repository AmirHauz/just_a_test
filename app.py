# display menu - done
# get input from the user - done
# implement the user selection - -DONE
#save  /LOAD (Serializing/deSerializing) -DONE

import json
import os

my_file= "contacts.json"
contacts=[]

def display_menu():
    print("a - add") # DONE
    print("d - delete")
    print("s - search")
    print("p - print all") # DONE
    print("x - exit") # DONE

def add_contact():
    temp_contact =input('contact name?')
    contacts.append(temp_contact)
    print('a contact added')

def print_all():
    for contact in contacts:
        print(contact)

def save_2_file():
    json_object = json.dumps(contacts, indent=4)
    print(json_object)
    # write contacts array to json file 
    with open(my_file, "w") as outfile:
	    outfile.write(json_object)

def load_from_file():
    global contacts
    isExist = os.path.exists(my_file)
     # read from json file to contacts array
    if isExist:
        with open(my_file, 'r') as openfile:
            contacts = json.load(openfile)
        print(contacts)

def search():
    if input('contact name?') in contacts: return True
    return False
    
def del_contact():
    #input from the user
    #
    temp = input('contact name')
    if temp in contacts:
        print(f"delete mr/{temp}")
        contacts.remove(temp)
    else: print(f"mr.{temp} not found")

def main():
    
    kelet = ''
    load_from_file()

    while (kelet  != 'x'):
        if kelet == 's':
            if search() : 
                print("Found")
            else:
                print("not Found")
        if kelet == 'd':
            del_contact()
        if kelet == 'a':
            add_contact()
        if kelet == 'p':
            print_all()
        display_menu()
        kelet=input("whata 2 do?")
    save_2_file()
    
    

if __name__ == '__main__':
    main()
    




