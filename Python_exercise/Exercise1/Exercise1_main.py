# -*- coding:utf-8 -*-
'''
이 파일은 절대 수정하지 말고, Exercise1_sub.py 파일의 빈 부분을 코딩하시오
'''

from Exercise1_sub import *

if __name__ == '__main__':
    dataList = []  # 데이터 리스트

    fp = open('data1.txt', 'r')
    strList = fp.read().splitlines()  # 모든 행을 한꺼번에 읽어옴. 예) ['1 100 2', '100 1000 7', ~~~~]
    fp.close()

    lineNum = 1

    for i in range(0, len(strList)):  # 1개 행씩 처리..

        dataList = strList[i].split()  # dataList는 숫자, 숫자 , 숫자 형식의 리스트를 가짐. 예) ['1'  '100'  '2']

        result = myCalc(dataList)  # 계산된 결과가 반환됨.

        # print(dataList[0], '부터', dataList[1], '까지', dataList[2], '의 배수의 합계는 ', result)
        print("{} 부터 {} 까지 {} 의 배수의 합계는 {}".format(dataList[0], dataList[1], dataList[2], result))

        lineNum += 1
