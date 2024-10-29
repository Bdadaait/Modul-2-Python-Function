
# Task 1: Write a function that lets the user add items to a list:

# Task 2: Include a function to remove items from the list:

# Task 3: Add a function that prints out the entire list in a formatted way:

def add_item(shopping_list, item):
    shopping_list.append(item) 
    print(f"'{item}' has been added to your shopping list.") 

def remove_item(shopping_list, item): 
   shopping_list.remove(item) 
   print(f"'{item}' has been removed from your shopping list.")
    
def print_list(shopping_list): 
        if shopping_list: 
             print("Your shopping list:") 
             for i, item in enumerate(shopping_list, start=1): 
                 print(f"{i}. {item}") 
        else: 
            print("Your shopping list is empty.") 
def shopping_list_maker(): 
    shopping_list = [] 
    
    while True: 
        
        print("a. Add item") 
        print("b. Remove item") 
        print("c. View shopping list") 
        print("d. Quit") 
            
        choice = input("Enter your choice (a/b/c/d): ") 
            
        if choice == 'a': 
            item = input("Enter the item to add: ") 
            add_item(shopping_list, item) 
        elif choice == 'b': 
            item = input("Enter the item to remove: ") 
            remove_item(shopping_list, item) 
        elif choice == 'c': 
            print_list(shopping_list) 
        elif choice == 'd': 
            print("Exiting the shopping list program. Goodbye!") 
            break 
        else: 
            print("Invalid choice. Please select a valid option.") 

shopping_list_maker()

