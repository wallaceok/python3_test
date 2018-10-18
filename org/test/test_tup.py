#coding:utf-8


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)

print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

#修改元组  --元组中的元素值是不允许修改的，但我们可以对元组进行连接组合

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)


#删除元组 --元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

tup = ('physics', 'chemistry', 1997, 2000)

print(tup)
del tup
print("After deleting tup : ")
#print(tup)    #输出会报错

#元组运算符 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
print(len((1, 2, 3)))  #计算元素个数   3

print((1, 2, 3) + (4, 5, 6)) #	连接 (1, 2, 3, 4, 5, 6)
print(('Hi!',) * 4)  #复制  ('Hi!', 'Hi!', 'Hi!', 'Hi!')

print(3 in (1, 2, 3)) #元素是否存在  	True
for x in (1, 2, 3): print(x)  #迭代

#元组索引，截取  因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素
L = ('spam', 'Spam', 'SPAM!')
print(L[2]) # 	'SPAM!'  读取第三个元素
print(L[-2]) #'Spam'  反向读取，读取倒数第二个元素
print(L[1:])  #('Spam', 'SPAM!')  截取元素

#无关闭分隔符  任意无符号的对象，以逗号隔开，默认为元组，如下实例
print ('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print ("Value of x , y : ", x,y)


#Python 元组 len() 函数计算元组元素个数。  max(tuple)\	min(tuple)\

tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')

print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))

#Python 元组 tuple() 函数将列表转换为元组。
print(tuple([1,2,3,4]))
print(tuple({1:2,3:4}))  #针对字典 会返回字典的key组成的tuple
print(tuple((1,2,3,4)))    #元组会返回元组自身

aList = [123, 'xyz', 'zara', 'abc'];
aTuple = tuple(aList)

print("Tuple elements : ", aTuple)






