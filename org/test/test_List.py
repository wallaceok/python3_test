import operator
import random

#print (str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10)))

L = ['Google', 'Runoob', 'Taobao']
print(L[2])
print(L[-2])
print(L[1:])

# 列表比较函数
list1, list2 = [123, 'xyz'], [456, 'abc']

print(operator.eq(list1, list2))
print(operator.eq(list2, list1))
list3 = list2 + [786]
print(operator.lt(list2, list3))

print(len(list1))


list1, list2 = ['123', 'xyz', 'zara', 'abc'], [456, 700, 200]

print("Max value element : ", max(list1))
print("min value element : ", min(list2))

#list() 方法用于将元组转换为列表。
#注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)

print("列表元素 : ", aList)

#append() 方法用于在列表末尾添加新的对象。
aList = [123, 'xyz', 'zara', 'abc']
aList.append( 2009 )
print ("Updated List : ", aList)

#count() 方法用于统计某个元素在列表中出现的次数。
aList = [123, 'xyz', 'zara', 'abc', 123]

print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))

#extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
aList = [123, 'xyz', 'zara', 'abc', 123]
bList = [2009, 'manni']
aList.extend(bList)

print ("Extended List : ", aList )
#index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
aList = [123, 'xyz', 'zara', 'abc']

print ("Index for xyz : ", aList.index( 'xyz' ))
print ("Index for zara : ", aList.index( 'zara' ))

#insert() 函数用于将指定对象插入列表的指定位置。
aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 3, 2009)

print ("Final List : ", aList)

#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(1)
print ("删除的项为 :", list_pop)
print ("列表现在为 : ", list1)

#remove() 函数用于移除列表中某个值的第一个匹配项。
aList = [123, 'xyz', 'zara', 'abc', 'xyz']

aList.remove('xyz')
print ("List : ", aList)
aList.remove('abc')
print ("List : ", aList)

#reverse() 函数用于反向列表中元素。
aList = [123, 'xyz', 'zara', 'abc', 'xyz']

aList.reverse()
print ("List : ", aList)

#sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
bbList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook']

bbList.sort()
print("List : ", bbList)

#以下实例降序输出列表
# 列表
vowels = ['e', 'a', 'u', 'o', 'i']
# 降序
vowels.sort(reverse=True)

# 输出结果
print ('降序输出:', vowels)

#以下实例演示了通过指定列表中的元素排序来输出列表：
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别 #排序列表：[(4, 1), (2, 2), (1, 3), (3, 4)]
print('排序列表：', random)





