from random import choice
import math
import numpy as np
import sys
rows = 13 
cols = 13 
array_2d = np.zeros((rows, cols), dtype=int)
min_result = {}
# Diện tích của từng department
department_areas = {
    1: [3.2, 47.6, 160],
    2: [3.2, 47.6, 160],
    3: [3.2, 47.6, 160],
    4: [3.2, 34.3, 110],
    5: [3.2, 29.2, 100],
    6: [3.2, 18.4, 60],
    7: [3.2, 13.3, 50],
    8: [14.6, 40.7, 600],
    9: [8.3, 40.7, 340],
    10: [4.3, 40.7, 180],
    11: [1.9, 40.7, 80],
    12: [3.5, 47.6, 170],
    13: [3.5, 47.6, 170]
}
data_dict = {
    'DCS_paths': 45555,
    'SHC_paths': 27360,
    'TABLETOP_paths': 912,
    'MOBILE_paths': 21782,
    'DESKTOP_paths': 4470
}


def caculate_traveling_distance():
    for key, value in paths.items():
        coordinate_counts = {}
        val = data_dict[key]
        # print(val)
        for path in value:
            for i in range(len(path) - 1):
                if key == "SHC_paths": 
                    if path[i+1] == 12 or path[i+1] == 11 : 
                        array_2d[(path[i] - 1) , (path[i+1] - 1)] = math.ceil(((val / 100) / 4) / 2 )
                        coordinate_counts[(path[i], path[i+1])] = 0
                    else:  
                        if (path[i], path[i+1]) not in coordinate_counts:  
                            if array_2d[(path[i] - 1) , (path[i+1] - 1)] != 0:
                                array_2d[(path[i] - 1) , (path[i+1] - 1)] += math.ceil((val / 100) / 4 )
                                coordinate_counts[(path[i], path[i+1])] = 0
                            else:
                                array_2d[(path[i] - 1) , (path[i+1] - 1)] = math.ceil((val / 100) / 4 )
                                coordinate_counts[(path[i], path[i+1])] = 0
                else :    
                    if (path[i], path[i+1]) not in coordinate_counts:  
                        if array_2d[(path[i] - 1) , (path[i+1] - 1)] != 0:
                            array_2d[(path[i] - 1) , (path[i+1] - 1)] += math.ceil((val / 100) / 4 )
                            coordinate_counts[(path[i], path[i+1])] = 0
                        else:
                            array_2d[(path[i] - 1) , (path[i+1] - 1)] = math.ceil((val / 100) / 4 )
                            coordinate_counts[(path[i], path[i+1])] = 0
        coordinate_counts.clear()
    return array_2d



# Các đường di chuyển qua các department của sản phẩm
paths = {
    "DCS_paths" : [[1, 5, 7, 13], [2, 5, 7, 13], [3, 5, 7, 13], [4, 5, 7, 13]] , 
    "SHC_paths" : [[1, 5, 7, 11], [1, 5, 7, 12], [2, 5, 7, 11], [2, 5, 7, 12], [3, 5, 7, 11], [3, 5, 7, 12], [4, 5, 7, 11], [4, 5, 7, 12]] ,
    "DESKTOP_paths" : [[1, 6, 7, 10], [2, 6, 7, 10], [3, 6, 7, 10], [4, 6, 7, 10]] , 
    "TABLETOP_paths" : [[1, 6, 7, 8], [2, 6, 7, 8], [3, 6, 7, 8], [4, 6, 7, 8]] , 
    "MOBILE_paths" : [[1, 6, 7, 9], [2, 6, 7, 9], [3, 6, 7, 9], [4, 6, 7, 9]]
}

check_range = list(range(1 , 14 ))
options = []
my_dict = {}
 
# Tìm department tiếp theo dựa trên các quy tắc đã cho
def find_next_department(array2d):
    if len(options) > 0 : 
        options.clear()
    while True : 
    # Tạo một danh sách các department
        departments = list(range(1, 14))

    # Chọn department đầu tiên ngẫu nhiên
        last_department = choice(departments)
        if last_department in check_range : 
            print(array2d)
            options.append(last_department)
            departments.remove(last_department)
            print(array2d[3][4])
            while len(departments) > 0:
                for i in range(0, 13):
                    if array2d[last_department - 1][i] > 150:
                        if (i + 1) in departments : 
                            my_dict[i + 1] = array2d[last_department - 1][i]
                        else : 
                            pass
                    elif array2d[last_department - 1][i] > 100 and array2d[last_department - 1][i] <= 150:
                        if (i + 1) in departments : 
                            my_dict[i + 1] = array2d[last_department - 1][i]
                        else : 
                            pass
                    elif array2d[last_department - 1][i] > 50 and array2d[last_department - 1][i] <= 100:
                        if (i + 1) in departments : 
                            my_dict[i + 1] = array2d[last_department - 1][i]
                        else : 
                            pass
                    elif array2d[last_department - 1][i] > 15 and array2d[last_department - 1][i] <= 50:
                        if (i + 1) in departments : 
                            my_dict[i + 1] = array2d[last_department - 1][i]
                        else : 
                            pass
                    elif array2d[last_department - 1][i] > 0 and array2d[last_department - 1][i] <= 15:
                        if (i + 1) in departments : 
                            my_dict[i + 1] = array2d[last_department - 1][i]
                        else : 
                            pass
                    else :
                        pass 
                if my_dict:
                    max_department = max(my_dict, key=my_dict.get)
                    options.append(max_department)
                    last_department = max_department
                    departments.remove(max_department)
                    my_dict.clear()
                else:
                    random_number = choice(departments)
                    options.append(random_number)
                    last_department = random_number
                    departments.remove(random_number)
            check_range.remove(options[0])
            break 
        else : 
            pass 
    return options 

# using loop 

# total_material_cost = 0
# for path , value in paths.items():
#     for p in value :
#         total_material_cost += calculate_material_traveling_distance(p)

# Khoảng cách giữa hai department
def distance(department1, department2):
    width_diff = ( department_areas[department1][0] / 2 ) -  ( department_areas[department2][0] /2 )
    length_diff = ( department_areas[department1][1] / 2 ) - ( department_areas[department2][1] / 2 )
    return math.sqrt(width_diff**2 + length_diff**2)


def calculate_material_traveling_distance(array2d):
    total_distance = 0
    path = find_next_department(array2d)
    for i in range(len(path) - 1):
        total_distance += distance(path[i], path[i+1])
    
    return total_distance * 100 , path 



# In kết quả
# total_material_cost , path  = calculate_material_traveling_distance()
# print("Total material cost:")
# print(total_material_cost)
# print(f"path {path}")
array2d = caculate_traveling_distance()

total_min = sys.maxsize
run = list(range(1, 14))
while True : 
    if len(check_range) > 0 : 
        total_material_cost, path = calculate_material_traveling_distance(array2d)
        print(total_material_cost)
        print(path)
        min_result[total_material_cost] = path[:]  
    else :
        break 

# while True:
#     if check:
#         total_material_cost, path = calculate_material_traveling_distance(array2d)
#         print(total_material_cost)
#         print(path)
#         min_result[total_material_cost] = path[:]  
#         check = False
#     roll = input("Press Y to roll, enter X to exit and print results:  \n")
#     if roll.lower() == "x":  
#         break 
#     if roll.lower() == "y":
#         total_material_cost, path = calculate_material_traveling_distance(array2d)
#         print(total_material_cost) 
#         print(path) 
#         min_result[total_material_cost] = path[:] 

print(min_result)
for result , path in min_result.items():
    
    if(result < total_min) : 
        total_min = result

print(total_min)
value = min_result[total_min]
print(value)

