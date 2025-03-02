
file_name = 'student.csv'
student = []

#loading data from file
def load_data():
    try:    
        with open(file_name,'r') as f:
            for line in f:
                data = line.strip().split(',')
                student.append(data)
    except FileNotFoundError:
         print("File not found!")

#Adding student
def add_student(students):
    try:
        roll_no = int(input("Student Roll_no: "))
        if students == []:
            name = input('Student Name: ').title()
            marks = int(input('Student Marks(1-100): '))
            while True:
                if marks > 100 or marks < 0:
                    print("Invalid Marks!\n")
                    return
            else:
                data = [str(roll_no),str(name),str(marks)]
                student.append(data)
                save(data)
                add_more_student = input('Does you want add more students y/n: ').lower()
                if add_more_student == 'y':
                    add_student(students)
                else:
                    main()

        for i in students:   
            if str(roll_no) == i[0]:
                print("Student already exists.")
                return
        else:       
                name = input('Student Name: ').title()
                marks = int(input('Student Marks(1-100): '))
                while True:
                    if marks > 100 or marks < 0:
                        print("Invalid Marks!\n")
                        return
                    else:
                        data2= [str(roll_no),str(name),str(marks)]
                        student.append(data2)
                        save(data2)
                        add_more_student = input('Does you want add more students y/n: ').lower()
                        if add_more_student == 'y':
                            add_student(students)
                        else:
                            break
    except ValueError:
        print("Invalid Roll_No! Roll_No and Marks should be in NUMBERS.\n")

# saving data to file
def save(data):
    with open(file_name,'a') as f:
        f.writelines(','.join(data)+'\n')

# searching student by Roll NO
def seach_student(student):
    student_roll_no = input('Student Roll_NO: ')
    found = False
    try:
        for i in student:
            if student_roll_no == i[0]:
                print(f'\nRoll_NO:{i[0]}, Name:{i[1]}, Marks:{i[2]}')
                found = True
                break
        if not found:
            print("Student not exits!")
    except ValueError:
        print("Students are not added yet!")

# display all student
def display_all_student(student_list):
    try:
        for students in student_list:
            roll_no = students[0]
            name = students[1]
            marks = students[2]
            print(f'Roll_NO:{roll_no}, Name:{name}, Marks:{marks}')
    except ValueError:
        print("Students are not added yet!")

# Delete student
def delete_student(roll_no, message):
    global student
    student_roll_no = roll_no
    found = False
    try:
        for i in student:
            if student_roll_no == i[0]:
                with open(file_name,'r') as f:
                    lines = f.readlines()
                found = True
                with open(file_name,'w') as f:
                    for line in lines:
                        if not line.startswith(student_roll_no + ","):
                            data = f.write(line)
                            student = [sub for sub in student if student_roll_no not in sub]
        if found == True:
            print(message)                   
        if not found:
            print("Student not exits!")     
    except ValueError:
        print("Students are not added yet!") 
        
#update student data
def updata_student_data(student):
    roll_no = input("Student Roll NO: ")
    found = False
    try:
        for index, i in enumerate(student):
            if roll_no == i[0]:            
                name = input(f'Update Student name {i[1]}: ').title()
                marks = int(input(f'Update student marks {i[2]}: '))
                while True:
                    if 0< marks >100:
                        print("Invalid marks!")
                        break
                    else:
                        i[0] = roll_no
                        i[1] = name
                        i[2] = marks
                        data = [str(roll_no),str(name),str(marks)]
                        found = True
                        student[index] = data
                        break
        if not found:
            print("Student not exits!")      
    except ValueError:
        print("Students are not added yet!")

# Calculating statistics       
def calculate_statistics(student):
    total_marks = 0
    No_student = 0
    try:
        for i in student:
            total_marks += int(i[2])
            No_student +=1
        average = total_marks/ No_student
        marks = [int(marks) for m in student for marks in m[2:]]
        minumum_marks = min(marks)
        maximum_marks = max(marks)
        return f'''\nLowest marks marks: {minumum_marks}
Average marks: {int(average)}
Heighest marks: {maximum_marks}
'''
    except ZeroDivisionError:
        print("Marks are not added yet!")

# Making main function with loop all function
def main():
    global student
    while True:
        print('''\n---------STUDENT DATA MANAGEMENT------
 1.Add student
 2.Update student data
 3.Delete student
 4.Display all student
 5.Search student    
 6.Statistics
 7.Exit
              ''')
        
        user_want= input("What you want: ")
        if user_want == '1':
            add_student(student)
        elif user_want == '2':
            updata_student_data(student)                
        elif user_want == '3':
            roll_no = input("Enter Student Roll_No: ")
            delete_student(roll_no,"Student deleted successfully.")
        elif user_want == '4':
            display_all_student(student)
        elif user_want == '5':
            seach_student(student)
        elif user_want == '6':
            print(calculate_statistics(student))
        else:
            break

if __name__ == '__main__':
    load_data()
    main()
