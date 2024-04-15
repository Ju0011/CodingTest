def solution(strings, n):
    #sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
    #sorted = 원본을 변형시키지 않고 정렬된 결과를 리턴함
    #어떤 단어 x의 n번째 글자 기준으로 정렬
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))