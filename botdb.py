import sqlite3


class BotDB:
    
    def __init__(self, db_file):
        self.conn= sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def add_user_status(self, user_id):
        result = self.cursor.execute(f"INSERT INTO `check_status` (`user_id`, `status`) SELECT `id`, 1 FROM `users` WHERE `user_telegram_id` = (?)", (str(user_id),))
        return self.conn.commit()

    def fetch_user_id(self, user_id):
        result = self.cursor.execute(f"SELECT user_id FROM `users` WHERE `user_telegram_id` = (?) ", (str(user_id),))
        res = result.fetchall()
        return str(res[0])[1]

    def get_user_status(self, user_id):
        result = self.cursor.execute(f"SELECT status FROM `check_status` WHERE `user_id` = (SELECT user_id FROM users WHERE user_telegram_id = (?)) ", (str(user_id),))
        res = result.fetchall()
        return str(res[0])[1]

    def get_user_to_show(self, status):
        result = self.cursor.execute( f"SELECT * FROM `users` WHERE `id` =  (?) ",(status,))
        res = result.fetchall()
        return res

    def change_status(self, user_id):
        self.cursor.execute(f"UPDATE check_status SET status = IIF(status = (SELECT MAX(id) FROM users), 1, status +1) WHERE `user_id` = (SELECT user_id FROM users WHERE user_telegram_id = (?))",(str(user_id),))
        return self.conn.commit()

    def check_user(self, user_id):
        result = self.cursor.execute(f"SELECT * FROM `users` WHERE `user_telegram_id` = (?) ", (str(user_id),))
        return result.fetchall()

    def set_column (self, user_id, name, column_name):
        self.cursor.execute(f"UPDATE users SET {column_name} = (?) WHERE `user_telegram_id` = (?)", (str(name) , str(user_id),))
        return self.conn.commit()

    def add_user(self,user_id):
        self.cursor.execute("INSERT INTO `users` (`user_telegram_id`) VALUES (?)", (str(user_id),))
        print('Новый пользователь внесен в базу данных')
        return self.conn.commit()

    def check_note_section_status(self, user_id):
        result = self.cursor.execute(
            f"SELECT `question_sections_status` FROM `user_config` WHERE `user_id` =  (?) ",
            (str(self.fetch_user_id(user_id), )))
        return result.fetchall()

    def get_config(self, user_id):
        result = self.cursor.execute(f"SELECT `work_hours`, `technic_name`, `question_sections_status` FROM `user_config` LEFT JOIN `technics` using(technic_id)  WHERE `user_id` =  (?) ", (str(self.fetch_user_id(user_id),)))
        return result.fetchall()

    def set_technic(self, user_id, technic):
        self.cursor.execute(f"UPDATE `user_config` SET `technic_id` = (?) WHERE  `user_id` = (?)",
                            (technic, str(self.fetch_user_id(user_id), )))
        return self.conn.commit()

    def change_sections_status(self, user_id, status):
        self.cursor.execute(f"UPDATE `user_config` SET `question_sections_status` = (?) WHERE  `user_id` = (?)",
                            (status, str(self.fetch_user_id(user_id), )))
        return self.conn.commit()

    def set_hours(self,user_id, hours):
        self.cursor.execute(f"UPDATE `user_config` SET `work_hours` = (?) WHERE  `user_id` = (?)",(hours, str(self.fetch_user_id(user_id), )))
        return self.conn.commit()

    def add_note(self, user_id, text):
        self.cursor.execute("INSERT INTO `notes` (`user_id`,`note`) VALUES (?,?) ",(str(self.fetch_user_id(user_id)) , str(text),))
        return self.conn.commit()

    def add_task(self, user_id, text):
        self.cursor.execute("INSERT INTO `tasks` (`user_id`,`task`) VALUES (?,?) ",(str(self.fetch_user_id(user_id)) , str(text),))
        return self.conn.commit()

    def add_duration(self, user_id, duration):
        self.cursor.execute(f"UPDATE `tasks` SET `duration` = (?)  WHERE  `user_id` =  (?) AND `task_id` = (Select MAX(`task_id`) from `tasks` where `user_id` = (?))",
                            (duration, str(self.fetch_user_id(user_id)), str(self.fetch_user_id(user_id)), ))
        return self.conn.commit()

    def add_section(self, user_id, section):
        self.cursor.execute(
            f"UPDATE `tasks` SET `matrix_section_id` = (?)  WHERE  `user_id` =  (?) AND `task_id` = (Select MAX(`task_id`) from `tasks` where `user_id` = (?))",
            (section, str(self.fetch_user_id(user_id)), str(self.fetch_user_id(user_id)),))
        return self.conn.commit()

    def add_note_kind(self, user_id, kind):
        self.cursor.execute(
            f"UPDATE `notes` SET `section_id` = (?)  WHERE  `user_id` =  (?) AND `note_id` = (Select MAX(`note_id`) FROM `notes` WHERE `user_id` = (?))",
            (kind, str(self.fetch_user_id(user_id)), str(self.fetch_user_id(user_id)),))
        return self.conn.commit()

    def del_records(self, user_id, what2del):
        result = self.cursor.execute(f"DELETE FROM `{what2del}` WHERE `user_id` = (?)", str(self.fetch_user_id(user_id)),)
        return self.conn.commit()

    def check_notes(self, user_id):
        result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_id` = (?)", str(self.fetch_user_id(user_id)),)
        return bool(len(result.fetchall()))

    def check_tasks(self, user_id):
        result = self.cursor.execute("SELECT `task` FROM `tasks` WHERE `user_id` = (?)", str(self.fetch_user_id(user_id)),)
        return bool(len(result.fetchall()))

    def check_mat_technic(self, user_id):
        result = self.cursor.execute("SELECT `technic_id` FROM `user_config` WHERE `user_id` = (?)",
                                     str(self.fetch_user_id(user_id)), )
        return bool(len(result.fetchall()))

    def check_section(self, user_id, section_id):
        result = self.cursor.execute("SELECT `matrix_section_id` FROM `tasks` WHERE `user_id` =  (?) and `matrix_section_id` = (?) ",
                                     (str(self.fetch_user_id(user_id)), section_id, ))
        return result.fetchall()

    def get_matrix_section(self, user_id, section_id):
        result = self.cursor.execute(
            f"SELECT `task` FROM `tasks` WHERE `user_id` =  (?) and `matrix_section_id` = (?)",
            (str(self.fetch_user_id(user_id)), section_id))
        return result.fetchall()

    def get_matrix_section_name(self, section_id):
        result = self.cursor.execute(
            f"SELECT `matrix_section` FROM `matrix_sections` WHERE  `matrix_section_id` = (?)", (section_id,))
        return result.fetchall()

    def show_notes(self, user_id,rang):
        if rang == 24:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_id` = (?) AND `date_added` BETWEEN datetime('now', 'start of day') AND datetime('now', 'localtime')  ORDER BY `section_id`, `date_added` ", str(self.fetch_user_id(user_id)),)
        if rang == 7:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_id` = (?) AND `date_added` BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') ORDER BY `date_added` ", str(self.fetch_user_id(user_id)),)
        if rang == 31:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_id` = (?) AND `date_added` BETWEEN datetime('now', 'start of month') AND datetime('now', 'localtime') ORDER BY `date_added`", str(self.fetch_user_id(user_id)),)
        if rang == 0:
            result = self.cursor.execute("SELECT `note` FROM `notes` WHERE `user_id` = (?) ", str(self.fetch_user_id(user_id)),)
        
        return result.fetchall()

    def update_satistics(self, user_id):
        result = self.cursor.execute(f"SELECT `id` FROM `active_shedule` WHERE `user_id` = (?)",
                                     str(self.fetch_user_id(user_id)), )
        result =  len(result.fetchall())
        self.cursor.execute(f"UPDATE `statistics` SET `task_done_count` = `task_done_count` + {result}  WHERE  `user_id` =  (?) ",
        (str(self.fetch_user_id(user_id)),))
        self.conn.commit()

    def del_active_shedule(self, user_id):
        self.cursor.execute(f"DELETE FROM `active_shedule` WHERE `user_id` = (?)",
                                     str(self.fetch_user_id(user_id)), )
        return self.conn.commit()
    def insert_active_shedule(self, user_id, secuin):
        for i in secuin:
            self.cursor.execute( f"INSERT INTO `active_shedule` (`user_id`, `task_id`) VALUES (?,?)", (str(self.fetch_user_id(user_id)), i, ))
            self.conn.commit()

    def del_records_from_schedule(self, user_id):
        self.cursor.execute(f"DELETE FROM `tasks` WHERE `task_id` IN (SELECT `task_id` FROM `active_shedule` WHERE `user_id` = (?))", str(self.fetch_user_id(user_id)), )
        return self.conn.commit()

    def get_task4scedule(self, user_id):
        result = self.cursor.execute(
            f"SELECT `matrix_section_id`, `task`, `duration`, `task_id` FROM `tasks` WHERE `user_id` =  (?) ORDER BY `matrix_section_id` ",
            (str(self.fetch_user_id(user_id), )))
        return result.fetchall()

    def get_task_done(self, user_id):
        result = self.cursor.execute(
            f"SELECT `task_done_count`FROM `statistics` WHERE `user_id` = (?)", (str(self.fetch_user_id(user_id), )))
        return result.fetchall()
