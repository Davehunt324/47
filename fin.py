#Python program that compares two numbers provided by the user and prints the larger number using if and else.
Num_1= int(input("Enter Number: "))
Num_2= int(input("Enter Number: "))
Num_3= int(input("Enter Number: "))
if Num_1 > Num_2 and Num_1 > Num_3:
    print(f'The first number is greater which is {Num_1}')
elif Num_2 > Num_1 and Num_2 > Num_3:   
    print(f'The Second number is greater which is {Num_2} ')
elif Num_3 > Num_2 and  Num_3 > Num_1:
    print(f'The third number is greater which is {Num_3} ')
    