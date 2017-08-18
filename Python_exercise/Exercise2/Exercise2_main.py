# -*- coding:utf-8 -*-
'''
이 파일은 절대 수정하지 말고, Exercise2_sub.py 파일의 빈 부분을 코딩하시오
'''

from Exercise2_sub import *

if __name__ == '__main__':
    dataList = []  # 원본 데이터 리스트

    fp = open('data2.txt', 'r')
    strList = fp.read().splitlines()
    fp.close()

    lineNum = 1

    for i in range(0, len(strList)):  # 1개 행씩 처리..
        dataList = strList[i].split()

        sortedList = mySort(dataList)

        print('원 데이터 :{} 개 --> 정렬된 데이터 : {} 개'.format(len(dataList), len(sortedList)))
        print(sortedList)

        lineNum += 1
