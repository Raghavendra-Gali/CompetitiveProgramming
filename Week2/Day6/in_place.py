import random
import time
def shuffle(the_list):

    # Shuffle the input in place
    i=0
    random_numbers=[]
    start=time.time()
    while i<len(the_list):
        r=random.randint(0,len(the_list)-1)
        if r not in random_numbers:
            random_numbers.append(r)
            i+=1
    print(time.time()-start)
    print(random_numbers)
    final_random_numbers=[]
    the_temp=the_list[:]
    the_list=[]
    print("The temp",the_temp)
    for i in range(len(the_list)):
        r=random_numbers[i]
        the_list.append(the_temp[r])   


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)