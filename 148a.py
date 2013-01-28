k = map(int,raw_input().split())[0]
l = map(int,raw_input().split())[0]
m = map(int,raw_input().split())[0]
n = map(int,raw_input().split())[0]
d = map(int,raw_input().split())[0]

num_list = list(range(int(d+1)))[1:]
#print num_list
num_list_after_k = filter(lambda x: x%k != 0,num_list)
num_list_after_l = filter(lambda x: x%l != 0,num_list_after_k)
num_list_after_m = filter(lambda x: x%m != 0,num_list_after_l)
num_list_after_n = filter(lambda x: x%n != 0,num_list_after_m)
#print num_list_after_n
print len(num_list) - len(num_list_after_n)
