
import requests
import json


class SurrealDB:

    def __init__(self, host: str):
        self.__host = host
        self.__headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'SurrealDB-Simple-Python-Library_0.0.1',
        }
        self.__user = ('root', 'root')

    # Changes User
    def set_user(self, user: tuple):
        self.__user = user

    # Changes Namespace and Database
    def use(self, namespace: str, database: str):
        self.__headers['NS'] = namespace
        self.__headers['DB'] = database

    # Raw Query -> Sends Post Request to DB
    def query(self, query: str):
        return requests.post(self.__host, headers=self.__headers, auth=self.__user, data=query)

    #
    # Helpers
    #

    # Get Info
    def info(self, thing: str = 'DB', arg: str = None):
        return self.query(f'INFO FOR {thing} {"" if arg is None else arg};')

    # Select Records
    def select(self, targets: str, projections: str = '*', options: str = None, timeout: int = None):
        return self.query(f'SELECT {projections} FROM {targets} {"" if options is None else options} {"" if timeout is None else ("TIMEOUT " + str(timeout) + "s")};')

    # Insert Record
    def insert(self, table: str, content: dict):
        return self.query(f'INSERT INTO {table} {json.dumps(content)};')

    # Create Record
    def create(self, thing: str, content: dict, returns: str = 'AFTER', timeout: int = None):
        return self.query(f'CREATE {thing} CONTENT {json.dumps(content)} RETURN {returns} {"" if timeout is None else ("TIMEOUT " + str(timeout) + "s")};')

    # Update Record
    def update(self, thing: str, content: dict, upd_type: str = 'CONTENT', condition: str = None, returns: str = 'AFTER', timeout: int = None):
        return self.query(f'UPDATE {thing} {upd_type} {json.dumps(content)} {"" if condition is None else ("WHERE " + condition)} RETURN {returns} {"" if timeout is None else ("TIMEOUT " + str(timeout) + "s")};')

    # Delete Record
    def delete(self, thing: str, condition: str = None, returns: str = 'AFTER', timeout: int = None):
        return self.query(f'DELETE {thing} {"" if condition is None else ("WHERE " + condition)} RETURN {returns} {"" if timeout is None else ("TIMEOUT " + str(timeout) + "s")};')
