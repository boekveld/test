#! /usr/bin/env python3

# 独学プログラマー チャレンジ問題0.fibonacci
# 2019/01/06更新
# 2019/01/03初出

#フィボナッチ数列を表示

def fib(n):
    a, b = 0, 1
    while a <= n:
        print(a)
        a, b = b, b + a

try:
    fib(int(input('整数を入力してください。その数以下のフィボナッチ数列を表示します。')))
except ValueError:
    print('入力が正しくありません。')
