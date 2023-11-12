"""
Name: Samuel Barroso
ID: 1844307
"""

import csv

class Students:
    def __init__(self, majors_list, gpa_list, graduation_dates_list):
        self.master_dict = {}
        self.create_master_dict(majors_list, gpa_list, graduation_dates_list)
    
    def create_master_dict(self, majors_list, gpa_list, graduation_dates_list):
        with open(majors_list) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                id = row[0]
                self.master_dict[id] = {"LastName": row[1], "FirstName": row[2], "Major": row[3], "DisciplinaryAction": row[4]}
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
    
    def print_dict(self):
        for key in self.master_dict:
            print(self.master_dict[key])

    def get_full_roster(self):
        last_names_list = []
        for keys in self.master_dict:
            last_names_list.append(self.master_dict[keys]["LastName"])

        last_names_list.sort()

        for key in self.master_dict:
            index = last_names_list.index(self.master_dict[key]["LastName"])
            last_names_list[index] = self.master_dict[key]
            last_names_list[index].update({"ID": key})
        return last_names_list

def write_list_to_file(file_name, list, order_of_params):
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for item in list:
            ordered_array = []
            for param in order_of_params:
                ordered_array.append(item[param])
            writer.writerow(ordered_array)

if __name__ == "__main__":
    student_manager = Students("./Inputs/StudentsMajorsList-3.csv", "./Inputs/GPAList-1.csv", "./Inputs/GraduationDatesList-1.csv")
    full_roster = student_manager.get_full_roster()
    order_of_params = ['ID', 'Major', 'FirstName', 'LastName', 'GPA', 'GraduationDate', 'DisciplinaryAction']
    write_list_to_file("FullRoster.csv", full_roster, order_of_params)