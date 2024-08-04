import csv
import os
from tkinter import *

def enter(word, kotoba_kana, kotoba_kanji):
    filename = os.path.join(os.getcwd(), "eigo_nihongo.csv")
    with open(filename, "a", encoding="utf-8", newline = '') as fin:
        writer = csv.writer(fin)
        writer.writerow([word.lower(), kotoba_kana, kotoba_kanji])

def search(num:int, word): #case insensitive search
    '''
    num is 1 if word is in english, 2 if in kana and 3 if in kanji
    '''
    filename = os.path.join(os.getcwd(), "eigo_nihongo.csv")
    output = []
    with open(filename, "r", encoding="utf-8") as fout:
        reader = csv.reader(fout)
        for data in reader:
            if (num == 1): #handling case for english
                if data[num-1] == word.lower():
                    output.append(data)
            else:
                if data[num-1] == word.lower():
                    output.append(data)
    return output



def read_all():
    filename = os.path.join(os.getcwd(), "eigo_nihongo.csv")
    with open(filename, "r", encoding="utf-8") as fout:
        reader = csv.reader(fout)
        for data in reader:
            print(data)

def delete_repetitions():
    filename = os.path.join(os.getcwd(), "eigo_nihongo.csv")
    rows_dic = {}  
    #as dictionaries have O(1) average time for in operation, thus making this function O(n)
    #if we use list, it would be O(n^2)
    with open(filename, "r", encoding="utf-8") as fout:
        reader = csv.reader(fout)
        for data in reader:
            if data :
                if data[0] not in rows_dic:
                    rows_dic.update({data[0]:data[1:]})
    with open(filename, "w", encoding="utf-8", newline = '') as fin:
        writer = csv.writer(fin)
        for i in rows_dic:
            row = [i,]
            row.extend(rows_dic[i])
            writer.writerow(row)
    
'''   
enter("Japan","にほん","日本")
enter("Word","ことば","言葉")
read_all()
delete_repetitions()
read_all()
''' 

root = Tk()
root.title("Japanese word collection")
root.geometry("1000x1000")
root.config(bg="lightcoral")

heading_txt = '''
何をしたいですか？ボタンを押して下さい\nWhat do you want to do? Please press the button
'''
heading = Label(root, text = heading_txt,
                bg="yellow",
                font=("courier", 20))
heading.pack(anchor=CENTER,pady=100)

#command for add_word button

def add_word_func():
    add_word_window = Toplevel(root)
    intro_txt = '''新しい言葉を入れて下さい    Please enter a new word'''
    add_word_window.title(intro_txt)
    add_word_window.geometry("1000x1000")
    add_word_window.config(bg="#777700")

    eng_word_label = Label(add_word_window, text= "English 英語 ", 
                           font=("helvetica",26), fg="white", bg="#777700")
    eng_word_label.pack(anchor=CENTER,pady=10)
    eng_word_entry = Entry(add_word_window, width=50,font=("helvetica",26))
    eng_word_entry.pack(anchor=CENTER,pady=10)

    kana_word_label = Label(add_word_window, text= "Hiragana/Katakana ひらがな/カタカナ ", 
                            font=("helvetica",26), fg="white", bg="#777700")
    kana_word_label.pack(anchor=CENTER,pady=10)
    kana_word_entry = Entry(add_word_window, width=50,font=("helvetica",26))
    kana_word_entry.pack(anchor=CENTER,pady=10)

    kanji_word_label = Label(add_word_window, text= "Kanji 漢字 ", 
                             font=("helvetica",26), fg="white", bg= "#777700")
    kanji_word_label.pack(anchor=CENTER,pady=10)
    kanji_word_entry = Entry(add_word_window, width=50,font=("helvetica",26))
    kanji_word_entry.pack(anchor=CENTER,pady=10)

    submit = Button(add_word_window, text="Submit", font=("helvetica",26)
                    ,command=lambda: (
                                    enter(eng_word_entry.get(),kana_word_entry.get(),kanji_word_entry.get()),
                                    delete_repetitions(), 
                                    add_word_window.destroy() 
                                      ))
    submit.pack(anchor="s",pady=30)

add_txt = '''新しい言葉を入れたい\nWant to enter a new word'''
add_word = Button(root, text=add_txt ,font=("courier", 20), command=add_word_func)
add_word.pack(anchor=CENTER,pady=30)


#command for search_word button
def search_word_output(num:int , word):
    search_output_window = Toplevel(root)
    search_output_window.geometry("1000x1000")
    search_output_window.config(bg="#770077")
    output = search(num, word)
    if output == []:
        answer = Label(search_output_window, text="No answer found." , bg="#770077", fg="white", font=("",40))
        answer.pack(anchor="center", pady=50)
    for i in range(len(output)):
        txt = output[i][0] + "||" + output[i][1] + "||" +output[i][2] + " \n"
        answer = Label(search_output_window, text=txt , bg="#770077", fg="white", font=("",20))
        answer.pack(anchor="center", pady=50)

    exit_txt = '''出たい\nWant to Leave'''
    exit_screen = Button(search_output_window, text = exit_txt,font=("", 20,),
                    fg="white",
                    bg="black",
                    command=search_output_window.destroy,
                    )
    exit_screen.pack(anchor='s',pady=50)


def search_word_func():
    search_word_window = Toplevel(root)
    intro_txt = '''言葉を探して下さい   Please search the word'''
    search_word_window.title(intro_txt)
    search_word_window.geometry("1000x1000")
    search_word_window.config(bg="#770077")

    question_text = '''
    どのように探したい\nHow do you want to search
    '''
    question = Label(search_word_window, text=question_text, bg="#770077", fg="white", font=("",40))
    question.pack(anchor=CENTER,pady=30)

    selected_button = IntVar(search_word_window)

    Radiobutton(search_word_window, text="English 英語 ", variable=selected_button, value=1,font=("",20)).pack(pady=5)
    Radiobutton(search_word_window, text="Hiragana/Katakana ひらがな/カタカナ ", variable=selected_button, value=2,font=("",20)).pack(pady=5)
    Radiobutton(search_word_window, text="Kanji 漢字 ", variable=selected_button, value=3,font=("",20)).pack(pady=5)

    searched_word = Entry(search_word_window, text="Please enter/入れて下さい ", font=("",40))
    searched_word.pack(anchor=CENTER,pady=30)

    submit = Button(search_word_window, text="Submit", font=("",30),
                    fg="white",
                    bg="black",
                    command= lambda : ( search_word_output(selected_button.get(), searched_word.get()), search_word_window.destroy() )
                    )
    submit.pack(anchor='s', pady=40)

    
search_txt = '''言葉を探したい\nWant to search a word'''
search_word = Button(root, text= search_txt,font=("courier", 20), command=search_word_func)
search_word.pack(anchor=CENTER,pady=30)


exit_txt = '''出たい\nWant to Leave'''
exit_screen = Button(root, text = exit_txt,font=("Times new roman", 20,),
                    fg="white",
                    bg="black",
                    activeforeground="red",
                    command=root.destroy,
                    )
exit_screen.pack(anchor='s',pady=50)


root.mainloop()

