# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random
import requests
import html
import urllib.request
#urllib.request for checking connectivity


# load questions and answer choices from json file api instead of the file
url1 = "https://opentdb.com/api.php?amount=10&category=23&difficulty=medium&type=multiple"
url2 = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"
url3 = "https://opentdb.com/api.php?amount=10&category=17&type=multiple"
url4 = "https://opentdb.com/api.php?amount=10&category=21&difficulty=easy&type=multiple"
def questionType() :
    global qtype
    qtype = Label(
        root,
        text='Select Type of Question',
        font=("Comic sans MS", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="cyan",
    )
    qtype.pack(pady=(100, 30))

    global urlvar,o1,o2,o3,o4
    urlvar = StringVar()
    urlvar.set("None")

    o1 = Radiobutton(
        root,
        text="History",
        font=("Comic sans MS", 12),
        value=url1,
        variable=urlvar,
        command=select,
        background="#ffffff",
    )
    o1.pack(pady=5)

    o2 = Radiobutton(
        root,
        text="General Knowledge",
        font=("Comic sans MS", 12),
        value=url2,
        variable=urlvar,
        command=select,
        background="#ffffff",
    )
    o2.pack(pady=5)

    o3 = Radiobutton(
        root,
        text="Science",
        font=("Comic sans MS", 12),
        value=url3,
        variable=urlvar,
        command=select,
        background="#ffffff",
    )
    o3.pack(pady=5)

    o4 = Radiobutton(
        root,
        text="Sports",
        font=("Comic sans MS", 12),
        value=url4,
        variable=urlvar,
        command=select,
        background="#ffffff",
    )
    o4.pack(pady=5)
turl="https://www.google.co.in/webhp"
def connect(host=turl) :
    try :
        urllib.request.urlopen(host)
        return False
    except :
        return True
qFile=[]
def getjason(url):
    global qFile
    if (connect()) :
        print("you are not connected to internet")
        with open('./data.json', encoding="utf8") as f:
            data = json.load(f)
    else :
        r = requests.get(url)
        data = json.loads(r.text)
    qFile = data['results']

def select() :
    global url,urlvar
    u = urlvar.get()
    url=u
    qtype.destroy()
    o1.destroy()
    o2.destroy()
    o3.destroy()
    o4.destroy()
    connect()
    getjason(url)
    qlist()
    startquiz()



#check whether you are connected to internet if not then default questions will appear


print("your answer","   ", "correct answer")
# convert the dictionary in lists of questions and answers_choice
questions=[]
answers_choice = []
answers = []
def qlist() :
    global qFile,questions,answers_choice,answers
    for i in range(0, 10):
        questions.append(qFile[i]['question'])

    temp_answers = []
    for i in range(0, 10):
        answers.append(qFile[i]["correct_answer"])
        temp_answers.append(qFile[i]["correct_answer"])
        temp_answers.extend(qFile[i]["incorrect_answers"])
        answers_choice.append(temp_answers)
        random.shuffle(answers_choice[i])
        temp_answers = []


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Comic sans MS", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text=f"Hurray!!! Your Score is {score} out of 50")
    elif (score >= 10 and score < 20):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text=f"Hmm nice you got {score} out of 50")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text=f"Your Score is {score} out of 50, Prepare more")


score = 0;


def calc():
    global score
    score += 5


ques = 1


def selected():
    global radiovar, answers_choice, answers
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    if answers_choice[ques-1 ][int(x)] == answers[ques-1]:
        calc()
    print(answers_choice[ques-1 ][int(x)], answers[ques-1])
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text=html.unescape(questions[ques]))
        r1['text'] = html.unescape(answers_choice[ques][0])
        r2['text'] = html.unescape(answers_choice[ques][1])
        r3['text'] = html.unescape(answers_choice[ques][2])
        r4['text'] = html.unescape(answers_choice[ques][3])
        ques += 1
    else:
        showresult(score)
#startquiz function
def startquiz():
    global lblQuestion, r1, r2, r3, r4,questions,answers_choice
    lblQuestion = Label(
        root,
        text=html.unescape(questions[0]),
        font=("Comic sans MS", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="cyan",
        #image=PhotoImage(file="qbox.png")
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=html.unescape(answers_choice[0][0]),
        font=("Comic sans MS", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=html.unescape(answers_choice[0][1]),
        font=("Comic sans MS", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=html.unescape(answers_choice[0][2]),
        font=("Comic sans MS", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=html.unescape(answers_choice[0][3]),
        font=("Comic sans MS", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)

#following operations wil be performed when start key is pressed
def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    questionType()

#gui part

root = tkinter.Tk()
root.title("Quiz in python")
root.geometry("780x660")
root.config(background="#ffffff")
root.resizable(0, 0)

img1 = PhotoImage(file="quiz.png")

labelimage = Label(
    root,
    image=img1,
    background="#ffffff",
)
labelimage.pack(pady=(4, 0))

labeltext = Label(
    root,
    text="Quiz in python",
    font=("Comic sans MS", 24, "bold"),
    background="#ffffff",
)
labeltext.pack(pady=(0, 50))

labeltextname = Label(
    root,
    text="By Ankit and Akanshu",
    font=("Comic sans MS", 14, "bold"),
    background="#ffffff",
)
labeltextname.pack(pady=(0,20))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image=img2,
    relief=FLAT,
    border=0,
    command=startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background="#ffffff",
    font=("Comic sans MS", 14),
    justify="center",
)
lblInstruction.pack(pady=(50, 100))

lblRules = Label(
    root,
    text="This quiz contains 10 questions. 5 marks for each question\nOnce you select a radio button that will be a final choice\nhence think before you select. Best of luck",
    width=100,
    font=("Comic sans MS", 14),
    background="#222fff",
    foreground="#FACA2F",
)
lblRules.pack()

root.mainloop()
