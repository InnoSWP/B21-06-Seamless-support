import gspread
from abc import ABCMeta, abstractmethod
from config import DATABASE_NAME
import time


class CloudDatabase:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """Initialization of your dataBase"""

    @abstractmethod
    def add_message_to_db(self, chat_id, from_id, text):
        """Adding message to your Database"""
        """Id of a chat, where this question was asked"""
        """Who sent this message"""
        """Text of a new message"""

    @abstractmethod
    def add_message_to_queue(self, user_id, text):
        """Adding message to your Queue"""

    @abstractmethod
    def pop_message_from_queue(self):
        """Getting first message from your Queue and then deleting this message"""

    @abstractmethod
    def peek_message_from_queue(self):
        """Getting first message from your Queue"""

    @abstractmethod
    def get_chat(self, chat_id):
        """Loading chat from your Database by its chat_id"""

    @abstractmethod
    def get_faqs(self):
        """Loading FAQ list from your Database"""


class GoogleSheets(CloudDatabase):

    def __init__(self):
        self.sa = gspread.service_account()
        self.sdb = self.sa.open(DATABASE_NAME)
        self.worksheets = self.sdb.worksheets()
        self.number_of_questions = self.worksheets[4].row_count - 1
        print(self.worksheets)

    def add_message_to_db(self, chat_id, from_id, text):
        self.worksheets[3].resize(rows=self.worksheets[3].row_count+1)
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

    def add_message_to_queue(self, user_id, text):
        self.worksheets[4].resize(self.number_of_questions + 2)
        self.worksheets[4].update_cell(self.number_of_questions + 2, 1, str(user_id))
        self.worksheets[4].update_cell(self.number_of_questions + 2, 2, str(text))
        self.number_of_questions += 1

    def pop_message_from_queue(self):
        message = self.peek_message_from_queue()
        self.worksheets[4].delete_row(2)
        self.number_of_questions -= 1
        print(self.number_of_questions)
        return message

    def peek_message_from_queue(self):
        message = self.worksheets[4].row_values(2)
        return message

    def get_faqs(self):
        records = self.worksheets[1].get_all_records()
        records = list(records)
        return records

    def get_num(self):
        return self.number_of_questions


gs = GoogleSheets()
