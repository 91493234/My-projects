import os 
import pyfiglet

operations_of_file = {1: 'Create file', 2: 'View all file', 3: 'Edit file', 4: 'Delete file', 5: 'Read file', 6: 'Exit '}
title = pyfiglet.figlet_format('\nFILE   MANAGER')
print(title)

def ops():  
    for i in operations_of_file.keys():
        print(f'{i}: {operations_of_file[i]}')
ops()


while True:
    user_want = int(input("Enter what you want: "))
    show_demand = operations_of_file[user_want]
    def showDemand():
        print(f'{show_demand}\n')


    if user_want == 1:
        showDemand()
        ask_for_file_name = input("Enter file name to create: ")
        if os.path.exists(ask_for_file_name):
            print(f'ERROR! {ask_for_file_name} is not exist')
        else:
            with open(ask_for_file_name, 'x') as crt:
                pass
            print(f"Successfully! '{ask_for_file_name}' file is created.")
            ask_again = input('Does you want to create more files: ').lower()
            if os.path.exist(ask_again):
                print(f'ERROR! {ask_again} is not exist')
            else:
                if ask_again == 'yes':
                    ask_for_file_name_again = input("Enter file name to create: ")
                    with open(ask_for_file_name_again, 'x') as crt2:
                        print(f"Successfully! '{ask_for_file_name_again}' file is created.")
                    ops()
                else:
                    ops()
        

    elif user_want == 2:
        showDemand()
        default_directory  = "E:/python_course/My_project/file manager"
        show_files = os.listdir(default_directory)
        for directory in show_files:
            print(directory)
        ops()
    elif user_want == 3:
        showDemand()
        ask_for_file = input('Enter file name to edit: ')
        if os.path.exists(ask_for_file):
            ask_for_message = input('Enter  data to add this file: ')
            with open(ask_for_file, 'w') as edit:
                edit.write(ask_for_message)
            print('Data edit successfully!')     

            ask_for_more_data = input('Does you want to add more data NO/Yes: ').lower()        
    
            if ask_for_more_data == 'yes':
                ask_for_which_file = input('Enter file name to add more data: ')
                if os.path.exists(ask_for_which_file):
                    ask_for_message_again = input('Enter more data to add: ')
                    with open(ask_for_which_file, 'a') as addData:
                        addData.write(ask_for_message_again)
                    print('Data added successfully!')
                    ops()
                else:
                    print(f'ERROR! {ask_for_which_file} file is not exist')

            else:
                ops()            
                
        else:
            print(f'ERROR! {ask_for_file} file is not exist')
            ops()

    elif user_want == 4:
        showDemand()
        file_to_delete = input("which file you want to delete: ")
        if os.path.exist(file_to_delete):
            file_path = f'E:/python_course/My_project/file manager/{file_to_delete}'
            os.remove(file_path)
            print(f'{file_to_delete} has been successfully deleted.')
            delete_more = input('Do you want delete more files Yes/No: ').lower()
            if delete_more == 'yes':
                delete_file = input("Enter file name to delete: ")
                if os.path.exists(delete_file):
                    file_path_to_delete = f'E:/python_course/My_project/file manager/{delete_file}'
                    os.remove(file_path_to_delete)
                    print(f'{delete_file} has been successfully deleted.')
                    ops()
                else:
                    print(f'ERROR! {delete_file} file is not exist')
                    ops()
            else:
                ops()
        else:
            print(f'ERROR! {file_to_delete} file is not exist')
            ops()


    elif user_want == 5:
        showDemand()
        file_to_read = input('Enter file name to read: ')
        if os.path.exists(file_to_read):
            with open(file_to_read, 'r') as readFile:
                print(readFile.read())
            read_more = input('Does you want read more file Yes/No: ').lower()
            if read_more == 'yes':
                read_file = input('Enter file name to read: ')
                if os.path.exists(read_file):
                    with open(file_to_read, 'r') as readFile_2:
                        print(readFile_2.read())
                    ops()
                else:
                    print(f'ERROR! {read_file} file is not exist')
                    ops()
            else:
                ops()
        else:
            print(f'ERROR! {file_to_read} file is not exist')
            ops()

            
    else:
        showDemand()
        break
