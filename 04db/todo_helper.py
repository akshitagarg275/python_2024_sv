# performing all the utility functionalities

import sqlite3

con = sqlite3.connect("todo.db")
cur = con.cursor()
table_name = 'todos'

# create a table 
# query: create table if not exists table_name (id integer primary key autoincrement, taskname text)
def create_table():
    sql = f'CREATE TABLE IF NOT EXISTS {table_name} (id integer primary key autoincrement, taskname text)'
    cur.execute(sql)



# Adding todo in the table
def add_todo(todoName):
    # insert into table_name (column_name) values (column_values)
    cur.execute("INSERT INTO " + table_name + " (taskname) values (?)", [todoName])
    print("Todo added in the DB successfully")
    con.commit()

# Reading data from the table
def read_todo():
    # select column_name1, column_name2 from table_name
    # select * from table_name
    cur.execute("SELECT * FROM " + table_name)

    for row in cur.fetchall():
        print(f'{row[0]} ----> {row[1]}')


# update the table
def update_todo(idx, updatedTask):
    # update table_name set column_name=new_value where ID=index
    cur.execute("UPDATE " +  table_name + " SET taskname = (?) WHERE id = (?)", [updatedTask, idx])
    print("Task completed successfully")
    con.commit()

# delete the data
def delete_task(idx):
    # delete from table_name where id = index
    cur.execute("DELETE from " + table_name + " WHERE id = (?)" , [idx])
    print("Task deleted successfully!")
    con.commit()

def close_connection():
    cur.close()
    con.close()