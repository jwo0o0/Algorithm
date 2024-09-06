import sys
read = sys.stdin.readline

N = int(read())
books = {} # books = { 책 제목: 팔린 개수 }

for _ in range(N):
    book = read().strip()
    if (not book in books):
        books[book] = 1
    else:
        books[book] += 1

titles = sorted(list(books.keys()), reverse=True) # 사전 역순으로 정렬된 책의 제목

max, maxTitle = 0, ""
for title in titles:
    if (books[title] >= max): 
        max = books[title]
        maxTitle = title

print(maxTitle)