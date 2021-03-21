#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 19:59:02 2021

@author: wushanshan
"""

def toupiaoqi(i,c):
    lunch = []
    toupiao = {}
    xuanxiang = 0
    cishu = 0
    
    while xuanxiang <= i:
        beixuan = input('输入今天想吃什么吧')
        lunch.append(beixuan)
        toupiao[beixuan] = 0
        xuanxiang = xuanxiang+1
    
    while cishu <= c:
        try:
            b = int(input('按照刚才输入顺序来投票吧，你选：'))
            if b <= xuanxiang:
                toupiao[lunch[b-1]] += 1
                cishu = cishu+1
            else:
                print('没有这个选项哦，再选一次吧')
                continue
            if cishu >= 5:
                m = str(input('选好了吗？(是/否)：'))
                if m == '是':
                    break
                else:
                    continue
        except ValueError:
            print('输入的格式不正确，要输入数字哦')
    print('投票结束')
    print(toupiao)
    
    
toupiaoqi(3, 10)
