import sys
sys.stdin = open('input.txt')

#  스택 직접 구현해서 풀기

class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.top = -1

    def push(self, num):
        pass

    def pop(self):
        pass


for test in range(1, 11):
    length, word = input().split()
    stack = Stack(length)  # 최악의 경우까지 생각해서

    for char in word:
        if stack.top == -1:
            stack.push(char)
