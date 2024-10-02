import sys, heapq
read = sys.stdin.readline 

P1, Y1, S1 = read().split()
P2, Y2, S2 = read().split()
P3, Y3, S3 = read().split()

# 첫 번째 방법
years = [int(Y1) % 100, int(Y2) % 100, int(Y3) % 100]
years.sort()
first_name = ''.join(map(str, years))
print(first_name)

# 두 번째 방법
p_s = [(-int(P1), S1[0]), (-int(P2), S2[0]), (-int(P3), S3[0])]
heapq.heapify(p_s)
second_name = heapq.heappop(p_s)[1] + heapq.heappop(p_s)[1] + heapq.heappop(p_s)[1]
print(second_name)