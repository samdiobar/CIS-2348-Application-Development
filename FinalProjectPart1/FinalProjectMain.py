"""
Name: Samuel Barroso
ID: 1844307
"""

import csv

# Auxiliary Function to format the "GraduationDate" of a student dictionary
# Format is in mm/dd/year
# Returns string
def format_date_string(dictionary):
    date_formatted = dictionary["GraduationDate"].split("/")
    date_formatted[0] = f'{date_formatted[0]:0>2}'
    date_formatted[1] = f'{date_formatted[1]:0>2}'
    return '/'.join(date_formatted)

# Auxiliary Function that sorts a students dictionary in order of the "GraduationDate"
# Returns list
def sort_by_date(dictionary):
    sorted_list = []
    for id in dictionary:
        date = dictionary[id]["GraduationDate"]
        dictionary[id]["GraduationDate"] = format_date_string(dictionary[id])
        if len(sorted_list) == 0:
            sorted_list.append(dictionary[id])
        else:
            changed = False
            for i in range(len(sorted_list)):
                date_temp = sorted_list[i]['GraduationDate']
                if time_greater_than(date_temp, date):
                    format_date_string(dictionary[id])
                    sorted_list.insert(i, dictionary[id])
                    changed = True
                    break
            if not changed:
                sorted_list.append(dictionary[id])
    return sorted_list

# Auxiliary function that converts a student dictionary to a list of students
# List is sorted by a specific key type
# Returns list
def dict_to_sorted_list(dictionary, sort_by):
    new_list = []

    if (sort_by == "GraduationDate"):
        return sort_by_date(dictionary)
    
    for key in dictionary:
        if sort_by == "ID":
            new_list.append(key)
        else:
            new_list.append(dictionary[key][sort_by])
    
    new_list.sort()
    
    for key in dictionary:
        if sort_by == "ID":
            index = new_list.index(key)
        else:
            index = new_list.index(dictionary[key][sort_by])
        new_list[index] = dictionary[key]
        new_list[index].update({"ID": key})
    return new_list

# Global date used for date comparisons
today = "11/12/2023"
# Auxiliary function that allows for comparisons between two dates
# Returns true is date1 is before date2
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

# Students Class stores a dictionary of students and extra functions
# master_dict key is the student id
# master_dict value is a set of Key:Value pairs
# Key:Value pairs include "LastName", "FirstName", "Major", "DA", "GPA", "GraduationDate"
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
    
    # Creates Students dictionary that is organized by major
    def create_by_majors_dict(self):
        by_majors_dict = {}
        for id in self.master_dict:
            major = self.master_dict[id]["Major"]
            try:
                by_majors_dict[major][id] = self.master_dict[id]
            except:
                by_majors_dict[major] = {}
                by_majors_dict[major][id] = self.master_dict[id]
        return by_majors_dict
    
    # Creates Students dictionary that only includes students who have the following requirements:
    #   - gpa > 3.8
    #   - no disciplinary action
    #   - has no disciplinary action
    # Returns dictionary
    def create_elegible_students_dict(self):
        elegible_students_dict = {}
        for id in self.master_dict:
            gpa = float(self.master_dict[id]["GPA"])
            if (gpa <= 3.8):
                continue
            if (self.master_dict[id]["DA"] == "Y"):
                continue
            if (time_greater_than(today, self.master_dict[id]["GraduationDate"])):
                continue
            elegible_students_dict[id] = self.master_dict[id]
            elegible_students_dict[id]['GPA'] = gpa
        return elegible_students_dict
    
    # Creates Students dictionary that only includes students who have disciplinary action
    # Returns Dictionary
    def create_disciplined_students_dict(self):
        disciplined_students_dict = {}
        for id in self.master_dict:
            disciplined = self.master_dict[id]["DA"]
            if (disciplined != "Y"):
                continue
            disciplined_students_dict[id] = self.master_dict[id]
        return disciplined_students_dict

# Writes list of sets into a new file named "FinalProject{file_name}.csv"
# Each row is ordered in order_of_params
def write_list_to_file(file_name, list, order_of_params):
    with open("FinalProject" + file_name + ".csv", 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for item in list:
            ordered_array = []
            for param in order_of_params:
                ordered_array.append(item[param])
            writer.writerow(ordered_array)

# Creates all the necessary dictionaries and lists based on the project requirements
# Writes the data into files based on the project requirements
def output_to_files(students, full_roster, elegible_students, disciplined_students_file_name):
    full_roster_list = dict_to_sorted_list(students.master_dict, "LastName")
    order_of_params = ['ID', 'Major', 'FirstName', 'LastName', 'GPA', 'GraduationDate', 'DA']
    write_list_to_file(full_roster, full_roster_list, order_of_params)

    by_majors_dict = students.create_by_majors_dict()
    order_of_params = ['ID', 'LastName', 'FirstName', 'GraduationDate', 'DA']
    for major in by_majors_dict:
        by_majors_list = dict_to_sorted_list(by_majors_dict[major], "ID")
        write_list_to_file(major, by_majors_list, order_of_params)

    elegible_students_dict = students.create_elegible_students_dict()
    elegible_students_list = dict_to_sorted_list(elegible_students_dict, "GPA")
    elegible_students_list.reverse()
    order_of_params = ['ID', 'LastName', 'FirstName', 'Major', 'GPA']
    write_list_to_file(elegible_students, elegible_students_list, order_of_params)

    disciplined_students_dict = students.create_disciplined_students_dict()
    disciplined_students_list = dict_to_sorted_list(disciplined_students_dict, "GraduationDate")
    order_of_params = ['ID', 'LastName', 'FirstName', 'GraduationDate']
    write_list_to_file(disciplined_students_file_name, disciplined_students_list, order_of_params)

# Main
if __name__ == "__main__":
    student_manager = Students("FinalProjectStudentsMajorsList.csv", "FinalProjectGPAList.csv", "FinalProjectGraduationDatesList.csv")
    output_to_files(student_manager, "FullRoster", "ScholarshipCandidates", "DisciplinedStudents")