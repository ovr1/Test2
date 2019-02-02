from typing import List, Any
from appJar import gui
import postgresql
file_name = 'reпistration5.5.txt'


testn = []
users = {}
ents = {}
# handle button events

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_db")
db.execute("CREATE TABLE IF NOT EXISTS registration5 (id numeric PRIMARY KEY,fio text, age numeric,v_purpose varchar(20), tel numeric, mail varchar(20), pasport varchar(20))")

#postgresql.exceptions.DuplicateTableError: relation "registration5" already exists
#postgresql.exceptions.UndefinedTableError: relation "registration5" does not exist

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        usr = app.getEntry("Фамилия")
        name = app.getEntry("Имя")
        otch = app.getEntry("Отчество")
        user = usr + ' '+ name + ' ' + otch
        users['Пациент'] = user
        age = app.getEntry("Ваш возраст")
        users['Ваш возраст'] = age

        pwd = app.getAllOptionBoxes()

        tel = app.getEntry("Ваш телефон")
        e_mail = app.getEntry("Ваш e-mail")
        sek = app.getEntry("Паспорт")
        ents['Телефон'] = tel
        ents['E-mail'] = e_mail
        ents['Паспорт'] = sek

        users.update(pwd)
        users.update(ents)
        testn.append(users)

        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(str(testn) + '\n')

        tablReg = db.prepare("INSERT INTO registration5 VALUES ($1, $2, $3, $4, $5, $6, $7)")
        raise_Reg = db.prepare("UPDATE registration5 SET fio = $2, age = $3, v_purpose = $4, tel = $5, mail = $6, pasport = $7 WHERE id = $1")

        with db.xact() as xact:
            TablRegict = db.query("SELECT id FROM registration5")
            N = str(int(len(TablRegict)) + 1)
            with open(file_name, 'r', encoding='utf-8') as f:
                contents = f.readlines()
                for line in contents:
                    ds = eval(str(line[1:-2]))
                    V = list(ds.values())
                    V.insert(0, N)
                    L = tuple(V)
                    print(L)
                    with db.xact():
                        tablReg(L[0], str(L[1]), L[2], str(L[3]), L[4], str(L[5]),str(L[6]))

# create a GUI variable called app
app = gui("Галина Рыбынок ", "380x350")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Добро пожаловать !!")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Фамилия")
app.addLabelEntry("Имя")
app.addLabelEntry("Отчество")
app.addLabelEntry("Ваш возраст")
app.addLabelOptionBox("- Цель Визита -", ["Консультация",
                                     "Классический массаж", "СПА", "Медитация"])
app.addLabelEntry("Ваш телефон")
app.addLabelEntry("Ваш e-mail")
app.addLabelSecretEntry("Паспорт")

# link the buttons to the function called press

app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Фамилия")

# start the GUI
app.go()