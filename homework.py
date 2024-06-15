# define var for saving user and print it
user="shmulic"
print(user)

#get user from terminal and print it
user=input("please enter your user name")
print(user)

#print hello if the user equal to our name
if user=="shlomi":
    print("hello", user)

#list with 5 names
list=["yossi","shiran","chagit","oliver","poly"]
print(list)

#only if it it is equal to our name:
for i in range(0,len(list)):
    if list[i] == "shlomi":
        print(list[i])
else:
    print("i didnt find any shlomi")

#get the variables from the terminal and put it in a list
list2=[]
list2 = list2.append(input("please enter 5 names"))
if len(list2)<=5: 
    print(list2)
else:
    print("your list is bigger than 5 names")

