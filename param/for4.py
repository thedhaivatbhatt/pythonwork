# Write a programe to count total number of even and odd number in list 
numbers=[10,50,9,32,66,71,30,95,12,33,52]

even_count=0
odd_count=0
for i in numbers:
    print(i)
    if i % 2  == 0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
        
print(f"total even number = {even_count}")
print(f"total odd number = {odd_count}")