import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        database='aob'
    )

    cur = mydb.cursor()
except Exception as error:
    err = str(error)
    if '1049' in err:
        db_to_create = mysql.connector.connect(
            host='localhost',
            user='root'
        )

        cur = db_to_create.cursor()
        cur.execute('CREATE DATABASE aob')

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            database='aob'
        )

        cur = mydb.cursor()

        cur.execute("""
            CREATE TABLE `discord_db` (
                `scroll_txt` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci'
            )
            COMMENT='Das ist die MainDB für den Discord Bot!'
            COLLATE='utf8mb4_general_ci'
            ENGINE=InnoDB
        """)
    else:
        raise Exception


