import os

folder = "rolex"
parent_path = "/home/sudharsane/python/examples"
path = os.path.join(parent_path, folder)
if not os.path.exists(path):
    os.mkdir(path)

file_path = path + "/.vikram.txt"

file = open(file_path, "w")
file.write("Aramikalangala !!!")


file = open(file_path, "a")
file.write("\nLifetime settlement")

os.remove(file_path)

os.rmdir(path)
