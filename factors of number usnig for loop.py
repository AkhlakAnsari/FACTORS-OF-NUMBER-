#factors of user input number using for loop
x= int(input('ENTER THE NUMBER:'))
print('FACTORS OF',x,'IS:')
for i in range(1,x+1):
    if x%i==0:
        print(i)
#thanks akhlakansari94@gmail.com