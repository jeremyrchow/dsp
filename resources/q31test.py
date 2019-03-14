def read_data(filename):
    """Returns a list of lists representing the rows of the csv file data.
    
    Arguments: filename is the name of a csv file (as a string)
    Returns: list of lists of strings, where every line is split into a list of values. 
        ex: ['Arsenal', 38, 26, 9, 3, 79, 36, 87]
    """
    football_data=[]
    file_reader = open(filename,'r')
    for row in file_reader:
        row=row.split(',')
        for column_index, item in enumerate(row):
            #row[column_index] = item.lower()
            if '\n' in item:
                row[column_index]=item.rstrip()
        football_data.append(row)
    return football_data

def get_index_with_min_abs_score_difference(data_list):
    
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals, in terms of absolute value.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """
    goals_scored_index = data_list[0].index('Goals')
    goals_lost_index = data_list[0].index('Goals Allowed')

    lowest_goals_difference = -1
    current_goal_difference = 0
    team_index = 0

    for row_counter, row in enumerate (data_list[1:]):
        current_goal_difference =  abs(int(row[goals_scored_index]) - int(row[goals_lost_index]))
        if lowest_goals_difference == -1:
            lowest_goals_difference = current_goal_difference
            team_index = row_counter
        elif current_goal_difference < lowest_goals_difference:
            lowest_goals_difference = current_goal_difference
            team_index = row_counter 
    return int(team_index+1)


def get_team(index_value, parsed_data):
    """ Returns the team name at a given index.
    
    Arguments: index_value is an integer row index
               parsed_data is the output of `read_data` above
               
    Returns: the team name
    """
    return str(parsed_data[get_index_with_min_abs_score_difference(parsed_data)][0])

##------ COPY THIS

footballTable = read_data('football.csv')
minRow = get_index_with_min_abs_score_difference(footballTable)
print(str(get_team(minRow, footballTable)))
