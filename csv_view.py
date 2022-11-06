def base_out():
    f = open('facebook.csv', 'r', encoding = 'utf-8')
    print('Смотрим базу')
    while True:
        a = '        '.join(f.readline().split(","))
        print(a)
        choi = input("если не хотите осуществлять просмотр базы, жмите 'y'?")
        if choi == 'y' or a == '' or a == '\n':
            print('просмотр окончен')
            f.close()
            break
        
