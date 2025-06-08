import psycopg2
def create_table():
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE IF NOT EXISTS STUDENTS (
    ID SERIAL PRIMARY KEY,
    NAME TEXT,
    AGE TEXT,
    ADDRESS TEXT
    );''')
    conn.commit()
    conn.close()
    print("table created successfully")

def insert_data(): 
    conn=psycopg2.connect(dbname="postgres",user="postgres",password="12345",host="localhost",port="5432")
    curr = conn.cursor()

    NAME=input("ENTER THE NAAME")
    AGE=input("ENTER THE AGE")
    ADDRESS=input("ENTER THE ADDRESS")
    query=(''' INSERT INTO STUDENTS (NAME,AGE,ADDRESS) VALUES (%s,%s,%s)''')
    curr.execute(query,(NAME,AGE,ADDRESS))

    conn.commit()
    conn.close()
    print("DATA INSERTED successfully") 

insert_data()      