import random 

x = [[random.randint(-10,10) for i in range(4)] for i in range(20)]   
unique = set()  
for list in x:  
    for i in range(len(list)):  
        for j in range( i+1, len(list)): 
            pair = tuple(sorted((list[i], list[j])))  
            unique.add(pair) 
print('Множество уникальных комбинаций пар:', unique) 
number = int(input("Введите число: "))
count = 0  
for pair in unique:
    sum = 0  
    for i in pair:   
        sum = sum + i  
    if sum < number:  
        count += 1   
print(f"Количество пар,меньше введенного числа {number}: ", count) 