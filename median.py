# Takes a list of numbers and returns its median.


def median(sequence):
    sorted_list = sorted(sequence)
    half_length = len(sorted_list) / 2
    if len(sorted_list) % 2 == 1:
        return sorted_list[int(half_length)]
    elif len(sorted_list) % 2 == 0:
        devided_item_1 = sorted_list[half_length] 
        devided_item_2 = sorted_list[half_length - 1]
        return (devided_item_1 + devided_item_2) / 2.0
         

print median([4, 5, 5, 4])
print median([1,6,7,9,2])