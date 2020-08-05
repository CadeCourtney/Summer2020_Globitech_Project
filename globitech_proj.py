import threading
import psycopg2
import time

tableExists = False
tLock = threading.Lock()


def check_table(dbArray):
    print('Checking Table')
    con = psycopg2.connect(user=str(dbArray[0]), password=str(dbArray[1]), host=str(dbArray[2]), port=str(dbArray[3]),
                           database=str(dbArray[4]))
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS Database;')
    cur.execute('CREATE TABLE Database(Name TEXT, Address TEXT, Email TEXT, Major TEXT);')
    con.commit()
    # print('Closing')
    con.close()


def upload(name, user, password, host, port, db, arrayOfTuples):
    try:
        print(name, 'is STARTING')
        con = psycopg2.connect(user=str(user), password=str(password), host=str(host), port=str(port), database=str(db))
        print(con)
        cur = con.cursor()
        # print(name, 'is INSERTING\n')
        cur.executemany('INSERT INTO Database VALUES(%s,%s,%s,%s);', arrayOfTuples)  # insert data into database
        con.commit()  # commit changes to DB
        cur.execute('SELECT * FROM Database')  # SELECT all (*) contents from table Pets
        # Debugging
        # data = cur.fetchall()  # place contents into data variable
        # print(name + ':', data)
        # for row in data:
        #     print(row)
    except (Exception, psycopg2.Error) as error:
        if con:
            print('Error!', error, 'Rolling Back')
            con.rollback()
        else:
            print("Error while connecting to PostgreSQL", error)
    finally:
        print(name, 'is CLOSING')
        if con:
            con.close()


def array_of_tuples(fileName):
    dataList = []
    with open(fileName) as fh:
        for ii in fh.readlines():
            data = tuple(ii.split(','))
            # print(data)
            dataList.append(data)
    dataList.pop(0)  # remove header
    # Debugging
    # for data in dataList:
    #     for item in data:
    #         print(item, type(item))
    # print('RETURNING LIST')
    return dataList


def main():
    start = time.time()
    db = ['USER', 'PASSWORD', '127.0.0.1', 5433, 'Database']
    fileArray = ['csv_file_1.csv', 'csv_file_2.csv', 'csv_file_3.csv', 'csv_file_4.csv']
    check_table(db)
    t1 = threading.Thread(target=upload,
                          args=('t1', db[0], db[1], db[2], db[3], db[4],
                                array_of_tuples(fileArray[0])))
    t2 = threading.Thread(target=upload,
                          args=('t2', db[0], db[1], db[2], db[3], db[4],
                                array_of_tuples(fileArray[1])))
    t3 = threading.Thread(target=upload,
                          args=('t3', db[0], db[1], db[2], db[3], db[4],
                                array_of_tuples(fileArray[2])))
    t4 = threading.Thread(target=upload,
                          args=('t4', db[0], db[1], db[2], db[3], db[4],
                                array_of_tuples(fileArray[3])))
    threads = [t1, t2, t3, t4]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print('TIME:', end - start)


# Debugging
# fileArray = ['csv_file_1.csv', 'csv_file_2.csv', 'csv_file_3.csv', 'csv_file_1.csv', 'csv_file_4.csv']
# dataArray = array_of_tuples(fileArray[0])
# print(dataArray)
if __name__ == '__main__':
    main()
