def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))       # numbers 배열의 요소들을 str형태로 변환한다.
    numbers.sort(key = lambda x : x*3, reverse=True)      # x값(숫자)를 세 번 곱해서 문자열 길이를 3배로 늘린 값을 기준으로 정렬한다. 이때 비교가 값의 크기로 비교되는 것이 아니라, 앞에서 세 자리까지의 문자의 크기에 따라 정렬된다.
    # ex) 3 => 333과 31 => 313131 이 있으면, 33과 31까지 중에서 3>1인 경우가 발생하므로, 3이 31보다 앞에 정렬된다.
    answer = str(int("".join(numbers)))     # 정답을 문자열로 리턴하라고 한다.
    
    # answer은 다음과 같이도 표현 가능하다.
    # answer = str(int(answer.join(numbers)))   # int()형으로 변환하지 않으면 오류가 발생한다.
    return answer