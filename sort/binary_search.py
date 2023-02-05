# https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/all/ALDS1_4_B
# 二分探索問題
# list_Sの中にlist_Tの要素がなんこあるかを計算するプログラム
n = int(input())
list_S = list(map(int, input().split()))
q = int(input())
list_T = list(map(int, input().split()))
def binarySearch(arg:int) -> int:
    min = 0
    max = n
    while min < max:
        mid = (min + max)//2
        if list_S[mid] == arg:
            return mid
        elif list_S[mid] < arg:
            min = mid + 1
        else:
            max = mid
    pass

c = 0
for t in list_T:
    if binarySearch(t) is None:
        pass
    else:
        c +=1
print(c)
# テストケース
#>>>15
#>>>0 0 1 1 2 2 3 3 3 5 6 6 8 9 9
#>>>10
#>>>8 4 6 5 0 2 1 7 9 3
#8
