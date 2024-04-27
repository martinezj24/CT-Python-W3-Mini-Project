import re
import os

# Contact Data Storage (Starting With An Empty Dictionary):
def read_contact():
    contacts = {}
    try:
        with open('contact_list.txt', 'r') as file:
            for line in file:
                data = re.search(r'([\w\s]+)-:-([\d{3}-\d{3}-\d{4}]+)-:-([\w\s]+)', line)
                email = data.group(3) #email is main key because it is usique, prevents errors for any duplicate names
                contacts[email] = {'Name': data.group(1), 'Phone': data.group(2), 'Email': email} 
    except FileNotFoundError:
        print('No Local files')
        return {}
    else:
        print('Importing Local Data...')
        return contacts

def write_contacts(contacts):
    with open('contact_list.txt', 'w') as file:
        for name, info in contacts.items():
            file.write(f"{name}-:-{info['Phone']}-:-{info['Email']}-:-{info.get('Notes', '')}\n")


# Functions For Each Action

# Add Contact Info:
def add_contact(contacts):
    os.system('cls') #using os.system('cls') for smoother user experience and decluttering terminal
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    additional = input('Notes: ')
    contacts[email] = {'Name': name, 'Phone': phone, 'Email': email, 'Notes': additional}
    write_contacts(contacts)
    print(f'Added {name} to your list!')


# View All Contacts:
def display(contacts):
    os.system('cls')
    print('Contacts List')
    print('---------------')
    for idx, contact in enumerate(contacts.values()):
        if 'Name' in contact:
            print(f"{idx+1}.) Name: {contact['Name']}, Phone: {contact.get('Phone', 'N/A')}, Email: {contact.get('Email', 'N/A')}")
        else:
            print(f"Error: Missing 'Name' key in contact {idx+1}")


# Remove Contact By Corresponding Number:
def remove_contact(contacts):
    os.system('cls')
    display(contacts)
    num_contacts = len(contacts)
    option = int(input(f"Enter the number of the contact you want to remove (1-{num_contacts}): "))
    
    if 1 <= option <= num_contacts: #ensures number is valid range of choices
        remove_email = list(contacts)[option - 1]
        removed_contact = contacts.pop(remove_email) #using .pop() to remove selected contact
        print(f"Removed {removed_contact['Name']}") #Success statement
        write_contacts(contacts)
    else:
        print('Invalid entry. Please enter a number within the valid range.')


# Search For Existing Contact (With Option To Add New):
def find_contact(contacts):
    os.system('cls')
    contact_to_find = input('Enter the email address of contact you want to find: ')
    if contact_to_find in contacts:
        contact = contacts[contact_to_find]
        print('Contact Profile Retrieved!')
        print(f"Name: {contact['Name']}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
        print(f"Notes: {contact.get('Notes', '')}")
    else: #Option to add new customer if customer does not exist
        add_option = input('Contact does not exist. Would you like to add this contact? Enter (Y/N): ')
        if add_option.upper() == 'Y':
            add_contact(contacts)
        else:
            print('Returning to main menu')

# Edit Existing Contact:

def edit_contact(contacts):
    os.system('cls')
    display(contacts)
    choice_edit = int(input('Choose corresponding number of contact to edit: '))
    if 1 <= choice_edit <= len(contacts): #ensures number is in valid range
        email_to_edit = list(contacts)[choice_edit - 1] #converting choice to corresponding email
        contact_to_edit = contacts[email_to_edit]
        new_name = input(f"Enter new name for {contact_to_edit['Name']}: ")
        new_phone = input(f"Enter new phone number for {contact_to_edit['Phone']}: ")
        new_email = input(f"Enter new email address for {contact_to_edit['Email']}: ")
        new_notes = input(f"Enter new notes for {contact_to_edit.get('Notes', '')}: ")
        contacts[email_to_edit] = {'Name': new_name, 'Phone': new_phone, 'Email': new_email, 'Notes': new_notes}
        write_contacts(contacts) #ensures edit will be recorded in the file
        
        print(f"Contact {contact_to_edit['Name']} updated successfully!")
    else:
        print("Invalid contact number. Please choose a number within the valid range.")

#User Interface (UI):

def menu():
    contacts = {}
    while True:
        action = input('''
    Welcome to the Contact Management System! 
Menu:
1.) Add a new contact
2.) Edit an existing contact
3.) Delete a contact
4.) Search for a contact
5.) Display all contacts
6.) Log Out

> ''')
        if action == '1':
            add_contact(contacts)
        elif action == '2':
            edit_contact(contacts)
        elif action == '3':
            remove_contact(contacts)
        elif action == '4':
            find_contact(contacts)
        elif action == '5':
            display(contacts)
        elif action == '6':
            print("Logged Out Successfully!")
            break
        else:
            print('Invalid input, try again!')


menu()