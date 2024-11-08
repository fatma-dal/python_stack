def countdown(num):
    return list(range(num, -1, -1))

print(countdown(5))

def print_and_return(num_list):
    print(num_list[0])
    return num_list[1]


print(print_and_return([1, 2]))  



def values_greater_than_second(num_list):
    if len(num_list) < 2:
        return False
    
    second_value = num_list[1]
    new_list = [num for num in num_list if num > second_value]
    
    print(len(new_list))
    return new_list

print(values_greater_than_second([3]))  


def length_and_value(size, value):
    return [value] * size

# Example usage
print(length_and_value(4, 7))  
print(length_and_value(6, 2))  
