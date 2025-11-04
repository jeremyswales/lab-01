def unique_sorted():
    
    # Ask the user to input numbers separated by spaces
    number = input("Enter numbers separated by spaces: ")

    # Convert the input string into a list of numbers by using split to look each number individually based off a space
    numbers = [float(x) for x in number.split()]

    # Remove duplicates and sort
    sorted_numbers = sorted(set(numbers))

    return sorted_numbers


result = unique_sorted()
print("sorted set", result)

''''''''''''''''''''''''''''''''''''

def cumulative_sum():
    
    # Ask the user for input
    number = input("Enter numbers separated by spaces: ")

    # Convert input into a list of numbers (floats or ints)
    numbers = [float(x) for x in number.split()]

    
    result = []
    total = 0
    for num in numbers:
        total += num
        result.append(total)

    return result
    
print("cumulativesum list is", cumulative_sum() )
 



