print("Mehal Rashid")
print("18B-063-CS(A)")
print("Assignment #1")
print("Exercise 3.21")



user_lst=[]
for x in range(8):
    a=int(input("Pleasse enter number "+str(x+1)+":"))
    user_lst.append(a)

for a in range(8):
    y = user_lst[a]
    if y%2==0:
        print(y)
