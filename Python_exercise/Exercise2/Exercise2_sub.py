# -*- coding:utf-8 -*-
"""이번문제에서는문자와숫자가섞여있는여러개의데이터를정렬하는프로그램을작성한다.
<요구사항>
1. 입력파일(data2.txt) 에는영문과숫자가혼합된3~8자리의데이터가여러개있다.
이데이터에는최소1글자이상의숫자가포함되어있다.
2. 각데이터에서숫자만추출한후, 오름차순으로정렬한다. 단, 중복된숫자는제거한다.
예) [‘D5R7V’, ’47RM6’, ‘628E’, ‘5Y7’, ‘VFVZX4CB’] 에서숫자만추출
[57, 476, 628, 57, 4] 을오름차순정렬하고, 중복된숫자를제거
[4, 57, 476, 628]
<작성할파일>
Exercise2_main.py 파일을확인하고, Exercise2_sub.py 파일을완성함
<실행예시>
원데이터: 5개--> 정렬된데이터: 4개
[4, 57, 476, 628]
13
"""
import copy


def mySort(rawList):
    retList = []  # 정렬된 숫자 리스트(중복 제거됨)

    #####  이 부분을 코딩하시오 ####
    # ---------------------------------->

    # 문자 중에서 숫자를 추출한다.
    def toNumber(string):
        numString = ''
        for i in range(0, len(string)):
            if string[i].isdigit():
                numString += string[i]
        return int(numString)

    for i in range(0, len(rawList)):
        retList.append(toNumber(rawList[i]))

    retList = list(set(retList))  # 중복 데이터 제거
    retList.sort()  # 정렬

    # <--------------------------------
    ##########################

    return retList
