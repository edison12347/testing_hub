def largest_histogram(histogram):

    def get_rectangle_size(rectangle_size):
        return min(rectangle_size) * len(rectangle_size)

    # Eliminate everything that is not a number
    histogram = list(filter(lambda x: type(x) == int, histogram))

    # Check for one cell wide rectangle
    max_histogram = max(histogram) if max(histogram) > len(histogram) else len(histogram)

    # check the sequence of rectangles
    for index, column_value in enumerate(histogram):
        rectangle = [column_value, ]
        max_rectangle = column_value
        try:
            for j in range(index + 1, len(histogram)):
                rectangle.append(histogram[j])
                if get_rectangle_size(rectangle) > max_rectangle:
                    max_rectangle = get_rectangle_size(rectangle)

                # new_rectangle = rectangle + [histogram[j]]
                # if get_rectangle_size(rectangle) < get_rectangle_size(new_rectangle):
                #     rectangle.append(histogram[j])
                if max_rectangle > max_histogram:
                    max_histogram = get_rectangle_size(rectangle)
                # else:
                #     break
        except IndexError:
            if get_rectangle_size(rectangle) > max_histogram:
                max_histogram = get_rectangle_size(rectangle)

    return max_histogram






# print(largest_histogram([5])) #== 5
#
# print(largest_histogram([5, 3])) #== 6
#
# print(largest_histogram([1, 1, 4, 3, 1])) #== 4Largest_Historam.py:6

print(largest_histogram([1, 6, 6, 6, 4, 6, 8, ])) #== 24
#
# print(largest_histogram([2, 1, 4, 5, 4, 1, 3, 3, 3 ])) #== 12
