from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


#------Вспомогательные кнопки-------
back = KeyboardButton('Назад')

back_key = ReplyKeyboardMarkup(resize_keyboard=True)
back_key.add(back)

#------главное меню-------
watch_ankets = KeyboardButton('Смотреть анкеты')
make_note = KeyboardButton('/Заметка')
other_btn = KeyboardButton('Другое')

Main_Menu = ReplyKeyboardMarkup(resize_keyboard=True)
Main_Menu.add(watch_ankets)

# -------- второе меню --------------
create_scedule = KeyboardButton('/Составить_рассписание')
statistics = KeyboardButton('/Статистика')
show_text = KeyboardButton('/Показать')
del_text = KeyboardButton('/Удалить')

second_menu = ReplyKeyboardMarkup(resize_keyboard=True)
second_menu.add(  show_text).add(statistics,create_scedule ).add(del_text, back)

#----------------меню да или нет ---------------
yes_btn =  KeyboardButton('Да')
no_btn =  KeyboardButton('Нет')

yes_or_no = ReplyKeyboardMarkup(resize_keyboard=True)
yes_or_no.add(yes_btn,no_btn)

#----------------меню выбора часов работы ---------------
btn_2 = KeyboardButton('2')
btn_4 = KeyboardButton('4')
btn_6 = KeyboardButton('6')
btn_8 = KeyboardButton('8')

hours_menu = ReplyKeyboardMarkup(resize_keyboard=True)
hours_menu.add(btn_2, btn_4, btn_6, btn_8)

#----------------меню настройки конфига ---------------
set_config =  KeyboardButton('Настроить сейчас')
set_config_later =  KeyboardButton('Настроить позже')

first_setup = ReplyKeyboardMarkup(resize_keyboard=True)
first_setup.add(set_config).add(set_config_later)

#----------------меню выбора часов работы ---------------
set_config = KeyboardButton('Настроить')
change_hours = KeyboardButton('Изменить кол-во рабочих часов')

start_set_config_menu = ReplyKeyboardMarkup(resize_keyboard=True)
start_set_config_menu.add(set_config).add(change_hours).add(back)

#----------------меню выбора техники ---------------
matrix_technic = KeyboardButton('Матрица Эйзенхауэра')
no_technic = KeyboardButton('Не использовать технику')

technic_menu = ReplyKeyboardMarkup(resize_keyboard=True)
technic_menu.add(matrix_technic ).add(no_technic).add(back)

#----------------меню выбора техники ---------------
btn_5mn = KeyboardButton('5 мин')
btn_15mn = KeyboardButton('15 мин')
btn_30mn = KeyboardButton('30 мин')
btn_1h = KeyboardButton('1 час')
btn_2h = KeyboardButton('2 часа')
btn_4h = KeyboardButton('4 часа')

duration_menu = ReplyKeyboardMarkup(resize_keyboard=True)
duration_menu.add(btn_5mn, btn_15mn, btn_30mn, btn_1h, btn_2h, btn_4h)

#----------------меню выбора секции ---------------
btn_im_ur = KeyboardButton('Важн. и срочн.')
btn_im_notur = KeyboardButton('Важн. и несрочн.')
btn_notim_ur = KeyboardButton('Неважн. и срочн.')
btn_notim_notur = KeyboardButton('Неважн. и несрочн.')

matrix_menu = ReplyKeyboardMarkup(resize_keyboard=True)
matrix_menu.add(btn_im_ur, btn_im_notur).add(btn_notim_ur, btn_notim_notur)

#----------------меню выбора вида заметки ---------------
btn_question = KeyboardButton('Вопрос')
btn_ordinary = KeyboardButton('Утверждение')

kind_of_note_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kind_of_note_menu.add(btn_question, btn_ordinary)

# меню выбора между заметками и задачами
show_task = KeyboardButton('Задачи')
show_note = KeyboardButton('Заметки')

note_or_task_menu = ReplyKeyboardMarkup(resize_keyboard=True)
note_or_task_menu.add(show_task, show_note).add(back)

# за какое время показывать запими меню
btn_0 = KeyboardButton('Показать все записи')
btn_24 = KeyboardButton('Показать записи за последние 24 часа')
btn_7 = KeyboardButton('Показать записи за последнюю неделю')
btn_31 = KeyboardButton('Показать записи за последний месяц')

show_duration_menu = ReplyKeyboardMarkup(resize_keyboard=True)
show_duration_menu.add(btn_0).add(btn_24).add(btn_7).add(btn_31)

#----------------меню выбора времени расписания ---------------
btn_two = KeyboardButton('2')
btn_four = KeyboardButton('4')
btn_six = KeyboardButton('6')
btn_eight = KeyboardButton('8')

shedule_time = ReplyKeyboardMarkup(resize_keyboard=True)
shedule_time.add(btn_two, btn_four, btn_six, btn_eight)

#----------------меню удаления задач---------------
DelAllTasks =  KeyboardButton('Все записи')
DelLastShedule =  KeyboardButton('Задачи с последнего рассписания')

AllOrShedule = ReplyKeyboardMarkup(resize_keyboard=True)
AllOrShedule.add(DelLastShedule).add(DelAllTasks)

