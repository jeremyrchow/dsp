import pprint as pp

facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

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
            row[column_index] = item.rstrip()
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
	expanded_name=name_string.split()
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


answer = get_dict()
pp.pprint(answer)
n = 0
print(answer['Feng'])
print(answer.items())
for key, vals in answer.items():
	print(['{key},{val}'.format(key=key, val=','.join(val)) for val in vals])
for key, vals in answer.items():
	print( all('{key},{val}'.format(key=key, val=','.join(val)) in facultycsv for val in vals))
	n+= len(vals)

#for key, vals in answer.items():
   # assert( all('{key},{val}'.format(key=key, val=','.join(val)) in facultycsv for val in vals))
  #  n += len(vals)
print(n)
print(facultycsv.count('\n'))
assert n == facultycsv.count('\n')


