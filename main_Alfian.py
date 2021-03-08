from getpass import getpass
import game_Mulya
import login_Anthony
import highscore_Anthony

myMenu = []
credentials = login_Anthony.Credentials()
high_score = highscore_Anthony.Highscore()

def menu_utama():     
    print(25 * "=" , "Tebak Angka" , 25 * "=")
    print(63 * "=")
    print("Daftar Menu")
    print("[1] Main")
    print("[2] Daftar")
    print("[3] High Score")
    print("[0] Keluar")
    print(63 * "=")
    opsi = input("Ketik pilihan angka pada daftar menu > ")

    if opsi == '1':
        print('Masukkan Credentials Anda! Maks: 3 kali')
        tries = 3
        while(tries > 0):
            print('Tries remaining:', tries)
            username = input('Username : ').lower()
            password = getpass('Password : ')
            if(credentials.login(username,password)):break
            tries-=1
        if(tries == 0):
            print('Anda gagal sebanyak 3x, kembali ke menu utama')
            menu_kembali()
        score = game_Mulya.play()
        high_score.save(username, score)

    elif opsi == '2':
        print(10*'*'+'Daftar User baru'+10*'*')
        username=input('Daftar Username : ').lower()
        password=getpass('Password : ')
        credentials.daftar(username,password)

    elif opsi == '3':
        high_score.show()

    elif opsi == '0':
      while True:
        opsi_kembali = input('''Apakah Anda ingin keluar dari aplikasi (Y/N)''')
        if opsi_kembali.upper() == 'Y':
          print('Terimakasih. Sampai jumpa :)')
          exit()
        elif opsi_kembali.upper() == 'N':
          print('Anda akan diarahkan ke menu utama')
          menu_utama()
        else :
          print ("Perintah tidak dapat diproses. Pastikan untuk hanya mengetikan huruf \"Y\" atau \"N\" dengan benar")
    else:
        print('ERROR : Pastikan hanya memilih angka pada daftar menu')

    menu_kembali()

def menu_kembali():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu_utama()


menu_utama()
