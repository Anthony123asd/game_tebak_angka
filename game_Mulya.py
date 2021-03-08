# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

def play():
    a = random.randint(0,20) #a adalah bilangan random yg akan ditebak
    #print("contoh angka random: ",a)
    score = 100
    b=11 #b adalah angka yg akan ditebak, b=11 inisiasi awal aja
    tebakan_bnr = False
    print("*" * 40)
    print("PERMAINAN TEBAK ANGKA")
    print("*" * 40)
    print("Silahkan menebak angka dari 1-20")
    print("Setiap kali kamu menebak salah, score akan dikurangi 10 poin")
    print("Kalau kamu memasukkan selain angka, kamu akan dipenalti 20 poin ;)")
    while score>0 and b!=a:
        print("Score mu saat ini ", score, "\n")
        try:
            b = int(input("Berapa tebakanmu? "))
            if b==a:
                tebakan_bnr = True
            elif b>a:
                score -= 10
                print("\nKegedean!")
            else:
                score -= 10
                print("\nKekecilan!")
        except ValueError:
            score -= 20
            print("itu bukan angka :(")

    if tebakan_bnr:
        print("yey kamu hebat! scoremu adalah ",score)
        return score
    else:
        print("GAME OVER!! Score : ",score)
        return score