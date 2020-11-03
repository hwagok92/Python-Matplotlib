#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: admin
'''

import matplotlib.pyplot as plt
from matplotlib import font_manager
from pandas.core.frame import DataFrame

###################그래프에 한글처리 하는 법 이건 정해진 코드임################################
font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_location).get_name()
plt.rc('font',family=font_name)
###############################################################################


x1 = [1,2,3,4]
y1 = [3,7,6,4]

x2 = [1,2,3,4]
y2 = [4,6,8,5]

plt.subplot(2,2,1) #2행 2열로 만들어서 1번째 자리에 넣고
plt.plot(x1,y1,'yo-')

plt.subplot(2,2,4) #2행 2열로 만들어서 4번째 자리에 넣어라
# plt.plot(x2,y2,'r.--')
plt.plot(x2,y2,color='green',linestyle='dotted',marker='D')

plt.show()

