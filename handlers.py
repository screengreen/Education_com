from aiogram import Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from bbot import BotDB1, dp
from config import *
import markups as nav
import admin
from functions import create_scedule, showing_tasks, add_duration, show_scedule


#------------Идентификация или добавление пользователя----------------
@dp.message_handler(commands=('start'), commands_prefix = "/!")
async def readyNote(message: types.Message, state=None):
    await admin.Add_User.welcome.set()
    result = BotDB1.check_user(message.from_user.id)
    if result:
        await message.bot.send_message(message.from_user.id,
                                       f'Добрый день, {message.from_user.first_name}. Приятно снова тебя увидеть!', reply_markup=nav.Main_Menu)
        await state.finish()
    else:
        BotDB1.add_user(message.from_user.id)
        BotDB1.add_user_status(message.from_user.id)
        await message.bot.send_message(message.from_user.id,
                                       f'Добрый день, {message.from_user.first_name} . Мы еще не знакомы!')
        import time
        time.sleep(1)
        await message.bot.send_message(message.from_user.id, 'Я  буду рад помочь найти тебе товарищей! Но для начала давай заполним твою анкету')
        time.sleep(1)
        await message.bot.send_message(message.from_user.id, 'Как тебя зовут?')

@dp.message_handler(content_types=['text'], state=admin.Add_User.welcome)
async def newNote(message: types.Message, state = FSMContext):
    await admin.Add_User.name.set()
    # проверка имени на разные штуки
    BotDB1.set_column(message.from_user.id, message.text, 'user_name')
    await message.bot.send_message(message.from_user.id, 'Из какого ты университета?')

@dp.message_handler(content_types=['text'], state=admin.Add_User.name)
async def newNote(message: types.Message, state = FSMContext):
    await admin.Add_User.third.set()
    # проверка имени на разные штуки
    BotDB1.set_column(message.from_user.id, int(message.text), 'Institute_id')
    await message.bot.send_message(message.from_user.id, 'Напиши свой город')

@dp.message_handler(content_types=['text'], state=admin.Add_User.third)
async def newNote(message: types.Message, state = FSMContext):
    await admin.Add_User.fourth.set()
    # проверка имени на разные штуки
    BotDB1.set_column(message.from_user.id, int(message.text), 'city_id')
    await message.bot.send_message(message.from_user.id, 'твоя специализация')

@dp.message_handler(content_types=['text'], state=admin.Add_User.fourth)
async def newNote(message: types.Message, state = FSMContext):
    await admin.Add_User.fifth.set()
    # проверка имени на разные штуки
    BotDB1.set_column(message.from_user.id, int(message.text), 'specialization_id')
    await message.bot.send_message(message.from_user.id, 'твои скилы')

@dp.message_handler(content_types=['text'], state=admin.Add_User.fifth)
async def newNote(message: types.Message, state = FSMContext):
    await admin.Add_User.sixth.set()
    # проверка имени на разные штуки
    BotDB1.set_column(message.from_user.id, int(message.text), 'skills_id')
    await state.finish()
    await message.bot.send_message(message.from_user.id, 'Записал', reply_markup=nav.Main_Menu)

@dp.message_handler()
async def readyNote1(message: types.Message):
    if message.text == 'Смотреть анкеты':
        status = BotDB1.get_user_status(message.from_user.id)
        res = BotDB1.get_user_to_show(status)
        BotDB1.change_status(message.from_user.id)
        result = f'вот анкета:\n Имя:{res[0][2]} \n Университет:{res[0][3]}\n Город:{res[0][4]}\n Специализация:3\n Скилы:1'
        await message.bot.send_message(message.from_user.id, result, reply_markup=nav.Main_Menu)




'''
#------------Блок записи заметок----------------
@dp.message_handler(commands=('Заметка'), commands_prefix = "/!", state=None)
async def readyNote(message: types.Message):
    await Add_Note.Ready_note.set()
    await message.bot.send_message(message.from_user.id, 'Записываю:', reply_markup=nav.back_key)

@dp.message_handler(content_types=['text'], state=Add_Note.Ready_note)
async def Note(message: types.Message, state = FSMContext):
    await Add_Note.note.set()
    if message.text == 'Назад':
        await message.bot.send_message(message.from_user.id, 'Возвращаюсь', reply_markup=nav.Main_Menu)
        await state.finish()
    else:
        BotDB1.add_note(message.from_user.id, message.text)
        await message.bot.send_message(message.from_user.id, 'В какую секцию?', reply_markup= nav.kind_of_note_menu)
        @dp.message_handler(content_types=['text'], state=Add_Note.note)
        async def kind_of_Note(message: types.Message, state = FSMContext):
            await Add_Note.note_kind.set()
            dict_1 = {'Вопрос':1, 'Утверждение': 2}
            BotDB1.add_note_kind(message.from_user.id, dict_1[message.text])
            await message.bot.send_message(message.from_user.id, 'Записал', reply_markup=nav.Main_Menu)
            await state.finish()


#------------Блок записи задач----------------
@dp.message_handler(commands=('Задача'), commands_prefix = "/!", state=None)
async def readyNote(message: types.Message):
    await Add_Task.Msg.set()
    await message.bot.send_message(message.from_user.id, 'Записываю:', reply_markup=nav.back_key)


@dp.message_handler(content_types=['text'], state=Add_Task.Msg)
async def newNote(message: types.Message, state = FSMContext):
    await Add_Task.duration.set()
    if message.text == 'Назад':
        await message.bot.send_message(message.from_user.id, 'Возвращаюсь', reply_markup=nav.Main_Menu)
        await state.finish()
    else:
        BotDB1.add_task(message.from_user.id, message.text)
        await message.bot.send_message(message.from_user.id, 'Сколько времени займет задача? (можно указать свое значение )',
                                       reply_markup=nav.duration_menu)


@dp.message_handler(content_types=['text'], state=Add_Task.duration)
async def newNote(message: types.Message, state=FSMContext):
    await Add_Task.technic_check.set()
    add_duration(message, message.text)
    await message.bot.send_message(message.from_user.id, 'Выберите секцию', reply_markup=nav.matrix_menu)
    @ dp.message_handler(content_types=['text'], state=Add_Task.technic_check)
    async def newNote(message: types.Message, state=FSMContext):
        await Add_Task.technic.set()
        dict_id = {'Важн. и срочн.': 1, 'Важн. и несрочн.':2, 'Неважн. и срочн.': 3, 'Неважн. и несрочн.': 4}
        BotDB1.add_section(message.from_user.id, dict_id[message.text])
        await message.bot.send_message(message.from_user.id, 'Записано', reply_markup=nav.Main_Menu)
        await state.finish()


# ---------------  Блок показа записей --------------
@dp.message_handler(commands=('Показать'), commands_prefix = "/!", state=None)
async def Show_notes_and_tasks(message: types.Message):
    await ShowNotes.start_show.set()
    await message.bot.send_message(message.from_user.id, 'Что показать ? ', reply_markup= nav.note_or_task_menu)

@dp.message_handler(content_types=['text'], state=ShowNotes.start_show)
async def what2show(message: types.Message, state = FSMContext):
    await ShowNotes.What2show.set()
    await message.bot.send_message(message.from_user.id, 'Поиск записей')
    if message.text == 'Заметки':
            if BotDB1.check_notes(message.from_user.id):
                await message.bot.send_message(message.from_user.id, 'За какое время показать записи?',
                                               reply_markup=nav.show_duration_menu)
                @dp.message_handler(content_types=['text'], state=ShowNotes.What2show)
                async def note_duration(message: types.Message, state=FSMContext):
                    await ShowNotes.note_show.set()
                    if message.text == 'Показать записи за последние 24 часа':
                        result = BotDB1.show_notes(message.from_user.id, 24)
                        await message.bot.send_message(message.from_user.id, 'Записи за последние 24 часа:' )
                        await message.bot.send_message(message.from_user.id, '+----------------+' )
                        for i in result:
                               l = str(i)
                               await message.bot.send_message(message.from_user.id, l[2:-3:])
                        await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.Main_Menu)

                    if message.text == 'Показать записи за последний месяц':
                        result = BotDB1.show_notes(message.from_user.id, 31)
                        await message.bot.send_message(message.from_user.id, 'Записи за последний месяц:' )
                        await message.bot.send_message(message.from_user.id, '+----------------+' )
                        for i in result:
                               l = str(i)
                               await message.bot.send_message(message.from_user.id, l[2:-3:])
                        await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.Main_Menu)

                    if message.text == 'Показать записи за последнюю неделю':
                        result = BotDB1.show_notes(message.from_user.id, 31)
                        await message.bot.send_message(message.from_user.id, 'Записи за последнюю неделю:' )
                        await message.bot.send_message(message.from_user.id, '+----------------+' )
                        for i in result:
                               l = str(i)
                               await message.bot.send_message(message.from_user.id, l[2:-3:])
                        await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.Main_Menu)

                    if message.text == 'Показать все записи':
                        result = BotDB1.show_notes(message.from_user.id, 0)
                        await message.bot.send_message(message.from_user.id, 'Все записи:' )
                        await message.bot.send_message(message.from_user.id, '+----------------+' )
                        for i in result:
                               l = str(i)
                               await message.bot.send_message(message.from_user.id, l[2:-3:])
                        await message.bot.send_message(message.from_user.id,'+----------------+' , reply_markup=nav.Main_Menu)
                    await state.finish()


            else:
                await message.bot.send_message(message.from_user.id, 'Записи не обнаружены', reply_markup=nav.second_menu)
                await state.finish()

    elif message.text == 'Задачи':
        if BotDB1.check_tasks(message.from_user.id):
            await showing_tasks(message, message.from_user.id)
            await state.finish()
        else:
            await message.bot.send_message(message.from_user.id, 'Записи не обнаружены', reply_markup=nav.second_menu)
            await state.finish()


# блок составления расписания
@dp.message_handler(commands=('Составить_рассписание'), commands_prefix = "/!", state=None)
async def Show_notes_and_tasks(message: types.Message):
    await MakeShedule.hours_count.set()
    await message.bot.send_message(message.from_user.id, 'На сколько часов ? (можно ввести свое целое число) ', reply_markup= nav.shedule_time)

@dp.message_handler(content_types=['text'], state=MakeShedule.hours_count)
async def what2show(message: types.Message, state = FSMContext):
    await MakeShedule.showing.set()
    result = BotDB1.get_task4scedule(message.from_user.id)
    BotDB1.del_active_shedule(message.from_user.id)
    scedule = create_scedule(result, int(message.text)*60)
    await show_scedule(message, scedule)
    await message.bot.send_message(message.from_user.id, 'Удачи !', reply_markup=nav.Main_Menu)
    await state.finish()


#Блок удаления записей
@dp.message_handler(commands=('Удалить'), commands_prefix = "/!", state=None)
async def Show_notes_and_tasks(message: types.Message):
    await DeleteNotes.start_del.set()
    await message.bot.send_message(message.from_user.id, 'Из чего удалить ? ', reply_markup= nav.note_or_task_menu)

@dp.message_handler(content_types=['text'], state=DeleteNotes.start_del)
async def what2show(message: types.Message, state = FSMContext):
    await DeleteNotes.What2del.set()
    if message.text == 'Заметки':
        if BotDB1.check_notes(message.from_user.id):
            BotDB1.del_records(message.from_user.id, 'notes')
            await message.bot.send_message(message.from_user.id, 'Заметки удалены', reply_markup=nav.Main_Menu)
            await state.finish()

        else:
            await message.bot.send_message(message.from_user.id, 'Записи не обнаружены', reply_markup=nav.second_menu)
            await state.finish()

    elif message.text == 'Задачи':
        if BotDB1.check_tasks(message.from_user.id):
            await message.bot.send_message(message.from_user.id, 'Что из этого удалить ?', reply_markup=nav.AllOrShedule)

            @dp.message_handler(content_types=['text'], state=DeleteNotes.What2del)
            async def what2show(message: types.Message, state=FSMContext):
                await DeleteNotes.delition.set()
                if message.text == 'Все записи':
                    BotDB1.del_records(message.from_user.id, 'tasks')
                    await message.bot.send_message(message.from_user.id, 'Задачи удалены',
                                                   reply_markup=nav.Main_Menu)
                    await state.finish()
                else:
                    BotDB1.update_satistics(message.from_user.id)
                    BotDB1.del_records_from_schedule(message.from_user.id)
                    BotDB1.del_active_shedule(message.from_user.id)
                    await message.bot.send_message(message.from_user.id, 'Задачи с последнего расписания удалены',
                                                   reply_markup=nav.Main_Menu)
                    await state.finish()

        else:
            await message.bot.send_message(message.from_user.id, 'Записи не обнаружены', reply_markup=nav.second_menu)
            await state.finish()
    elif message.text == 'Назад':
        await message.bot.send_message(message.from_user.id, 'Возвращаюсь', reply_markup=nav.second_menu)


@dp.message_handler(commands=('Статистика'), commands_prefix = "/!")
async def Show_notes_and_tasks(message: types.Message):
    result = BotDB1.get_task_done(message.from_user.id)
    await message.bot.send_message(message.from_user.id, f'всего выполненно заданий - {result[0][0]} ', reply_markup= nav.second_menu)


@dp.message_handler()
async def ordinary(message: types.Message):
    if message.text == 'Другое':
        await message.bot.send_message(message.from_user.id, 'Переключаюсь', reply_markup= nav.second_menu)
    elif message.text == 'Назад':
        await message.bot.send_message(message.from_user.id, 'Возвращаюсь', reply_markup= nav.Main_Menu)
    else:
        await message.bot.send_message(message.from_user.id, 'не знаю, что и сказать', reply_markup= nav.Main_Menu)
'''