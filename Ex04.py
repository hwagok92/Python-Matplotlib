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

#차트 비율 설정
slices = [1,2,3,4]

hobbies = ['공부','영화감상','운동','게임']
#앞글자만 써도 색 설정 가능
cols = ['c','m','r','b']

plt.pie(slices,labels=hobbies,colors=cols,shadow=True,startangle=90,
        explode=(0,0.2,0,0),autopct='%.2f%%')

plt.legend(loc=0)
# 0:제일 안겹치는 자리
# 1:우상
# 2:좌상
# 3:좌하
# 4:우하
# 5:오른쪽
# 6:왼쪽
# 7:오른쪽
# 8:아래
# 9:아래
# 9:위
# 10:가운데



plt.show()










