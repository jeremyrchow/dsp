from collections import Counter
def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.
    
    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    data_list=[]
    file_reader = open(filename,'r')
    for row in file_reader:
        row=row.split(',')
        for column_index, item in enumerate(row):
            row[column_index] = item.lower().rstrip().lstrip()
        data_list.append(row)

    return data_list

def remove_periods(string_with_periods):
    string_with_no_periods = ''
    for char in string_with_periods:
        if char != '.':
            string_with_no_periods += char
    return string_with_no_periods


def find_degrees(data_list_of_lists):
    data_table = read_data(data_list_of_lists)
    list_of_degrees=[]
    phd_index = int(data_table[0].index('degree'))
    tempString= ' '
    for row in data_table[1:]:
        for column_index,item in enumerate(row):
            if column_index == phd_index:
                row[column_index] = remove_periods(item)
                list_of_degrees.append(row[column_index])

    corrected_list_of_degrees=' '.join(list_of_degrees).split()

    return(corrected_list_of_degrees)



def count_degrees(csv_file_name):
    degrees_list=find_degrees(csv_file_name)
    return(Counter(degrees_list))


#---------- RETURN statements    
print('-----------------')
print(count_degrees('faculty.csv'))
