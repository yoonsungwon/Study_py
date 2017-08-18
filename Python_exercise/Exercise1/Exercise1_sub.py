# -*- coding:utf-8 -*-
"""
이번문제에서는두숫자사이의합계를구하는프로그램을작성한다.
<요구사항>
1. 입력파일(data1.txt) 을읽어서, 두숫자사이의모든숫자중제시된배수의합계를구하는프로그램을작성한다.
2. 제공된입력파일에는각줄에“시작숫자끝숫자배수” 3개의양의정수가써있다.
3. 제공되는코드를확인하여두숫자사이의배수가모두합산되도록코드를작성한다.
예) 1 100 2 인경우, 1부터100까지의모든정수중에서2의배수의합계인2550을출력
<작성할파일>
Exercise1_main.py 파일을확인하고, Exercise1_sub.py 파일을완성함
<실행예시>
1부터100까지2의배수의합계는2550
100부터1000까지7의배수의합계는70336
100부터1까지2의배수의합계는2550
1234부터78910까지78의배수의합계는39892788
"""


def myCalc(calcList):
    startNum = calcList[0]  # 시작 숫자 예) '1'
    endNum = calcList[1]  # 끝 숫자 예) '100'
    multiple = calcList[2]  # 배수 예) '2'

    retValue = 0  # 계산된 결과값

    #####  이 부분을 코딩하시오 ####
    # ---------------------------------->
    startNum = int(startNum)
    endNum = int(endNum)
    multiple = int(multiple)

    if startNum > endNum:
        startNum, endNum = endNum, startNum
    return_val = [i for i in range(startNum, endNum + 1) if i % multiple == 0]
    retValue = sum(return_val)
    # <--------------------------------
    ##########################

    return retValue
