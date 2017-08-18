# -*- coding:utf-8 -*-
"""이번 연습 문제에서는 법인등록번호의 오류검색번호를 생성하는 프로그램을 작성한다.
※ 법인에 대한 등록번호의 구성
1) 법인등록번호는 등기관서별 분류번호 4자리, 법인종류별 분류번호 2자리, 일련번호 6자리 및 오류검색번호 1자리로 구성된다.
2) 일련번호가 6자리 숫자가 아닌 경우, 앞에 숫자 0을 붙여 6자리를 만든다. 예) 일련번호가 1  000001
※ 오류검색번호 산출방식
1) 법인등록번호 앞의 12자리 숫자에 각각 1과 2를 곱하고, 그 값들을 모두 더한다.
예) 등기관서별 분류번호 1101 / 법인종류별 분류번호 11 / 일련번호 006243 인 경우 (110111-006243)
1 1 0 1 1 1 - 0 0 6 2 4 3
X 1 2 1 2 1 2 1 2 1 2 1 2
1 2 0 2 1 2 0 0 6 4 4 6  총합 28
2) 총합을 10으로 나누어 몫과 나머지를 구하고, 10에서 나머지를 뺀 값을 오류검색번호로 한다. 단, 오류검색번호가 10인 경우 ‘0’으로 한다.
예) 28 / 10  몫 2, 나머지 8  10 – 8 = 2  오류검색번호는 2
<요구사항>
입력된 등기관서별 분류번호, 법인종류별 분류번호, 일련번호, 오류검색번호를 이용하여 유효한 법인등록번호인지 확인한다.
<실행 예시>
법인등기번호 110111-0062432은(는) 유효합니다.
"""
def checkErrorNumber(numbers):
    result = False
    companyRegisterNumber = ""

    if len(numbers) != 4:
        return False

    try:
        if len(numbers[2]) != 6:
            companyRegisterNumber = numbers[0] + numbers[1] + '-' + "{0:06}".format(int(numbers[2]))
    except:
        return False

    sum = 0
    mul = 1
    for ch in companyRegisterNumber:
        mul = (mul % 2)
        if ch == '-':
            continue
        sum += int(ch) * mul
        mul += 1
    print sum

    print("법인등기번호 {} 은(는) ".format(companyRegisterNumber))

    return result


if __name__ == '__main__':

    # 파라미터를 바꿔가면서 테스트
    result = checkErrorNumber(["1101", "11", "6243", "8"])

    if result:
        print("유효합니다.")
    else:
        print("유효하지 않습니다.")
