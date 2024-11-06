T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_number = int(input())
    grade = list(map(int, input().split()))
    grade_count = {}
    for i in grade:
        if i in grade_count:
            grade_count[i] += 1
        else:
            grade_count[i] = 1
    freq = grade_count[0]
    for key in grade_count:
        if grade_count[freq] < grade_count[key]:
            freq = key
    print(f"#{test_case} {freq}")
