import eel
from call_db import cursor, connection

cur = cursor
db = connection
cur.execute("""CREATE TABLE IF NOT EXISTS Users(
id INT AUTO_INCREMENT,
login VARCHAR(32),
phone VARCHAR(32),
PRIMARY KEY(id)
)""")
db.commit()


def valid_number(number):
    print(number)
    len_num = len(number)
    len_bool = False
    prefix = False
    cod = False
    if len_num == 12 and number[0] == '+':
        len_bool = True
    elif len_num == 11:
        len_bool = True
    if number[:-10] in ['8', '+7']:
        prefix = True
    if number[-10:-7][0] == '9':
        cod = True
    target = prefix == len_bool == cod
    return target
    print(target)

def add_to_base(inform):
    cur.execute("""SELECT phone FROM Users""")
    if valid_number(inform[1]):
        if not (inform[1],) in cur.fetchall():
            l = list(inform)
            l[1] = inform[1][-10:]
            inform = tuple(l)
            cur.execute("""SELECT * FROM Users""")
            cur.executemany("INSERT INTO Users(login,phone) Values(%s,%s)", [inform])
        else:
            print("Было")
    else:
        print("Номер херня")
    connection.commit()
    cur.execute("""SELECT * FROM Users""")


eel.init("web")


@eel.expose
def get_inf(nick, tel):
    inf = (str(nick), str(tel))
    add_to_base(inf)


eel.start("register.html", size=(1200, 900))
