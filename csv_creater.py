def base_in():
    f = open('facebook.csv', 'a')
    print('Заполняем базу')
    while True:
        fam = input('введите фамилию ')
        name = input('введите имя ')
        tele = input('введите номер телефона ')
        inform = input('введите описание ')
        choi = input("хотите остановить заполнение базы, жмите 'y'?")
        if choi == 'y':
            f.writelines(",".join([fam, name, tele, inform]))
            break
            f.close()
        else:
            f.writelines(",".join([fam, name, tele, inform])+'\n')
    print('заполнение остановлено')
    
