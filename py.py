# print("I am R N Singh entering in the coding world as an python developer")
# x=int(input("Enter the Name1: "))
# y=int(input("Enter the Name2: "))

# print(x+y)
# name="Ram Naran Singh"
# age=20
# marks=7.5
# Sec="A"
# complex_number="6+8i"
# A=True
# print(type(name))
# print(type(age))
# print(type(marks))
# print(type(Sec))
# print(type(complex_number))
# print(type(A))

# a=int(input('Enter num1: '))
# b=int(input('Enter num2: '))
# sum=a+b
# print(sum)

# a,b=2,'5'
# c=int(b)
# print(a+c)

# side=float(input("Enter the Side of Sq1: "))
# Area=side**2
# print(Area,"meter_Square")

# a=float(input("Enter num1: "))
# b=float(input("Enter num2: "))
# Avg=(a+b)/2
# print(Avg)

# a=int(input("Enter the number1: "))
# b=int(input("Enter the number2: "))
# if(a>=b):
#     print(True)
# else:
#     print(False)

# Name1=input("Enter User 1st Name: ")
# print(len(Name1))

# str="Ram $ Shyam $ $ Mohan"
# dollar_count=str.find('$')
# print("The Occourance of dollar: ",str.find('$'))

# marks=int(input("Enter the marks: "))
# if(marks>=90):
#     Grade='A'
# elif(marks<90 and marks>=80):
#     Grade='B'
# elif(marks<80 and marks>=70):
#     Grade='C'
# elif(marks<70 and marks>=60):
#     Grade='D'
# else:
#     Grade='Low Grade'
# print(Grade)

# n=int(input("Enter the number entered by the user: "))
# if(n%2==0):
#     print("Even")
# else:
#     print("ODD")

# x=int(input("Enter the Num1: "))
# y=int(input("Enter the Num2: "))
# z=int(input("Enter the Num3: "))
# if(x>y and x>z):
#     Greatest_number= x
# elif(y>x and y>z):
#     Greatest_number= y
# else:
#     Greatest_number= z
# print("Greatest number is: ",Greatest_number)

# num=int(input("Enter the number: "))
# if(num%7==0):
#     print("Give number is multiple of 7")
# else:
#     print("Not a multiple of 7")

# str1=input("Enter the movie1: ")
# str2=input("Enter the movie2: ")
# str3=input("Enter the movie3: ")
# list=[str1, str2, str3]
# print(list)

# list1=[1,2,3, 'ADA',3, 2,1]
# list2=list1.copy()
# list2.reverse()
# if(list1==list2):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# tup=('A','B','A','D','A','F')
# n=tup.count('A')
# print("Number of students with the “A” grade in the following tuple: ",n)

# list=['A','B','A','D','A','F']
# list.sort()
# print("Sorted list: ",list)

# dict={
#     "table" : "a piece of furniture",
# "Paintings": "list of facts & figures",
# "cat" : "a small animal"
# }
# Mydict=dict.items()
# print(Mydict)

# subjects=["python","java","C++","python","javascript","java","python","java","C++","C"]
# unique_subjects=set(subjects)
# classroom_needed=len(unique_subjects)
# print("unique_subjects: ",unique_subjects)
# print("classroom_needed: ", classroom_needed)

# marks={}
# x=int(input("Enter phy: "))
# marks.update({"phy": x})
# x=int(input("Enter chem: "))
# marks.update({"chem": x})
# x=int(input("Enter maths: "))
# marks.update({"maths": x})
# print(marks)

# values={
#     ("float", 9.0),
#     ("int", 9)
# }
# print(values)

# i=1
# while i<=100:
#     print(i)
#     i+=1

# i=100
# while i>=1:
#     print(i)
#     i-=1

# n=int(input("Enter a Table Number: "))
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# i=1
# while i<=10:
#     print(i**2)
#     i+=1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i=0
# while i< len(nums):
#     print(nums[i])
#     i +=1

# nums = (1,4,9,16,25,36,49,64,81,100)
# i=0
# x=36
# while i< len(nums):
#     if nums[i]==x:
#         print("INDEX FOUND at", i)
#     i+=1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i=0
# for i in nums:
#     print(i)
#     i+=1

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i=0
# x=int(input("Enter the number to be found: "))
# for el in nums:
#     if el==x:
#         print("Number found in list at the index of ",i)
#     i+=1
    
# for el in range(1 ,101):
#     print(el)

# for el in range(100 ,0, -1):
# #     print(el)

# n=int(input("Enter the Table number: "))
# for i in range(1,11,1):
#     print(n*i)

# n=int(input("Enter the numbers: "))
# sum=0
# i=1
# while i <=n:
#     sum+=i
#     i+=1
# print("Sum of n numbers: ",sum)

# n=int(input("Enter the number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("Factorial of given number: ",fact)
    
# def length(b):
#     b=[9,8,7,6,"Ram"]
#     return b
# print(len(length([9,8,7,6,"Ram"])))

# def list(my_list):
#     print(*my_list)   
# my_list=[1,2,3,4,5,6]
# print(my_list)

# def cal_fact(n):
#     fact= 1
#     for i in range(1, n+1):
#         fact*=1
#     print(fact)
# cal_fact(6)

# n=int(input("Enter the Given number: "))
# fact=1
# for i in range(1, n+1):
#     fact=fact*i
#     i+=1
# print(fact)

# a= float(input("Enter num1: "))
# b= float(input("Enter num1: "))
# op=input("Enter operators (+,-,*,/): ")
# if op == '+':
#     print(a + b)

# elif op == '-':
#     print(a - b)

# elif op == '*':
#     print(a * b)

# elif op == '/':
#     print(a / b)

# else:
#     print("Invalid operator")

# arr=[1,'Ram',4,6,7,'Diya']
# n=len(arr)
# for i in range (n):
#     min_index=i
# for j in range(i+1,n):
#     if arr[j]<min_index:
#         min_index=j
# arr[i],arr[min_index]=arr[min_index],arr[i]
# print(arr)

# arr=[1,2,4,6,9,2,1]
# n=len(arr)
# for i in range(1,n):
#     temp=arr[i]
#     j=i
# while j>0 and arr[j-1]>temp:
#     arr[j]=arr[j-1]
#     j=j-1
#     arr[j]=temp
# print("Sorted array: ",arr)

# arr=[1,2,3,4,5]
# n=len(arr)
# key=int(input("Enter the key to be searched: "))
# for i in range(n):
#     if arr[i]==key:
#         print("Element found at index",i)
#         break
# else:
#     print("Not found")

# arr=[1,2,3,4,5,6,7,8,9]
# n=len(arr)
# key=int(input("Enter the key to be searched: "))
# low=0
# high=n-1
# while low<=high:
#     mid=(low+high)//2
#     if arr[mid]==key:
#         print("found at index",mid)
#         break
#     elif key<arr[mid]:
#         high=mid-1
#     else:
#         low=mid+1
# else:
#     print("Not found")        

# import numpy as np
# a=np.arr([[1,2,3],[4,5,6]])
# print(a)
# b=np.arr([10,20])
# print(b)
# x=np.linalg.solve(a,b)
# print(x)

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from scipy import stats

# print("NumPy:", np.__version__)
# print("Pandas:", pd.__version__)
# print("Matplotlib:", plt.matplotlib.__version__)
# print("Scikit-learn imported successfully")
# print("SciPy:", stats.__version__ if hasattr(stats, "__version__") else "Imported successfully")

# import pandas as pd
# data = {
#     "Name": ["Ram", "Amit", "Riya"],
#     "Age": [21, 22, 20]
# }
# df = pd.DataFrame(data)
# print(df)

# import numpy as np
# a=np.array([[1,5,3],[4,8,6],[7,2,9]])
# print(a)
# b=np.array([10,20,30])
# print(b)
# x=np.linalg.solve(a, b)
# print(x)

# import numpy as np

# a = np.array([[1, 2, 3],
#               [2, 5, 3],
#               [1, 0, 8]])

# b = np.array([10, 18, 12])

# x = np.linalg.solve(a, b)

# print(x)

# def list(lst=[1,2,3,4,5,'RamNarayanSingh']):
#     length=len(lst)
#     return length
# print(list())    

# def list(lst):
#     for items in lst:
#         print(items, end='')
# numbers = [10,20,30,40,50 ,'Ram']
# list(numbers)

# def list(lst):
#     for items in lst:
#         print(items, end='')
# lst=[10,20,30,40,50 ,'Ram']
# list(lst)

# def list(lst):
#      print(*lst)
# lst=[10,20,30,40,50 ,'Ram']
# list(lst)

# def factorial(n):
#     fact=1
#     i=1
#     while(i<=n):
#         fact=fact*i
#         i+=1
#     return fact
# print(factorial(5))

# n=int(input("Enter the Given number: "))
# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact*=i
#     return fact
# print(factorial(n))

# Amount=float(input("Enter Dhiram Value: "))   
# def usd_to_inr(Dhiram):
#     INR=Dhiram*30
#     return INR
# print("Amount in INR: ",usd_to_inr(Amount)) 

# n=int(input("Enter the given number which sum to be calculated: "))
# def sum_of_numbers(n):
#     if n<=0:
#         return 0
#     total=0
#     while(n>0):
#         total+=n
#         n-=1
#     print(total)
# print(sum_of_numbers(n))

# def list(lst,index=0):
#     if index==len(lst):
#         return
#     print(lst[index],end='')
#     list(lst,index+1)
# numbers=[10,20,30,40,50]
# print(list(numbers))

# f=open("demo.txt","r")
# data=f.read()
# new_data=data.replace("Java","Python")
# print(new_data)
# print(data)
# print(type(data))
# f.close

# f=open("demo.txt","r+")
# f.write("\nI am a programmer")
# f.close()

# word="xlearning"
# with open("demo.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("Found")
#     else:
#         print("False")

# def check_for_word():
#     word="xlearning"
#     with open("demo.txt","r") as f:
#      data=f.read()
#     if(data.find(word)!=-1):
#         print("Found")
#     else:
#         print("False")
# check_for_word()

# class student:
#     name="Ashi Kumari"
# s1=student()
# print(s1.name)

# class Student:
#     def __init__(self,name,marksS1,marksS2,marksS3):
#         self.name= name
#         self.marksS1=marksS1
#         self.marksS2=marksS2
#         self.marksS3=marksS3
#     def print_average(self):
#         Average=(self.marksS1+self.marksS2+self.marksS3)/3
#         print("Name: ",self.name)
#         print("Average of marks: ",Average)
#     s1 = Student("Ram",50,60,70)
#     s1.print_average()

# class Student:
#     # Constructor
#     def __init__(self, name, mark1, mark2, mark3):
#         self.name = name
#         self.mark1 = mark1
#         self.mark2 = mark2
#         self.mark3 = mark3
#     # Method to print average
#     def print_average(self):
#         average = (self.mark1 + self.mark2 + self.mark3) / 3
#         print("Student Name:", self.name)
#         print("Average Marks:", average)
# name=input("Enter your name: ")
# mark1=float(input("Marks1: "))
# mark2=float(input("Marks2: "))
# mark3=float(input("Marks3: "))
# # Creating an object
# student1 = Student(name,mark1,mark2,mark3)
# # Calling the method
# student1.print_average()

# class Student:
#     def __init__(self,name):
#         self.name = name
# def hello(self):
#     print("hello",self.name)
# s1= Student("Ram")
# s1.hello()

# class Account:
#     def __init__(self,account_no,balance):
#         self.account_no=account_no
#         self.balance=balance
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"{amount} credited successful" )
#     def debit(self,amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"₹{amount} debited successfully.")
#         else:
#             print("Insufficient balance!")
#     def print_balance(self):
#         print("Account No. : ",self.account_no)
#         print("current Balance: ",self.balance)
# account_no=int(input("Enter User Account No. : "))
# balance=int(input("Enter User Balance : "))
# acc1= Account(account_no, balance)
# acc1.print_balance()
# credit_amount=int(input("Enter the credit Amount: "))
# acc1.credit(credit_amount)
# acc1.print_balance()
# debit_amount=int(input("Enter the debit Amount: "))
# acc1.debit(debit_amount)
# acc1.print_balance()
