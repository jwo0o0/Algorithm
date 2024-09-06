import sys
read = sys.stdin.readline

N = int(read())

# files = { 파일 타입: 개수 }
files = {}
for _ in range(N):
    file, type = read().strip().split(".")
    if (not type in files): # 딕셔너리에 존재하지 않으면 1로 초기화
        files[type] = 1
    else: # 이미 존재하면 +1
        files[type] += 1

# 딕셔너리의 key(파일 타입)를 이름순으로 정렬한 리스트
types = sorted(list(files.keys()))
for type in types:
    print(f"{type} {files[type]}")