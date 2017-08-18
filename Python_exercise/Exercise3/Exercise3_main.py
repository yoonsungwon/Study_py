# -*- coding:utf-8 -*-
'''
이 파일은 절대 수정하지 말고, Exercise3_sub.py 파일의 빈 부분을 코딩하시오
'''

from Exercise3_sub import *

if __name__ == '__main__':
    inputList = []  # 파일에서 읽어온 값들의 리스트 (문자열)
    rfp = None  # 입력 파일
    res = 0.0  # 문제 조건으로 계산한 평균값

    rfp = open('data3.txt', 'r')
    line = 1
    while True:
        rLine = rfp.readline()
        if rLine == '' or rLine == None:
            break
        inputList = rLine.split()
        res = averageOfList(inputList)
        # print(len(inputList), '개 데이터의 평균값 : %10.2f' % res)
        print("{0} 개 데이터의 평균값 : {1:10.2f}".format(len(inputList), res))
        line += 1
    rfp.close()
