def base_out():
    f = open('facebook.csv', 'r')
    print('Вся база ')
    a = f.readlines()
    print(*a)
    f.close()
        
