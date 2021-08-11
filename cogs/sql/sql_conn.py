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
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `scroll_txt` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            PRIMARY KEY (`id`) USING BTREE
        )
        COMMENT='Das ist die main DB für den Discord Bot!'
        COLLATE='utf8mb4_general_ci'
        ENGINE=InnoDB
        AUTO_INCREMENT=0
        """)

        cur.execute("INSERT INTO discord_db (id, scroll_txt) VALUE (0, 'Waddup B*tch!')")
        cur.commit()
    else:
        raise Exception


