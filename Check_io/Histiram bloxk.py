def largest_histogram(histogram):
    histogram = list(filter(lambda x: type(x) == int, histogram))
    for i in range(len(histogram)):
        max_histo = histogram[i]
        temp_histo = histogram[i]
        try:
            for j in range(i + 1,len(histogram)):  # check histo compare logic
                    if histogram[i] <= histogram[j]:
                        temp_histo += histogram[i]
            if temp_histo < max_histo:
                max_histo = temp_histo
        except IndexError:
            if max_histo < len(histogram):
                max_histo = len(histogram)
    return max_histo







# print(largest_histogram([5])) #== 5

print(largest_histogram([5, 3])) #== 6

print(largest_histogram([1, 1, 4, 1])) #== 4

# print(largest_histogram([5, 2, 4, 6, 6, ])) #== 4

print(largest_histogram([2, 1, 4, 5, 1, 3, 3])) #== 8
