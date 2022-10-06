#!/usr/bin/env python 3

szorzandó=5
szorzó=input('Mennyivel szorozam meg az'+ str(szorzandó)+'-öt? ')
print(szorzandó, '-ször ', szorzó,' annyi mint ',sep='',end='')
szorzó=int(szorzó)
print(szorzandó*szorzó)