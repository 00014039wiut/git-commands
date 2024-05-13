import psycopg2

db_name = "company"
password = "Sql7575"
user = 'postgres'
port = 5432
host = 'localhost'

conn = psycopg2.connect(database=db_name, password=password, user=user, port=port, host=host)
cur = conn.cursor()


def create_table():
    create_table_query = '''Create table Users(
    ID serial primary key unique,
    name varchar(20) not null,
    age int not null,
    email varchar(30),
    password varchar(50)
    
    )'''
    cur.execute(create_table_query)
    conn.commit()


# create_table()
class User:
    def __init__(self,
                 user_name: str,
                 user_age: int,
                 user_email: str,
                 user_password: str):
        self.name = user_name
        self.age = user_age
        self.email = user_email
        self.password = user_password

    def save(self):
        insert_data_query = "insert into users(name, age, email, password) values(%s,%s, %s, %s);"
        insert_data_params = (self.name, self.age, self.email, self.password)
        cur.execute(insert_data_query, insert_data_params)
        conn.commit()

    @staticmethod
    def get_all():
        get_all_query = """select * from users"""
        cur.execute(get_all_query)
        data = cur.fetchall()
        for i in data:
            print(i)
        conn.commit()


def create_new_user():
    user_name = input("Name => ")
    user_age = int(input("Age => "))
    user_email = input("Email => ")
    user_password = input("Password => ")
    user1 = User(user_name, user_age, user_email, user_password)
    user1.save()
    print("User successfully saved")


def create_schema():
    schema = """create schema texnomart"""
    cur.execute(schema)
    conn.commit()
create_schema()


create_new_user()
User.get_all()
