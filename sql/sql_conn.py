import mysql.connector

from config import SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE


try:
    mydb = mysql.connector.connect(
        host=SQL_HOST,
        user=SQL_USER,
        password=SQL_PASSWORD,
        database=SQL_DATABASE
    )

    cur = mydb.cursor()
except Exception as error:
    err = str(error)
    if '1049' in err:
        print('[SQL] Database does not exist or is misspelled')
    else:
        raise Exception


def create_table(arg):
    if arg.lower() == 'main':
        cur = mydb.cursor()

        cur.execute("""
        CREATE TABLE `discord_db` (
            `id` INT(11) NOT NULL AUTO_INCREMENT,
            `scroll_txt` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
            PRIMARY KEY (`id`) USING BTREE
        )
        COMMENT='Das ist der Main Table für den AOB-Discordbot!'
        COLLATE='utf8mb4_general_ci'
        ENGINE=InnoDB
        AUTO_INCREMENT=0
        """)

        cur.execute("INSERT INTO discord_db (id, scroll_txt) VALUE (0, 'ts3.ageofblocks.de')")
        cur.commit()
    else:
        return 'Unknown argument'



