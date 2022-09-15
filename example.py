
from surrealdb import SurrealDB


def main():

    # host
    db = SurrealDB('http://localhost:8000/sql')

    # namespace, db
    db.use('test', 'test')

    # raw query -> returns 'requests' Response Object
    resp = db.query("CREATE person:1 SET name='Safat', age=22, occupation='Student'")

    # print code / text / encode json
    print(resp.status_code)
    print(resp.text)
    print(resp.json())

    # change user
    db.set_user(('test', 'test'))

    # change namespace/db
    db.use('test', 'test1')
    resp = db.query("SELECT * from person")
    print(resp.text)


if __name__ == '__main__':
    main()
