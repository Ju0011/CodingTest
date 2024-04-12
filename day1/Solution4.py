#해싱
def solution(genres, plays):
    genre_map = dict()

    for i in range(len(genres)):  # // 장르별 플레이 수를 누적해 더합니다.
        if genres[i] not in genre_map:
            genre_map[genres[i]] = 0
        genre_map[genres[i]] += plays[i]

    items = [(-genre_map[genres[i]], -plays[i], i)
             for i in range(len(genres))]
    items.sort()  # 장르 플레이 수(내림차순), 플레이 수(내림차순), 인덱스(오름차순)

    album = []

    last_genre = ''
    count = 0
    for item in items:
        if last_genre == genres[item[2]]:  # 같은 장르가 몇개 들어갔는지 확인
            count += 1
        else:
            count = 1
        last_genre = genres[item[2]]

        if count > 2:  # 같은 장르가 이미 2개 들어갔다면 최종 앨범에 미포함
            continue

        album.append(item[2])

    return album

print(solution(["classic", "pop", "classic", "classic", "pop"],
               [500, 600, 150, 800, 2500]))