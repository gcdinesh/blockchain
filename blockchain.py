ipstr = "c a b"
arr = ipstr.split(" ")
arr.sort()

count_arr = []
name_arr = []
ind_arr = []
count = 1
temp_name = arr[0]

for i in range(1,len(arr)):
     if(arr[i] == temp_name):
       count = count + 1
     else:
         name_arr.append(temp_name)
         count_arr.append(count)
         temp_name = arr[i]
         count = 1

name_arr.append(temp_name)
count_arr.append(count)
maxim = count_arr[0]
name = name_arr[0]

for i in range(len(count_arr)):
   if(count_arr[i] > maxim):
       maxim = count_arr[i]
       name = name_arr[i]

  
winner = name + " " +str(maxim)
print(winner)