from bbot import BotDB1
import copy
import markups as nav


def create_scedule(secuin, h=480):


    if h%4 == 0 and h >7*60:
        sec_time = [[round((0.8*h)), 1], [round(0.2*h), 2], [0, 3], [0, 4]]
    else:
        sec_time = [[h, 1], [0, 2], [0, 3], [0, 4]]
    leftover = 0
    tasks = []
    times = []
    task_ids = []
    def each_section(sect):
        nonlocal h, leftover
        sec_time[sect][0] += leftover
        leftover = 0
        for ob in secuin:
            if ob[0] == sec_time[sect][1]:
                if ((sec_time[sect][0] - int(ob[2])) >= 0):
                    sec_time[sect][0] -= int(ob[2])
                    tasks.append(ob[1])
                    times.append(ob[2])
                    task_ids.append(ob[3])

        leftover = copy.copy(sec_time[sect][0])


    each_section(0)
    each_section(1)
    each_section(2)
    each_section(3)
    final_list = [tasks, times, task_ids]
    return final_list

async def showing_tasks(message, user_id):
    for i in [1, 2, 3, 4]:
        if BotDB1.check_section(user_id, i):
            result = BotDB1.get_matrix_section(user_id, i)
            await message.bot.send_message(message.from_user.id,
                                               f'=={BotDB1.get_matrix_section_name(i)[0][0].upper()}==', reply_markup=nav.Main_Menu)
            n = 1
            for f in result:
                l = str(f)
                await message.bot.send_message(message.from_user.id, f"{n}) {l[2:-3:]} ")
                n += 1
def add_duration(message, dur):
    if 'мин' in dur and 'час' in dur:
        ind = dur.find('час')
        hours = dur[:ind]
        hours = ''.join(i for i in hours if not i.isalpha())
        hours = hours.strip()
        minutes = dur[ind:]
        minutes = ''.join(i for i in minutes if not i.isalpha())
        minutes = minutes.strip()
        result = int(minutes) + int(hours) * 60
        BotDB1.add_duration(message.from_user.id, result)

    elif 'мин' in dur:
        dur = ''.join(i for i in dur if not i.isalpha())
        dur.strip()
        BotDB1.add_duration(message.from_user.id, int(dur))

    elif 'час' in dur:
        dur = ''.join(i for i in dur if not i.isalpha())
        dur = dur.replace(',','.')
        dur = dur.strip()
        dur = float(dur)*60
        BotDB1.add_duration(message.from_user.id, int(dur))


async def show_scedule(message, secuin):
    list1 = zip(secuin[0], secuin[1])
    n = 1
    for d in list1:
        await message.bot.send_message(message.from_user.id, f"{n}) {d[0]} - {d[1]} мин")
        n += 1
    BotDB1.insert_active_shedule(message.from_user.id, secuin[2])




