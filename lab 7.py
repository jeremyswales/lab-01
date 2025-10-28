def rotating_array(size, begin):
    array = []
    for number in range(size):
        number = begin
        array.append(number)
        begin = begin -3
    print(f"orginal array list: {array}")

    even_index = array[::2]
    print(f"even index list: {even_index}")

    even_index = even_index[1:] + even_index[:1]
    print(f"even index list after rotation: {even_index}")

    array[::2] = even_index 
    return array

size=int(input("What size do you want the array list:"))
begin=int(input("What do you want to begin with:"))
print(f"Your array list after rotatio: {rotating_array(size, begin)}")