# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 09:57:14 2021

@author: nitac
"""

x={'A001':'小熊軟糖 20元'}
y={'A002':'冰棒 25元'}
z={'A004':'王子麵 10元'}
w={'A006':'汽水 30元'}
b=input('請按a尋找商品')

while b=='a': 
    a=input('請輸入貨號')
    if a=='A001':
        print('A001:小熊軟糖 20元')
    elif a=='A002':
        print('A002:冰棒 25元')
    elif a=='A004':
        print('A004:王子麵 10元')
    elif a=='A006':
        print('A006:汽水 30元')
    else:
        print('沒有這個商品，請重新輸入')
        
        