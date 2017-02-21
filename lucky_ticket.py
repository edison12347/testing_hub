MIN_NUMBER = 100000
TOTAL_NUMBER = 999999
#lst = list(map(int, str(TOTAL_NUMBER))
# print(lst)

counter = 0

for number in range(MIN_NUMBER,TOTAL_NUMBER):
    number_split = list(map(int, str(number)))
    if sum(number_split[0:3]) == sum(number_split[3:6]):
        counter += 1

print("number of lucky tickets:", counter)

probability = counter / TOTAL_NUMBER

print("probability:", probability)