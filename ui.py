import csv_creater as cr
import csv_view as cv
import csv_slay as sl
import csv_all_view as cav
def select_number():
    # меню выбора, что делать с базой
     select_num = input("Здравствуйте, выберите действия:\n\
          '1' хотите заполнить базу\n\
          '2' прочитать базу построчно\n\
          '3' прочитать всю базу\n\
          '4' очистить базу  ")
     if select_num == '1':
         return cr.base_in()
     if select_num == '2':
         return cv.base_out()
     if select_num == '3':
         return cav.base_out()
     if select_num == '4':
         return sl.base_out()
     if not select_num in {'1','2','3','4'}:
         return print('вы выбрали номер вне диапазона')

