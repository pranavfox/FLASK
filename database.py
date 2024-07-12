import mysql.connector


def get_data():
    mydb = mysql.connector.connect(host = "localhost",user="root ",database="testtube")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchmany()
    mycursor.close()
    mydb.close()
    return result
    