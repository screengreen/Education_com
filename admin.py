from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class Add_User(StatesGroup):
    welcome = State()
    name = State()
    third = State()
    fourth = State()
    fifth = State()
    sixth = State()



#блок добавления заметки
class Add_Note(StatesGroup):
     Ready_note = State()
     note = State()
     note_kind = State()


# Блок настроек
class Change_config(StatesGroup):
    current_config = State()
    hours = State()
    sub_hours = State()
    technic = State()
    note_section = State()

# блок добавления задачи
class Add_Task(StatesGroup):
    Msg = State()
    duration = State()
    technic_check = State()
    technic = State()

# блок показа записей
class ShowNotes(StatesGroup):
    start_show = State()
    What2show = State()
    note_show = State()

# блок удаления записей
class DeleteNotes(StatesGroup):
    start_del =  State()
    What2del = State()
    delition = State()
    Secdelition = State()

# блок составления расписания
class MakeShedule(StatesGroup):
    hours_count=  State()
    showing = State()