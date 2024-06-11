from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
import json
import settings
import uuid
   
window = Tk(className="Тест")
window.configure(bg="#CCFFFF")
window.geometry("400x200+480+180")
i = 0
a = 0
amount = 0
question_list = [("Завдання №1: Для чого призначено модуль tkinter?"),
                ("Завдання №2: Які основні етапи потрібно виконати для створення\n вікна?"),
                ("Завдання №3: Що таке клас у програмуванні на Python і як його\n створити?"),
                ("Завдання №4: Дайте визначення поняттю «подія»"),
                ("Завдання №5: Які функції можна використовувати\n для роботи з файлами в Python?")]
answer_list = [["Використовується для генерації випадкових чисел \n i виконання різних операцій, пов'язаних з випадковістю.",
                "Використовується для створення графічних інтерфейсів користувача.",
                "Надає функції для роботи з часом i датами."],
                ["Імпортувати необхідні класи з бібліотеки Tkinter;\n Створити екземпляр головного вікна;\n Опціонально налаштувати параметри вікна.",
                "Імпортувати необхідні класи з бібліотеки Tkinter;\n Створити екземпляр головного вікна;\n Опціонально налаштувати параметри вікна;\n Додати віджети та розмістити їх у вікні;\n Запустити головний цикл обробки подій.",
                "Створити екземпляр головного вікна;\n Імпортувати необхідні класи з бібліотеки Tkinter;\n  Запустити головний цикл обробки подій;\n Опціонально налаштувати параметри вікна."],
                ["Клас - це змінна, що містить набір значень\n і функцій, які оперують цими значеннями.\n Клас можна створити за допомогою ключового слова def. \n Наприклад: def MyClass():.",
                "Клас - це об'єкт, який містить дані та методи, що працюють з цими даними.\n Клас можна створити за допомогою ключового слова class.\n Наприклад: class MyClass:.",
                "Клас - це тип даних, що використовується для зберігання даних у вигляді колекції.\n Клас можна створити за допомогою ключового слова create_class.\n Наприклад: create_class MyClass:."],
                ["Подія - це функція, що пов'язана з певним об'єктом.",
                "Подія – подальша реакція програми (зовнішня дія) на віджет.",
                "Подія - це іменований блок коду."],
                ["open()","read()"," write()", "close()"]]


#------------------------------------
def registration(event):
    global but_start
    global a
    if (event.keysym == "space" or event.keysym == "<Button-1>") and a == 1:
        but_start.config(state="disabled")
        but_start.config(state="normal")
        return "break"
    but_start.config(state="disabled")
    global entry1
    global entry2
    global entry3
    global window1
    reg = Toplevel(window,bg="#CCFFFF")
    reg.title("Реєстрація")
    reg.geometry("350x250+500+180")
    label1 = Label(reg, text="Введіть ім'я\n(тільки букви):")
    label1.place(x=20,y=16)
    entry1 = Entry(reg,font="Arial16", fg="#AD0600")
    entry1.focus_get()
    entry1.place(x=110,y=16)
    label2 = Label(reg, text="Введіть пароль\n(тільки цифри):")
    label2.place(x=20,y=56)
    entry2 = Entry(reg,font="Arial16", fg="#AD0600")
    entry2.focus_get()
    entry2.place(x=120,y=56)
    label3 = Label(reg, text="Введіть пошту:")
    label3.place(x=20,y=96)
    entry3 = Entry(reg,font="Arial16", fg="#AD0600")
    entry3.focus_get()
    entry3.place(x=120,y=96)
    but_r1 = Button(reg, text="Завершити")
    but_r1.bind("<Motion>", check_entry)
    but_r1.place(x=120,y=156)
    a += 1
        

#------------------------------------

def check_entry(event):
    global name
    global password
    global email
    name = entry1.get()
    password = entry2.get()
    email = entry3.get()
    if name.isalpha() and password.isdigit() and  email.isalpha():
        get_value()
    else:
        # but_r1["state"] = DISABLED  
        showerror("Помилка!","Зробіть, як указано за інструкцією", icon="warning")
        name.isupper

#------------------------------------
def get_value():
    global t
    t = entry1.get()
    start_question()
#------------------------------------

def start_question():
    global var
    global entry1
    global window1
    global fram1
    window.destroy()
    window1 = Tk(className="Завдання")
    window1.configure(bg="#FFDDCC")
    window1.geometry("500x400+460+120")

    mainmenu = Menu(window1)
    window1.config(menu=mainmenu)

    def del_win():
        window1.destroy()

    filemenu1 = Menu (mainmenu, tearoff=0 , bg = "#FFC34D", foreground  = "#6B3927")
    filemenu1.add_command (label="Вихід", command=del_win)

    filemenu2 = Menu(mainmenu, tearoff=0 , bg = "#FFC34D", foreground  = "#6B3927")

    mainmenu.add_cascade (label = "Файл", menu=filemenu1)
    mainmenu.add_cascade(label = "Змінити", menu=filemenu2)
    # filemenu2_1 = Menu(filemenu2, tearoff=0 , bg = "#FFC34D", foreground  = "#6B3927")

    submenu1 = Menu(filemenu2, tearoff=0, bg="#FFC34D", foreground="#6B3927")
    submenu2 = Menu(filemenu2, tearoff=0, bg="#FFC34D", foreground="#6B3927")
    submenu3 = Menu(filemenu2, tearoff=0, bg="#FFC34D", foreground="#6B3927")

    filemenu2.add_cascade(label="Фон(колір)", menu=submenu1)
    filemenu2.add_cascade(label="Шрифт(колір)", menu=submenu2)
    filemenu2.add_cascade(label="Фон рамки(колір)", menu=submenu3)

    def change_color_fon(label_id):
        if label_id == 1:
            window1["bg"] = "#AF002A"
            label1["bg"] = "#AF002A"
        if label_id == 2:
            window1["bg"] = "#72A0C1"
            label1["bg"] = "#72A0C1"
        if label_id == 3:
            window1["bg"] = "#84DE02"
            label1["bg"] = "#84DE02"
        if label_id == 4:
            window1["bg"] = "#AB274F"
            label1["bg"] = "#AB274F"
        if label_id == 5:
            window1["bg"] = "#FF7E00"
            label1["bg"] = "#FF7E00"
    def change_color_font(label_id):
        if label_id == 1:
            rad1["fg"] = "#AF002A"
            rad2["fg"] = "#AF002A"
            rad3["fg"] = "#AF002A"
            label1["fg"] = "#AF002A"
            but_question["fg"] = "#AF002A"
        if label_id == 2:
            rad1["fg"] = "#72A0C1"
            rad2["fg"] = "#72A0C1"
            rad3["fg"] = "#72A0C1"
            label1["fg"] = "#72A0C1"
            but_question["fg"] = "#72A0C1" 
        if label_id == 3:
            rad1["fg"] = "#84DE02"
            rad2["fg"] = "#84DE02"
            rad3["fg"] = "#84DE02"
            label1["fg"] = "#84DE02"
        if label_id == 4:
            rad1["fg"] = "#AB274F"
            rad2["fg"] = "#AB274F"
            rad3["fg"] = "#AB274F"
            label1["fg"] = "#AB274F"
            but_question["fg"] = "#AB274F" 
        if label_id == 5:
            rad1["fg"] = "#FF7E00"
            rad2["fg"] = "#FF7E00"
            rad3["fg"] = "#FF7E00"
            label1["fg"] = "#FF7E00"
            but_question["fg"] = "#FF7E00"  
    def change_size_font(label_id):
        if label_id == 1:
            fram1["bg"] = "#AF002A"
            rad1["bg"] = "#AF002A"
            rad2["bg"] = "#AF002A"
            rad3["bg"] = "#AF002A"
        if label_id == 2:
            fram1["bg"] = "#72A0C1"
            rad1["bg"] = "#72A0C1"
            rad2["bg"] = "#72A0C1"
            rad3["bg"] = "#72A0C1"
        if label_id == 3:
            fram1["bg"] = "#84DE02"
            rad1["bg"] = "#84DE02"
            rad2["bg"] = "#84DE02"
            rad3["bg"] = "#84DE02"
        if label_id == 4:
            fram1["bg"] = "#AB274F"
            rad1["bg"] = "#AB274F"
            rad2["bg"] = "#AB274F"
            rad3["bg"] = "#AB274F"
        if label_id == 5:
            fram1["bg"] = "#FF7E00"
            rad1["bg"] = "#FF7E00"
            rad2["bg"] = "#FF7E00"
            rad3["bg"] = "#FF7E00"

    submenu1.add_command (label="Alabama-Crimson", command =lambda:change_color_fon(1)), submenu2.add_command (label="Alabama-Crimson", command= lambda:change_color_font(1)),submenu3.add_command (label="Alabama-Crimson", command = lambda:change_size_font(1))
    submenu1.add_command (label="Air-Superiority", command =lambda:change_color_fon(2)), submenu2.add_command (label="Air-Superiority", command= lambda:change_color_font(2)), submenu3.add_command (label="Air-Superiority", command = lambda:change_size_font(2))
    submenu1.add_command (label="Alien-Armpit", command =lambda:change_color_fon(3)), submenu2.add_command (label="Alien-Armpit", command= lambda:change_color_font(3)), submenu3.add_command (label="Alien-Armpit", command = lambda:change_size_font(3))
    submenu1.add_command (label="Amaranth-Purple", command =lambda:change_color_fon(4)), submenu2.add_command (label="Amaranth-Purple", command= lambda:change_color_font(4)), submenu3.add_command (label="Amaranth-Purple", command = lambda:change_size_font(4))
    submenu1.add_command (label="Amber-Sae-Ece", command =lambda:change_color_fon(5)), submenu2.add_command (label="Amber-Sae-Ece", command= lambda:change_color_font(5)), submenu3.add_command (label="Amber-Sae-Ece", command =lambda: change_size_font(5))

    label1 = Label(window1, text=question_list[0], font="Impact", bg="#FFDDCC")
    label1.pack(pady=30)
    fram1 = LabelFrame(window1)
    fram1.pack(pady=10)
    var = IntVar()
    # random.shuffle(answer_list[0])
    rad1 = Radiobutton(fram1, text=answer_list[0][0], fg="#0000FF", variable=var, value=1)
    rad2 = Radiobutton(fram1, text=answer_list[0][1], fg="#0000FF", variable=var, value=2)
    rad3 = Radiobutton(fram1, text=answer_list[0][2], fg="#0000FF", variable=var, value=3)
    rad1.pack(ipady=5, side=TOP); rad2.pack(ipady=5, side=TOP); rad3.pack(ipady=5, side=TOP)
    # rad1.place(x=10, y=70)
    # rad2.place(x=10, y=120)
    # rad3.place(x=10, y=160)

    but_question = Button(window1, text="Далі", width=12, bg="#26E600")
    but_question.place(x=200, y=265)
    but_question.bind("<Control-space>", lambda event: change(var, label1, rad1, rad2, rad3, but_question, fram1, window1, event))
    but_question.bind("<Button-1>", lambda event: change(var, label1, rad1, rad2, rad3, but_question, fram1, window1, event))
    window1.mainloop()
    
def change(var,label1,rad1,rad2,rad3,but_question,fram1, window1, event):
    global t
    global i
    global amount
    i += 1
    # random.shuffle(answer_list[0+i])
    fram1.pack(pady = 1)
    label1["text"] = question_list[0+i]
    rad1["text"] = answer_list[0+i][0]
    rad1.pack(ipady = 1, pady=0)
    rad2["text"] = answer_list[0+i][1]
    rad2.pack(ipady = 1, pady=0)
    rad3["text"] = answer_list[0+i][2]
    rad3.pack(ipady = 1, pady=0)
    but_question.place(y = 350)
    if var.get() == 1:
        var.set(0)
    if var.get() == 2:
        amount += 1
        var.set(0)
    if var.get() == 3:
        var.set(0)

    if i == 3:
        global label_photo
        image = Image.open("event.png")
        image = image.resize((300,110), Image.LANCZOS)
        image = ImageTk.PhotoImage(image)
        label_photo = Label(window1, image=image)
        label_photo.image = image
        label_photo.pack(pady=25)
    if i == 4:
        try:
            label_photo.destroy()
            fram1.destroy()
        except:
            pass

        cheack_var1 = IntVar()
        cheack_var2 = IntVar()
        cheack_var3 = IntVar()
        cheack_var4 = IntVar()

        check_1 = Checkbutton(window1, text=answer_list[0+i][0], variable=cheack_var1, onvalue=1, offvalue=0, bg="#59B300", fg="#CCCCFF")
        check_1.place(x = 200,y = 120) 
        check_2 = Checkbutton(window1, text=answer_list[0+i][1], variable=cheack_var2, onvalue=1, offvalue=0,bg="#59B300", fg="#CCCCFF")
        check_2.place(x = 200,y = 160) 
        check_3 = Checkbutton(window1, text=answer_list[0+i][2], variable=cheack_var3, onvalue=1, offvalue=0,bg="#59B300", fg="#CCCCFF")
        check_3.place(x = 200,y = 200) 
        check_4 = Checkbutton(window1, text=answer_list[0+i][3], variable=cheack_var4, onvalue=1, offvalue=0,bg="#59B300", fg="#CCCCFF")
        check_4.place(x = 200,y = 240)
        # rad2.pack(ipady = 1, pady=0)
        # rad3.pack(ipady = 1, pady=0)
        but_question.destroy()
        but_end = Button(window1,text="Завершити!",bg="#B3BFFF", font="Arial",fg="#999900")
        but_end.place(x=210, y = 330)
        but_end.bind("<Button-3>",lambda event: check_answer(cheack_var1,cheack_var2,cheack_var3,cheack_var4, event))

def check_answer(cheack_var1,cheack_var2,cheack_var3,cheack_var4,event):
    global amount
    if cheack_var1.get() == 1 and cheack_var2.get() == 1 and cheack_var3.get() == 1 and cheack_var4.get() == 1:
        amount += 1
    else:
        amount += 0
    The_end(var, t, event)

def The_end(var,t, event):
    global name
    global password
    global email
    global amount

    unique_id = str(uuid.uuid4())
    unique_id = unique_id[24:36]

    user_data =  {
        "db_id": unique_id,
        "firstname" : name,
        "password" : password,
        "email" : email,
        "point" : amount
    }

    file_name = "C:\\Users\Home\Desktop\Лаб\Лаби 2 семестр\LR25\json_users\json_info" + unique_id + '.json'
    with open(file_name,"w", encoding="utf-8") as file:
        json.dump(user_data, file, ensure_ascii=False)

    settings.my_collection.insert_one(user_data)

    window1.destroy()
    if var.get() == 1:
        var.set(0)
    elif var.get() == 2:
        amount += 1
        var.set(0)
    elif var.get() == 3:
        var.set(0)
    window2 = Tk(className="Результати")
    window2.configure(bg="#88FF4D")
    window2.geometry("550x450+440+120")
    fram1 = LabelFrame(window2, bg="#FFEEE6", text="Завершення", font="Arial", fg="#B30059")
    fram1.pack(pady=110, fill="y", expand=3)
    fram2 = LabelFrame(fram1, bg="#FFEEE6")
    fram2.pack(pady=10,fill="x", expand=2)
    fram3 = LabelFrame(fram1, bg="#FFEEE6", width=400, height=300)
    fram3.pack(pady=1)
    t = t +", "+ f"Ваші бали:{amount} / {len(question_list)}"
    label_end = Label(fram2, width=15,text=t, height=3, bg="#FFEEE6", fg="#B30059", font="Impact18")
    label_end.pack(ipady = 5, pady=5, fill=X)

    label_end2 = Label(fram3,text=f"Дякую за проходження тесту\n На все добре😉", width=30, height=3, bg="#FFEEE6",fg="#B30059",font="Arial18")
    label_end2.pack(ipady = 5, pady=5)

but_start = Button(window, text="Почати тестування!", width=15, height=4, justify=CENTER, bg="#84DE02", fg="#B30000",font="Arial", relief=GROOVE)
but_start.bind("<Button-1>", registration)
but_start.place(x=120, y=50)

window.mainloop()

