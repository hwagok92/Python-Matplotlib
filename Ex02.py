#-*- coding:utf-8
'''
Created on 2020. 11. 3.

@author: admin
'''

import matplotlib.pyplot as plt
from matplotlib import font_manager

###################그래프에 한글처리 하는 법 이건 정해진 코드임################################
font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_location).get_name()
plt.rc('font',family=font_name)
###############################################################################


siljuk = [25,30,40,35,25,45]
members = ['태연','윤아','웬디','슬기','효리','서현']


# plt.bar(members,siljuk)
# plt.xlabel('회원이름')
# plt.ylabel('실적',rotation=0)

plt.barh(members,siljuk)
plt.xlabel('실적')
plt.ylabel('회원이름',rotation=0)
plt.title('회원별 업무실적')

filename='barGraph.png'

plt.savefig(filename)

plt.show()
