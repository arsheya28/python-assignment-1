''' 
python assignment 1
 // ans 24
 '''
'''

def add(num,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("select operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True : 
    choice=input("enter choice(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("enter first no: "))
            num2=float(input("enter second no: "))
        except valueerror:
            print("invalid input")
            continue
        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))
            next_calculation=input("lets do next calculation? (yes/no): ")

            if next_calculation=="no":
                                   break
            
            else:
                                   print("invalid input") 

'''
'''
// ans 26
'''
'''
str="iamarsheya"
print(str.startswith("i"))
print(str.startswith("i",2,8))
print(str.startswith("am",5,8)) 

'''
'''
// ans 27 
'''
'''
string= "orange"
print([*string])  
'''
'''
// ans 1
'''
'''
num1 = 2
num2 = 3
sum = num1 + num2
print(sum)
'''
'''
// ans 2
'''
'''
x=24
if x % 24==0:
print(x,"is even")
else:
print(x,"is odd")
'''
'''
// ans 3
'''
'''
def factorial(n):
    return 1 if (n==1 or n==0) else n*factorial(n-1)
    num=5
    print("factorial of",num,"is",factorial(num)) 

'''
'''
// ans 4
'''
'''
name=input("hello!your name?")
print("hello"+name+"it was nice meeting you")
'''
'''
// ans 5
'''
'''
temp=input("please enter your name!")
try:
    with open('gfg.txt', 'w') as gfg:
except Exception as e:
    print("there is a problem", str(e))

'''
'''
// ans 7
'''
'''
str = "green"
print(len(str))
'''
'''
// ans 8
'''
'''
str_list=['python', 'is', 'fun']
result = ' '.join(str_list)
print(result)
'''
'''
// ans 9
'''
'''
mystring1 = "a friend in need is a friend indeed"
if "need" in mystring1:
    print("yes")
else:
    print("no")
'''
'''
// ans 10
'''
'''
original_text= "list updated"
upper_text= original_text.upper()
print(upper_text)
'''
'''
// ans 11
'''
'''
n=10
num1=0
num2=1
next_number=num2
count=1
while count<=n:
    print(next_number, end=" ")
    count+= 1
    num1, num2=num2, next_number
    next_number=num1 + num2
    print()

'''
'''
// ans 12
'''
'''
def getsum(n):
    strr=str(n)
    list_of_number=list(map(int, strr.strip()))
    return sum(list_of_number)
    n=12345
    print(getsum(n)) 
'''

'''
// ans 13
'''
'''
def age_calculator(current_year,birth_year):
    age=current_year-birth_year
    print("the age is",age,"years")
    age_calculator(2003,2024) 
'''

'''
// ans 14
'''
'''
no_of_lines=5
lines= ""
for i in range(no_of_lines):
    lines+=input()+"\n"
    print(lines) 
'''
'''
// ans 15
'''
'''
import csv
with open('good.csv', mode='r') as file:
    csvFile=csv.reader(file)
    for lines in csvFile:
        print(lines)
'''
'''
// ans 16
'''
'''
test_str="arsheya"
all_freq={}
for i in test_str:
    if i in all_freq[i]:
        all_freq[i]+=1
    else:
        all_freq[i]=1
        print("count of all characters is:\n"+str(all_freq)) 

'''
'''
// ans 17
'''
'''
print("convert to title".title())
'''
'''
// ans 18
'''
'''
inp1= "listen"
inp2= "silent"
x=[inp1[i] for i in range(0,len(inp1))]
x.sort()
y=[inp2[i] for i in range(0,len(inp2))]
y.sort() 
if(x==y):
    print("anagrams")
else:
    print("not anagrams") 
'''
'''
// ans 19
'''
'''
import string
test_str='she, is my, best friend;'
test_str=test_str.translate(str.maketrans('', '', string.punctuation))
print(test_str) 
'''
'''
// ans 20
'''
'''
total=0
list1=[11,5,17,18,23]
for ele in range(0,len(list1)):
    total=total+list1[ele]
    print("sum is", total) 
'''
'''
// ans 21
'''
'''
my_list=[1,2,3,4,5,6,7,8,9,10]
count=my_list.count(5)
print(count)
'''
'''
// ans 22
'''
'''
test_list=[1,2,3,4,5]
print("the original list is: "+str(test_list))
max_all=max(test_list)
min_all=min(test_list)
print("the max of list is: "+str(max_all))
print("the min of list is: "+str(min_all)) 
'''
'''
// ans 23
'''
'''
celsius=int(input("enter temp in celsius :\n"))
farenheit=(1.8*celsius)+32
print("temp in farenheit :\n",farenheit)
'''














































