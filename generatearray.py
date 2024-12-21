# opening the file in read mode 
my_file = open("data/words.txt", "r") 
  
# reading the file 
data = my_file.read()  
data_into_list = data.split("\n") 
print(data_into_list) 
with open('out.txt', 'w') as f:
    print(data_into_list, file=f) 

my_file.close() 