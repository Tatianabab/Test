#1
#константа-переменная, которая не изменяется
A=5.123
# №2
int,str,tuple
# №3
#len выведет последний элемент из списка. Например:
my_list=[1,2,3,4,5,6,7,8,9]
print(len(my_list))
# №4
spisok = [1, 4, 2, 1, 3, 5, 6, 7, 9, 10]
number=spisok[4]
print(number)
# №5
my_list=[1,9,3,4,5]
my_list.pop(1)
my_list.insert(1,2)
print(my_list)
# №6
numbers = [8, 12, 7, 4, 15, 6, 77, 18, 2, 1]
num_ber=[]
for i in numbers:
    if i % 2==0:
        num_ber.append(i)
print(num_ber)
# №7
my_list={'яблоки':'b','груши':'d'}
# №8
a=58
print(f"Груши:{a}")
# №9
my_list = [8, 12, 7, 4, 15, 6, 77, 18, 2, 1]
a=0
while my_list:
    num=my_list.pop(0)
    if num%2!=0:
        a+=num
print(a)
# №10
my_list = [8, 12, 7, 4, 15, 6, 77, 18, 2, 1]
a=my_list.pop(4)
b=str(a+5)
print(b)