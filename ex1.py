#  write a program to accept user body temperature in farenheit and if is is above 100.2 then display message you have high grade fever and if not display you are normal 

body=int(input('enter body temp'))
if body>=100.2:
    print("you have high grade fever")
else:
    print("you are normal")
