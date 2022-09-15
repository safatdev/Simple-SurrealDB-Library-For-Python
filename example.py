
from surrealdb import SurrealDB


def main():

    # host
    db = SurrealDB('http://localhost:8000/sql')

    # namespace and db
    db.use('test', 'test')

    # DBInfo
    resp = db.info()

    # Create Table `person` with custom `id` and content
    resp = db.create('person:safat', {'name': 'Safat', 'age': 22, 'occupation': 'Student'})

    # Select all records in person table
    resp = db.select('person')

    # Insert into person with custom id
    resp = db.insert('person', {'name': 'Bob', 'age': 30, 'occupation': 'Builder'})

    # Select name and age where age>18
    resp = db.select('person', projections='name, age', options='WHERE age > 18')

    # Update bob's age -> return before updated record
    resp = db.update('person', {'age': 32}, upd_type='MERGE', condition='name="Bob"', returns='BEFORE')

    # Delete with condition and timeout
    resp = db.delete('person', condition='age>30', timeout=5)

    # Delete with id
    resp = db.delete('person:safat')

    # Table info
    resp = db.info('TABLE', 'person')

    # Change user
    db.set_user(('test', 'test'))

    # Change namespace/db
    db.use('test', 'test1')

    # Custom Query
    resp = db.query("SELECT * from person")

    # response
    print(resp.status_code)
    print(resp.text)
    print(resp.json())


if __name__ == '__main__':
    main()
