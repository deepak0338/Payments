from collections import OrderedDict as Od


def parse_months(months_string):
    num_to_months = _init_months()
    month_list = []
    months_string = months_string.split(',')
    for v in months_string:
        temp = v.split('-')
        if len(temp) == 1:
            month_list.append(num_to_months[int(temp[0])])
        else:
            start, end = int(temp[0]), int(temp[-1])+1
            for val in range(start, end):
                month_list.append(num_to_months[val])
    return month_list


def _init_months():
    temp = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    months = Od()
    for i in range(1, 13):
        months[i] = temp[i-1]
    return months


def get_months():
    temp = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


if __name__ == '__main__':
    data = input("Enter monthly data:")
    parse_months(data)

