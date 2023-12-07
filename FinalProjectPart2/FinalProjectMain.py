"""
Name: Samuel Barroso
ID: 1844307
"""

import csv

# param: list (List of strings)
# return: (Boolean): Returns true if the list of strings includes exactly one float value
def has_one_float(list):
    cnt = 0
    for str in list:
        if str == list[-1] and list[-1][-1] == ".":
            str = str[0:-1]
        if (str.replace(".", "").isnumeric() and str.count(".") <= 1):
            cnt += 1
    if cnt == 1:
        return True
    return False
# param: list (List of strings)
# return: (Float): Returns first float value found in list. If no floats found, return 0.0
def get_float(list):
    for str in list:
        if str == list[-1] and list[-1][-1] == ".":
            str = str[0:-1]
        if (str.replace(".", "").isnumeric() and str.count(".") <= 1):
            return float(str)
    return 0.0
# param: date1 (String)
# param: date2 (String)
# return: (Boolean): Returns true if date1 is after date2
today = "12/7/2023"
def time_greater_than(date1, date2):
    date1_arr = date1.split("/")
    date2_arr = date2.split("/")
    if int(date1_arr[2]) > int(date2_arr[2]):
        return True
    elif int(date1_arr[2]) == int(date2_arr[2]):
        if int(date1_arr[0]) > int(date2_arr[0]):
            return True
        elif int(date1_arr[0]) == int(date2_arr[0]):
            if int(date1_arr[1]) > int(date2_arr[1]):
                return True
    return False
# param: student (Student object)
# prints Student object
def print_student(student):
    print(f'{student["ID"]:10}{student["FirstName"]:14}{student["LastName"]:14}{student["GPA"]:7}')

class Students:
    # Class contructor
    def __init__(self, majors_list, gpa_list, graduation_dates_list):
        self.master_dict = {}
        self.create_master_dict(majors_list, gpa_list, graduation_dates_list)
    
    # Reads information from the 3 input files and collects them all into one dictionary
    def create_master_dict(self, majors_list, gpa_list, graduation_dates_list):
        with open(majors_list) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id = row[0]
                self.master_dict[id] = {"LastName": row[1], "FirstName": row[2], "Major": row[3], "DA": row[4]}
        with open(gpa_list) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id = row[0]
                self.master_dict[id].update({"GPA": row[1]})
        with open(graduation_dates_list) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id = row[0]
                self.master_dict[id].update({"GraduationDate": row[1]})

# params: student (Student object)
# manages Student query system
def print_menu(students):
    student_dict = students.master_dict
    # get initial user input
    user_input = input("Provide Student major and GPA: \n")
    print()
    user_input_lower = user_input.lower()
    while user_input != "q":
        # get set of majors from input files
        majors_set = {student_dict[id]["Major"].lower() for id in student_dict}
        # make sure there is exactly one major and exactly one float value in the user input
        if not any(user_input_lower.count(major) == 1 for major in majors_set):
            print("No such student")
        elif not has_one_float(user_input.split(" ")):
            print("No such student")
        # computes logic for finding desired query
        else:
            input_major = ""
            for major in majors_set:
                if major in user_input_lower:
                    input_major = major
            input_gpa = get_float(user_input.split(" "))

            students_under_1 = []
            students_under_25 = []
            student_closest_gpa = None
            for id in student_dict:
                if student_dict[id]["Major"] != input_major.title():
                    continue
                if student_dict[id]["DA"] != "":
                    continue
                if not time_greater_than(today, student_dict[id]["GraduationDate"]):
                    continue
                
                if -0.101 <= float(student_dict[id]["GPA"]) - input_gpa <= 0.101:
                    temp = student_dict[id]
                    temp["ID"] = id
                    students_under_1.append(temp)
                elif -0.251 <= float(student_dict[id]["GPA"]) - input_gpa <= 0.251:
                    temp = student_dict[id]
                    temp["ID"] = id
                    students_under_25.append(temp)
                else:
                    if student_closest_gpa == None:
                        temp = student_dict[id]
                        temp["ID"] = id
                        student_closest_gpa = temp
                    elif abs(float(student_closest_gpa["GPA"]) - input_gpa) > abs(float(student_dict[id]["GPA"]) - input_gpa):
                        temp = student_dict[id]
                        temp["ID"] = id
                        student_closest_gpa = temp

            # print found students
            if len(students_under_1) > 0:
                print("Your student(s):")
                print(f'{"ID":10}{"First Name":14}{"Last Name":14}{"GPA":7}')
                print('-' * 45)
                for student in students_under_1:
                    print_student(student)
                print()
            if len(students_under_25) > 0:
                print("You may also consider:")
                print(f'{"ID":10}{"First Name":14}{"Last Name":14}{"GPA":7}')
                print('-' * 45)
                for student in students_under_25:
                    print_student(student)
                print()
            if len(students_under_1) == 0 and len(students_under_25) == 0 and student_closest_gpa != None:
                print("Your student with desired GPA was not found")
                print("Student with nearest GPA:")
                print(f'{"ID":10}{"First Name":14}{"Last Name":14}{"GPA":7}')
                print('-' * 45)
                print_student(student_closest_gpa)
                print()
            elif len(students_under_1) == 0 and len(students_under_25) == 0:
                print("No such student")

        user_input = input("Provide Student major and GPA (type \'q\' to quit): \n")
        print()
        user_input_lower = user_input.lower()

if __name__ == "__main__":
    students_majors_list = "FinalProjectStudentsMajorsList.csv"
    gpa_list = "FinalProjectGPAList.csv"
    graduation_dates_list = "FinalProjectGraduationDatesList.csv"
    student_manager = Students(students_majors_list, gpa_list, graduation_dates_list)

    print_menu(student_manager)