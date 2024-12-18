import getpass
from os import getenv
from dotenv import load_dotenv, find_dotenv
from pykeepass import PyKeePass
from src.Entry.Entry import Entry

class App:

    def __init__(self):

        load_dotenv(find_dotenv())

        keepass_db_path = getenv("KEEPASS_DB_PATH")
        keepass_db_password = getenv("KEEPASS_DB_PASSWORD")

        if not keepass_db_path:
            print("KEEPASS_DB_PATH")
            keepass_db_path = input("Введите keepass_db_path: ")
        if not keepass_db_password:
            print("KEEPASS_DB_PASSWORD")
            keepass_db_password = getpass.getpass(prompt="Введите keepass_db_password: ")

        self._keepass = PyKeePass(keepass_db_path, keepass_db_password)
        self._entries = self._keepass.entries

    def check_urls(self):
        print('start check_urls')
        for entry in self._entries:
            entry = Entry(entry)
            entry.url.check_url()
        print('stop check_urls')

    def sanitize_urls(self):
        print('start sanitize_urls')
        for entry in self._entries:
            entry = Entry(entry)
            entry.url.remove_http()
            entry.url.remove_https()
            entry.url.remove_www()
            entry.url.remove_end_slash()
            entry.url.remove_wp_login()
            entry.url.google_ru_to_com()
        print('stop sanitize_urls')

    def sanitize_usernames(self):
        print('start sanitize_usernames')
        for entry in self._entries:
            entry = Entry(entry)
            entry.username.ya_to_yandex()
            entry.username.lowercase()
        print('stop sanitize_usernames')

    def save(self):
        self._keepass.save()
        print('Изменения сохранены')
































