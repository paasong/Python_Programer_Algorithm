def solution(n):
    answer = 0
    while(True):
        answer += 1
        if n % answer == 1:
            return answer

print(solution(10))