#Project: Cuckoo Hashing-Advanced Data Structures
#Author: Vivek Sharma
#Date: 11/15/19

num_list = input("Enter elements for cuckoo hashing").split(',')#this takes input from user and splits individual numbers

hash_location_dict = {}#This stores the hash location slots for individual element.
storage_dict = {}#This is the final table which stores the elements.

table_flag = 0 #Storage table flag 0 for first hash table and 1 for second hash table.

#Initialize the two hash tables and allocate 'x' in each slot of both the tables)
def initialize():
    for cnt in range(len(num_list)):
        first_hash = int(num_list[cnt]) % 11
        second_hash = int((int(num_list[cnt]) / 11) % 11)
        hash_location_dict[num_list[cnt]] = [first_hash,second_hash]
    for i in range(11):
        storage_dict[i] = ['x','x']

def allocate_slot(key,flag):
    table_flag = flag #set the flag to choose the table for element storage
    if(flag == 0):
        #extract the location from storage_dict
        loc = hash_location_dict[key][0]
        print("Location of element ",key," is ",loc)
        if(storage_dict[loc][0] == 'x'):
            print("Slot it empty in table 1, inserting new element ",key)
            storage_dict[loc][0] = key#The slot in table one is empty
        else:
            pushed_element = storage_dict[loc][0]
            print("Collision has occured ",pushed_element," is pushed")
            storage_dict[loc][0] = key
            allocate_slot(pushed_element,1)
    if(flag == 1):#collision
        loc = hash_location_dict[key][1]
        print("Location of element ",key," is ",loc)
        if(storage_dict[loc][1] == 'x'):
            print("Slot it empty in table 2, inserting new element ",key)
            storage_dict[loc][1] = key#The slot in table two is empty
        else:
            pushed_element = storage_dict[loc][1]
            print("Collision has occured ",pushed_element," is pushed")
            storage_dict[loc][1] = key
            allocate_slot(pushed_element,0)

#Welcome to Cuckoo hash function: Main function        
initialize()
print("Pre computed hash location on both tables for each element is ", hash_location_dict)

print("Cuckoo dictionary ",storage_dict)
for cnt in range(len(num_list)):
    allocate_slot(num_list[cnt],0)
    
print("================Final Setting in Tables======================")

for i in range(11):
    print("Slot ",i,storage_dict[i])
