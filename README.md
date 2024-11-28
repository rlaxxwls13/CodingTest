# CodingTest

## 다시 풀어볼 문제
1. D2 달팽이숫자 --> d2인데 너무 오래걸림 코드도 더러운듯..dfs로 풀수있다는데 공부하고 다시 풀어볼 것

## Tip
1. map 객체는 iterator이기 때문에 한 번 사용하면 내부 데이터를 소모하여 다시 사용할 수 없음. 재사용 하려면 list 객체로 변환해야 함
2. 반올림: round(num, (반올림할 자리수)), math.ceil(), math.floor()
3. 빈 리스트에 max 함수를 사용하면 오류가 남
4. 파이썬에는 삼항연산자가 없다. 헐.. (True) if (Condition) else (False) 써야 함
5. 파이썬 리스트 선언: list=[0 for i in range(n)], 이중리스트: list=[[0 for j in range(cols)] for i in range(rows)]
6.''.join(list) : list속 string을 한 문자열로 연결할때 (반대:split())
7.