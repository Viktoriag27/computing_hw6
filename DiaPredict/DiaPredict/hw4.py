##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
from functools import reduce
from geopy.distance import geodesic
import pandas as pd
from datetime import date

def count_simba(strings):
    # Use map to count "Simba" in each string
    simba_counts = map(lambda s: s.count("Simba"), strings)
    # Use reduce to sum up all counts of Simba in each string
    total_simba_count = reduce(lambda a, b: a + b, simba_counts)
    
    return total_simba_count

# Test
# strings = ["Simba and Nala are lions.", 
#            "I laugh in the face of danger.", 
#            "Hakuna matata", 
#            "Timon, Pumba and Simba are friends, but Simba could eat the other two."
# ]

# print(count_simba(strings))  # Output should be 3

# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 


def get_day_month_year(dates):
    # Use map to extract day, month, year from each date
    day_month_year = map(lambda d: {'day': d.day, 'month': d.month, 'year': d.year}, dates)
    
    # Use reduce to accumulate them into a list
    day_month_year_list = reduce(lambda acc, val: acc + [val], day_month_year, [])
    
    # Convert the list into a DataFrame
    df = pd.DataFrame(day_month_year_list)
    
    return df

# Test
# dates = [
#     date(2023, 10, 17), 
#     date(2022, 5, 23), 
#     date(2024, 12, 1)
# ]

# df = get_day_month_year(dates)
# print(df)

# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

def compute_distance(coord_pairs):
    # Use map to calculate the distance between each pair of coordinates
    distances = list(map(lambda pair: geodesic(pair[0], pair[1]).kilometers, coord_pairs))
    
    return distances

# # Test
# coords = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
# distances = compute_distance(coords)
# print(distances)

#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#
def sum_general_int_list(lst):
    total_sum = 0
    # Iterate through each item in the list
    for item in lst:
        # If the item is an integer, add it to the total sum
        if isinstance(item, int):
            total_sum += item
        # If it is a list, recursively call the function on the sublist    
        elif isinstance(item, list):
            total_sum += sum_general_int_list(item)
    
    return total_sum

# Test
# list_1 = [1, [2, [3, 4, [5]]]]
# print(sum_general_int_list(list_1))  # Expected output: 15

# # Test 4
# list_2 = []
# print(sum_general_int_list(list_2))  # Expected output: 0


