#!/usr/bin/env python3
#coding=utf-8

'infix expression 2 postfix expression'

#定义数字和不同优先级的运算符
Num = [str(x) for x in range(10)]
operator = {'+':1, '-':1, '*':2, '/':2}

def in2post(s):
    stack = []      #存放运算符的栈
    result = ''     #存放后缀表达式结果
    for x in s:
        if x in Num:
            result = result + x
            if x == s[-1]:          #最后一个数字的情况
                for m in stack[::-1]:
                    result = result + m
                stack.clear()
        elif x in operator:
            stack.append(x)
            if len(stack) > 1 and '(' not in stack:
                if operator[stack[-1]] > operator[stack[-2]]:       #新运算符优先级为2，上一运算符优先级为1的情况
                    pass
                else:
                    if operator[stack[-1]] == 2:                    #新运算符和上一运算符优先级都是2
                        result = result + stack[-2]
                        stack.pop(-2)
                    else:                                           #新运算符优先级为1
                        for n in stack[:-1][::-1]:
                            result = result + n
                        stack = [stack[-1]]
        elif x == '(':
            stack.append(x)
        elif x == ')':
            y = stack.index('(')
            if x == s[-1]:          #')'是最后一个字符的情况
                stack.pop(y)
                for a in stack[::-1]:
                    result = result + a
                stack.clear()
            else:
                for o in stack[y+1:][::-1]:
                    result = result + o
                stack = stack[:y]
    print(result)

s = input('input the infix pression')
in2post(s)


