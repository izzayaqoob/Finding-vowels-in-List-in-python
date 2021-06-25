list=['apple','bottle','lemon','peach','mango']
count=0
for x in range(0,len(list)):
    for y in list[x]:
        if y=='a' or y=='e' or y=='i' or y=='o' or y=='u':
            count=count+1
print('Number of vowels in list: ',count)
