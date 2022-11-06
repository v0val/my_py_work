def base_in():
    f = open('facebook.csv', 'a', encoding ='utf-8')
    print('Добавляем данные в базу')
    while True:
        fam = input('введите фамилию ')
        name = input('введите имя ')
        tele = input('введите номер телефона ')
        work = input('введите должность ')
        choi = input("хотите остановить заполнение базы, жмите 'y'?  ")
        if choi == 'y':
            f.writelines(",".join([fam, name, tele, work]))
            break
            f.close()
        else:
            f.writelines(",".join([fam, name, tele, work])+'\n')
    print('заполнение остановлено')
    
