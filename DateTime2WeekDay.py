__author__ = 'Administrator'
import re
str="output_2016.06.26.txt"
x=re.search("output_(?P<Year>\d{4}).(?P<Month>\d{2}).(?P<Day>\d{2})",str)#
Year=int(x.group(1))
y=Year%100
print(y)
C=int(Year/100)
print(C)
m=int(x.group(2))
print(m)
d=int(x.group(3))
print(d)
W=int(C/4)-2*C+y+int(y/4)+int(26*(m+1)/10)+d-1#日期转换成星期天的蔡勒公式
print(W%7)

