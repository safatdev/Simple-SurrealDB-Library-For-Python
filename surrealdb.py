
import requests
import json
import re


class SurrealDB:

    def __init__(self, host: str):
        self.__host = host
        self.__headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'SurrealDB-Simple-Python-Library_0.0.1',
        }
        self.__user = ('root', 'root')

    def set_user(self, user: tuple):
        self.__user = user

    def use(self, namespace: str, database: str):
        self.__headers['NS'] = namespace
        self.__headers['DB'] = database

    def query(self, query: str):
        return requests.post(self.__host, headers=self.__headers, auth=self.__user, data=query)
