import pprint as pp

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
            row[column_index] = item.rstrip().lstrip()
        data_list.append(row)
    return data_list


def find_column_values(data_list_of_lists,col_name):
    data_table = (data_list_of_lists)
    list_of_col_values=[]
    desired_col_index = int(data_table[0].index(col_name))
    for row in data_table[1:]:
        for column_index,item in enumerate(row):
            if column_index == desired_col_index:
                list_of_col_values.append(row[column_index])

    return(list_of_col_values)
def find_row_values(data_list_of_lists):
	data_table = read_data
	for row in data_list_of_lists:
		return

def find_last_name(name_string):
	expanded_name=name_string.split(" ")
	last_name = expanded_name[-1]
	return last_name

def get_dict():
	last_name_dict=dict()
	data_table= read_data('faculty.csv')
	name_column=find_column_values(data_table,'name')
	last_names=[find_last_name(name) for name in name_column]
	print('last names column length')
	print(len(last_names))
	for index,name in enumerate(last_names):
		if name in last_name_dict:
			last_name_dict[name].append(data_table[index+1][1:])
		else:
			last_name_dict[name] = data_table[index+1][1:]
	return last_name_dict

#----- test statement


my_dict=get_dict()
pp.pprint(my_dict)
print(len(my_dict))
print(len(read_data('faculty.csv')))
print(my_dict['Li'])
