import gspread
from config import DATABASE_NAME


class Database:

    def __init__(self):
        self.sa = gspread.service_account()
        self.sdb = self.sa.open(DATABASE_NAME)
        self.worksheets = self.sdb.worksheets()
        print(self.worksheets)

    def add_message_to_db(self, chat_id, from_id, text):
        self.worksheets[3].add_rows(1)
        index = self.worksheets[3].row_count + 1
        print('index: ' + str(index) + ' text:' + text)
        self.worksheets[3].update_cell(index, 1, str(chat_id))
        self.worksheets[3].update_cell(index, 2, str(from_id))
        self.worksheets[3].update_cell(index, 3, str(text))
        print('ADDED')

    def get_chat(self, chat_id):
        records = self.worksheets[3].get_all_records()
        chat = filter(lambda record: str(record["chat_id"]) == str(chat_id), records)
        chat = list(chat)
        return chat

    def get_faqs(self):
        records = self.worksheets[1].get_all_records()
        records = list(records)
        return records

