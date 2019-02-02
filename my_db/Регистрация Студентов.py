from typing import List, Any
from appJar import gui
import postgresql
file_name = 'students.txt'


testn = []
users = {}
ents = {}
# handle button events

db = postgresql.open("pq://postgres:G24O02d24230303@127.0.0.1:5432/my_db")
db.execute("CREATE TABLE IF NOT EXISTS students(id numeric PRIMARY KEY,fio text, birthday varchar(20),gender varchar , description varchar(50), raiting numeric)")

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
        users['Педагог'] = user
        birthday = app.getEntry("Ваш день рождения")
        users['Ваш день рождения'] = birthday

        gender = app.getAllOptionBoxes()

        description = app.getEntry("Что Вы изучаете")
        raiting = app.getEntry("Рейтинг")
        ents['Что Вы изучаете'] = description
        ents['Рейтинг'] = raiting

        users.update(gender)
        users.update(ents)
        testn.append(users)

        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(str(testn) + '\n')

        tablReg = db.prepare("INSERT INTO students VALUES ($1, $2, $3, $4, $5, $6)")
        raise_Reg = db.prepare("UPDATE students SET fio = $2, birthday = $3, gender = $4, description  = $5, raiting = $6 WHERE id = $1")

        with db.xact() as xact:
            TablRegict = db.query("SELECT id FROM students")
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
                        tablReg(L[0], str(L[1]), L[2], str(L[3]), L[4], str(L[5]))

# create a GUI variable called app
app = gui("Список Студентов ", "380x350")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Зарегистрируйтесь пожалуйста !!")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Фамилия")
app.addLabelEntry("Имя")
app.addLabelEntry("Отчество")
app.addLabelEntry("Ваш день рождения")
app.addLabelOptionBox("- Укажите Ваш пол -", ["True","False"])
app.addLabelEntry("Что Вы изучаете")
app.addLabelEntry("Рейтинг")

# link the buttons to the function called press

app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Фамилия")

# start the GUI
app.go()