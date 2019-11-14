import datetime as dt
import months_parser as mp
import pandas as pd
import numpy as np


m_list = ['Name', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
file_path = '/Users/uxas/Fees_details/Organizations/TSTTA_fees.csv'


def read_file(ind_col=None):
    csv_file = pd.read_csv(file_path, index_col=ind_col).copy()
    return csv_file


def write_to_file(file, f_path):
    file.to_csv(f_path, index=False)


def reformat_names(names_list):
    if names_list is []:
        print("List Empty")
        return
    else:
        for i in range(0, len(names_list)):
            names_list[i] = names_list[i].title()


def add_student():
    csv_file = pd.read_csv(file_path).copy()
    ind_val = csv_file.index[-1] + 1
    n_list = []
    names_set = set(csv_file['Name'])
    print("Enter student name(s):")
    while True:
        name = input().rstrip().lstrip().title()
        if name == '-1':
            break
        else:
            n_list.append(name)
    print("Following will be added:{}\n".format(n_list))
    frames_to_be_added = [csv_file]
    for v in n_list:
        if v not in names_set:
            frames_to_be_added.append(pd.DataFrame([[v] + [np.NaN]*12], columns=m_list, index=[ind_val]))
            ind_val += 1
        else:
            print("Not creating duplicate record for", v)
    csv_file = pd.concat(frames_to_be_added)
    csv_file.sort_values(by=['Name'], inplace=True)
    csv_file.to_csv('/Users/uxas/Fees_details/Organizations/Test.csv', index=False)
    view_data(n_list)
    view_data(csv_file)


def fee_update_name_wise():
    help_string = "\nEnter monthly fees details:\nEnter months in the following format\n" \
                  "[1-12] or 1, 2, 3, .. or 1, 2-6, 7,...."
    csv_file = pd.read_csv(file_path).copy(deep=False)
    names_set = set(csv_file['Name'])
    print("Enter list of students for fee updates: ")
    names_list = []
    while True:
        name = input()
        if name == '-1':
            break
        else:
            names_list.append(name)
    val = input("\nEnter value to be assigned to {}:\n".format(names_list)).rstrip().lstrip().title()
    for v in names_list:
        print("Enter details for", v)
        month_list = mp.parse_months(input())
        csv_file.loc[csv_file['Name'] == v, month_list] = val
        csv_file.to_csv(file_path, index=False)
        print("Updated file:\n", csv_file)


def fee_input_month_wise():
    months = m_list[1:]
    col_name = months[dt.datetime.today().month - 1]
    names_list = []
    print("Enter list of entries for the month of {}".format(months[dt.datetime.today().month - 1]))
    while True:
        name = input()
        if name.rstrip().lstrip() == '-1':
            break
        else:
            names_list.append(name.rstrip().lstrip().title())
    csv_file = pd.read_csv('/Users/uxas/Fees_details/TSTTA_fees.csv').copy(deep=False)
    csv_file.set_index('Name', drop=False, inplace=True)
    csv_file.loc[names_list, col_name] = 'Paid'
    csv_file.to_csv(file_path, index=False)


def auto_update():
    months = m_list[1:]
    col_name = months[dt.datetime.today().month - 1]

    csv_file = pd.read_csv(file_path).copy(deep=False)
    csv_file.loc[:, col_name] = 'Pending'
    csv_file.to_csv(file_path, index=False)


def remove_student(name):
    pass


def view_data(x=None):
    if x is None:
        disp_file = read_file()
        print(disp_file)
    else:
        print(x)


if __name__ == '__main__':
    menu = "1. Add student\n2. Update fee details\n3. View Data\n4. Update monthly details"
    print(menu)
    while True:
        choice = input("Enter choice (1 | 2 | 3 | 4):").lstrip().rstrip()
        if choice == '1':
            add_student()
        elif choice == '2':
            fee_update_name_wise()
        elif choice == '3':
            view_data()
        elif choice == '4':
            fee_input_month_wise()
        else:
            print("Quitting program!")
            break

