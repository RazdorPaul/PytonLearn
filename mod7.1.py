my_file = open("poem.txt", 'r')
my_list = my_file.readlines()
for i in my_list:
    print(i, end='')
print(end='\n')
my_file.close()