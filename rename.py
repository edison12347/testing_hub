import os

path = "/home/edison12347/Pictures/Dom_100/"
dir_name = os.path.dirname(path)

dir_list = os.listdir(path)

for dir_ in dir_list:
    print("DIR name:", dir_)
    count = 1
    for filename in os.listdir(path + dir_):
        old_file = os.path.join(path + dir_, filename)
        new_file = os.path.join(path + dir_, "Dom_{}_{:02d}.jpg".format(dir_, count))
        os.rename(old_file, new_file)
        count += 1



