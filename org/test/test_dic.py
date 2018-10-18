#coding:utf-8
import unittest

class Test_dic(unittest.TestCase):
    def test_dic(self):
        # 字典是 {} 里面是key:value
        dict = {'a': 1, 'b': 2, 'c': '3'}
        print( dict['b'])
        self.assertEqual(dict['b'],2)
        print(dict)
        #值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
        dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
        #也可如此创建字典：
        dict1 = {'abc': 456}
        dict2 = {'abc': 123, 98.6: 37}
        #访问字典里的值
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        print("dict['Name']: ", dict['Name'])
        print("dict['Age']: ", dict['Age'])
        #如果用字典里没有的键访问数据，会输出错误  KeyError: 'Alice'


        #修改字典--        向字典添加新内容的方法是增加新的键 / 值对，修改或删除已有键 / 值对如下实例
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
        dict['Age'] = 8  # update existing entry
        dict['School'] = "DPS School"  # Add new entry
        print("dict['Age']: ", dict['Age'])
        print("dict['School']: ", dict['School'])

        #删除字典元素 --能删单一的元素也能清空字典，清空只需一项操作 显示删除一个字典用del命令
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

        del dict['Name']  # 删除键是'Name'的条目
        dict.clear()  # 清空词典所有条目
        del dict  # 删除词典
        #但这会引发一个异常，因为用del后字典不再存在 TypeError: 'type' object is unsubscriptable
        #print("dict['Age']: ", dict['Age'])
        #print("dict['School']: ", dict['School'])

        #字典键的特性  字典值可以没有限制地取任何python对象，既可以是标准的对象，也可以是用户定义的，但键不行
        #1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例
        dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
        print("dict['Name']: ", dict['Name'])   #dict['Name']:  Manni

        #2）键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行，如下实例：
       # dict = {['Name']: 'Zara', 'Age': 7}

       #print("dict['Name']: ", dict['Name'])    #会报错 TypeError: list objects are unhashable


        #字典内置函数&方法
        #Python 字典(Dictionary) len() 函数计算字典元素个数，即键的总数。
        dict = {'Name': 'Zara', 'Age': 7}
        print("Length : %d" % len(dict))

        #Python 字典(Dictionary) str() 函数将值转化为适于人阅读的形式，以可打印的字符串表示。
        dict = {'Name': 'Zara', 'Age': 7};
        print("Equivalent String : %s" % str(dict))

        #Python 字典(Dictionary) type() 函数返回输入的变量类型，如果变量是字典就返回字典类型。
        dict = {'Name': 'Zara', 'Age': 7};
        print("Variable Type : %s" % type(dict))

        #Python字典包含了以下内置方法

        #Python 字典(Dictionary) clear() 函数用于删除字典内所有元素。  dict.clear()
        dict = {'Name': 'Zara', 'Age': 7};

        print("Start Len : %d" % len(dict))
        dict.clear()
        print("End Len : %d" % len(dict))

        #Python 字典(Dictionary) copy() 函数返回一个字典的浅复制。
        dict1 = {'Name': 'Zara', 'Age': 7};

        dict2 = dict1.copy()
        print("New Dictinary : %s" % str(dict2))

        #Python 字典 fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值
        #dict.fromkeys(seq[, value])
        #seq -- 字典键值列表。 value -- 可选参数, 设置键序列（seq）的值。
        seq = ('Google', 'Runoob', 'Taobao')

        dict = dict.fromkeys(seq)
        print("新字典为 : %s" % str(dict))

        dict = dict.fromkeys(seq, 10)
        print("新字典为 : %s" % str(dict))

        #Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。 dict.get(key, default=None) key -- 字典中要查找的键。
        #default -- 如果指定键的值不存在时，返回该默认值值。  返回指定键的值，如果值不在字典中返回默认值None。
        dict = {'Name': 'Zara', 'Age': 27}

        print("Value : %s" % dict.get('Age'))
        print("Value : %s" % dict.get('Sex', "Never"))

        #Python 字典(Dictionary) has_key() 函数用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。
        #dict.has_key(key)
        #key -- 要在字典中查找的键。如果键在字典里返回true，否则返回false。
        dict = {'Name': 'Zara', 'Age': 7}

        #print("Value : %s" % dict.has_key('Age'))
        #print("Value : %s" % dict.has_key('Sex'))

        #Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
        dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
        print("字典值 : %s" % dict.items())
        # 遍历字典列表
        for key, values in dict.items():
            print(key, values)


        #Python 字典(Dictionary) keys() 函数以列表返回一个字典所有的键。
        dict = {'Name': 'Zara', 'Age': 7}

        print("Value : %s" % dict.keys())

        #Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值
        #dict.setdefault(key, default=None)  key -- 查找的键值。 default -- 键不存在时，设置的默认键值。
        dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}

        print("Value : %s" % dict.setdefault('runoob', None))
        print("Value : %s" % dict.setdefault('Taobao', '淘宝'))

        #Python 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里。 dict2 -- 添加到指定字典dict里的字典。
        dict = {'Name': 'Zara', 'Age': 7}
        dict2 = {'Sex': 'female'}

        dict.update(dict2)
        print("Value : %s" % dict)

        #Python 字典(Dictionary) values() 函数以列表返回字典中的所有值。
        dict = {'Name': 'Zara', 'Age': 7}

        print("Value : %s" % dict.values())

        #Python 字典 pop() 方法删除字典给定键 key 及对应的值，返回值为被删除的值。key 值必须给出。 否则，返回 default 值。
        site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
        pop_obj = site.pop('name')
        print(pop_obj) # 输出 ：菜鸟教程

        #Python 字典 popitem() 方法随机返回并删除字典中的一对键和值。如果字典已经为空，却调用了此方法，就报出KeyError异常。
        site = {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
        pop_obj = site.popitem()
        print(pop_obj)
        print(site)



