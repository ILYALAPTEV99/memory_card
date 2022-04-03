#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

app = QApplication([])
window = QWidget()
window.setWindowTitle('Конкурс от Crazy People')
nad = QLabel('Какой национальности не существует?')
box = QGroupBox('Варианты')
bt1 = QRadioButton('Энцы')
bt2 = QRadioButton('Чулымцы')
bt3 = QRadioButton('Смурфы')
bt4 = QRadioButton('Алуеты')
bt5 = QPushButton('Ответить')
box2 = QGroupBox('Результат')
nad2 = QLabel('Правильно/Неправильно')
nad3 = QLabel('Правильно')
answer = [bt1, bt2, bt3, bt4]
box.show()
box2.hide()
v_lineb2 = QVBoxLayout()
v_lineb2.addWidget(nad2, alignment = Qt.AlignLeft)
v_lineb2.addWidget(nad3, alignment= Qt.AlignCenter)
v_line = QVBoxLayout()
v_line1 = QHBoxLayout()
v_line2 = QHBoxLayout()
v_line3 = QHBoxLayout()
v_line4 = QHBoxLayout()
mainline = QVBoxLayout()      
def test():
    box2.hide()
    box.show()
    bbox.setExclusive(False)        
    bt1.setChecked(False)
    bt2.setChecked(False)
    bt3.setChecked(False)
    bt4.setChecked(False)
    bbox.setExclusive(True)
    bt5.setText('Ответить')
def otvet():
    box.hide()
    box2.show()
    bt5.setText('Следующий вопрос')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

qust = list()
q1 = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алуеты')
q2 = Question('Государский язык Бразилии?', 'Португальский', 'Испанский', 'Итальянский', 'Бразильский')
q3 = Question('Какой страны не существует?', 'Мурт', 'Бразилия', 'Италия', 'Россия')
q4 = Question('Какой язык программирования мы изучаем?', 'Pyton', 'C++', 'Java', 'С')
q5 = Question('Сколько океанов в мире?', '5', '2', '4', '6')
q6 = Question('Сколько будет 2+2?', '4', '22', '2', '8')
q7 = Question('В каком году вышла гта 5?', '2015', '2010', '1977', '2000')
q8 = Question('В каком годы вышел майнкрафт?', '2009', '2008', '2000', '2001')
q9 = Question('В каком годы вышла форза хорайзен 4', '2018', '2020', '2019', '2021')
q10 = Question('Какой сейчас год?', '2021', '2200', '2009', '2020')
qust.append(q1)
qust.append(q2)
qust.append(q3)
qust.append(q4)
qust.append(q5)
qust.append(q6)
qust.append(q7)
qust.append(q8)
qust.append(q9)
qust.append(q10)
def ask(q: Question):
    shuffle(answer)
    nad.setText(q.question)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    na = f'Правильный ответ: {q.right_answer}'
    nad3.setText(na)



def check_answer():
    prov = answer[0].isChecked()
    if prov:
        res = True

    else:
        res = False
    show_correct(res)

def wind():
    shuffle(qust)
    ask(qust[0])

window.b = 0
window.c = 1
window.total = window.b/window.c*100
ask(q1)
print(qust)


def show_correct(res):
    if bt5.text() == 'Следующий вопрос':
        wind()
        test()
        window.c += 1
    else:
        print('Количество пройденых вопросов:',window.c)
        if res:
            window.b += 1
            print('Количество правильных ответов:',window.b)
            otvet()
            nad2.setText('Правильно')
        else:
            print('Количество правильных ответов:',window.b)
            otvet()
            nad2.setText('Неправильно')
        window.total = window.b/window.c*100
        print('Процент эфективность правильных ответов:',window.total)





bt5.clicked.connect(check_answer)

bbox = QButtonGroup()
bbox.addButton(bt1)
bbox.addButton(bt2)
bbox.addButton(bt3)
bbox.addButton(bt4)


#v_line.addWidget(nad, alignment= Qt.AlignCenter)
#v_line1.addWidget(nad, alignment = Qt.AlignCenter)
v_line2.addWidget(answer[0], alignment= Qt.AlignCenter)
v_line3.addWidget(answer[1], alignment= Qt.AlignCenter)
v_line2.addWidget(answer[2], alignment= Qt.AlignCenter)
v_line3.addWidget(answer[3], alignment= Qt.AlignCenter)
#v_line4.addWidget(bt5, alignment= Qt.AlignCenter)

#v_line.addLayout(v_line1)
v_line.addLayout(v_line2)
v_line.addLayout(v_line3)
#v_line.addLayout(v_line4)
#v_line.addLayout(v_lineb2)
mainline.addWidget(nad, alignment= Qt.AlignCenter)
mainline.addWidget(box)
mainline.addWidget(box2)
box.setLayout(v_line)
box2.setLayout(v_lineb2)
mainline2 = QVBoxLayout()
mainline3 = QVBoxLayout()
h_line = QHBoxLayout()
h_line.addWidget(bt5, stretch=2)
h_line2 = QHBoxLayout()
mainline.addLayout(h_line)
mainline.addLayout(h_line2)
mainline.setSpacing(5)
mainline2.setSpacing(5)
mainline3.setSpacing(5)

#box2.setLayout(v_line)
window.setLayout(mainline)
window.setLayout(mainline2)
window.setLayout(mainline3)
window.show()
app.exec_()