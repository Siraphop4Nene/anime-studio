from tkinter import *
from tkinter.ttk import Treeview

import factory as f

factory = f.Factory()


def anime_data():
    anime_list = factory.get_all_anime()
    for anime in anime_list:
        tree.insert('', 'end', values=(int(anime.id), anime.name, int(anime.studio_id), int(anime.ep)))


def studio_data():
    studio_list = factory.get_all_studios()
    for studio in studio_list:
        tree2.insert('', 'end', values=(int(studio.id), studio.name))


def refresh_table():
    clear_studio_table()
    clear_anime_table()
    anime_data()
    studio_data()


def clear_anime_table():
    tree.delete(*tree.get_children())


def clear_studio_table():
    tree2.delete(*tree2.get_children())


def get_anime_from_anime_id():
    anime_id = anime_entry.get()
    anime = factory.get_anime_by_id(int(anime_id))
    return anime


def get_studio_from_studio_id():
    studio_id = studio_entry.get()
    studio = factory.get_studio_by_id(int(studio_id))
    return studio


def search_studio_id():
    studio_id = studio_search_entry.get()
    try:
        int(studio_id)
    except ValueError:
        print("Please enter a valid studio id")
        return
    clear_studio_table()
    studio = factory.get_studio_by_id(int(studio_id))
    tree2.insert('', 'end', values=(int(studio.id), studio.name))


def search_anime_id():
    anime_id = anime_search_entry.get()
    try:
        int(anime_id)
    except ValueError:
        print("Please enter a valid anime id")
        return
    clear_anime_table()
    anime = factory.get_anime_by_id(int(anime_id))
    tree.insert('', 'end', values=(int(anime.id), anime.name, int(anime.studio_id), int(anime.ep)))


def update_anime_data():
    anime = get_anime_from_anime_id()
    anime_id = anime_entry.get()
    anime_name = name_entry.get()
    studio_id = studio_entry.get()
    ep = ep_entry.get()
    factory.update_anime(anime, int(anime_id), anime_name, int(studio_id), int(ep))
    factory.commit()
    refresh_table()


def update_studio_data():
    studio = get_studio_from_studio_id()
    studio_id = studio_entry.get()
    studio_name = studio_name_entry.get()
    factory.update_studio(studio, int(studio_id), studio_name)
    factory.commit()
    refresh_table()


def add_anime():
    anime_name = name_entry.get()
    studio_id = studio_entry.get()
    ep = ep_entry.get()
    factory.add_anime(anime_name, int(studio_id), int(ep))
    factory.commit()
    refresh_table()


def add_studio():
    studio_name = studio_name_entry.get()
    factory.add_studio(studio_name)
    factory.commit()
    refresh_table()


def delete_anime():
    anime = anime_entry.get()
    factory.delete_anime(int(anime))
    factory.commit()
    refresh_table()


def delete_studio():
    studio = studio_entry.get()
    factory.delete_studio(int(studio))
    factory.commit()
    refresh_table()


app = Tk()
frame_search = Frame(app)
frame_search.grid(row=0, column=0)

lbl_search = Label(frame_search, text='Search by anime ID',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=0, column=0, sticky=W)
anime_search = StringVar()
anime_search_entry = Entry(frame_search, textvariable=anime_search)
anime_search_entry.grid(row=0, column=1)

lbl_search = Label(frame_search, text='Search by studio ID',
                   font=('bold', 12), pady=20)
lbl_search.grid(row=1, column=0, sticky=W)
studio_search = StringVar()
studio_search_entry = Entry(frame_search, textvariable=studio_search)
studio_search_entry.grid(row=1, column=1)

frame_fields = Frame(app)
frame_fields.grid(row=1, column=0)
# anime id
anime_id = StringVar()
anime_label = Label(frame_fields, text='AnimeID', font=('bold', 12))
anime_label.grid(row=0, column=0, sticky=E)
anime_entry = Entry(frame_fields, textvariable=anime_id)
anime_entry.grid(row=0, column=1, sticky=W)
# anime name
name_text = StringVar()
name_label = Label(frame_fields, text='Name', font=('bold', 12))
name_label.grid(row=0, column=2, sticky=E)
name_entry = Entry(frame_fields, textvariable=name_text)
name_entry.grid(row=0, column=3, sticky=W)
# studio id
studio_text = StringVar()
studio_label = Label(frame_fields, text='StudioID', font=('bold', 12))
studio_label.grid(row=1, column=0, sticky=E)
studio_entry = Entry(frame_fields, textvariable=studio_text)
studio_entry.grid(row=1, column=1, sticky=W)
# episode
ep_text = StringVar()
ep_label = Label(frame_fields, text='Number of Episodes', font=('bold', 12), pady=20)
ep_label.grid(row=1, column=2, sticky=E)
ep_entry = Entry(frame_fields, textvariable=ep_text)
ep_entry.grid(row=1, column=3, sticky=W)

# studio name
studio_name_text = StringVar()
studio_name_label = Label(frame_fields, text='Studio Name', font=('bold', 12))
studio_name_label.grid(row=2, column=0, sticky=E)
studio_name_entry = Entry(frame_fields, textvariable=studio_name_text)
studio_name_entry.grid(row=2, column=1, sticky=W)

frame_buttons = Frame(app)
frame_buttons.grid(row=2, column=0)

search_anime_btn = Button(frame_buttons, text='Search anime', width=12, command=search_anime_id)
search_anime_btn.grid(row=0, column=0, pady=20)
search_studio_btn = Button(frame_buttons, text='Search studio', width=12, command=search_studio_id)
search_studio_btn.grid(row=0, column=1, pady=20)
update_anime_btn = Button(frame_buttons, text='Update anime', width=12, command=update_anime_data)
update_anime_btn.grid(row=0, column=2, pady=20)
update_studio_btn = Button(frame_buttons, text='Update studio', width=12, command=update_studio_data)
update_studio_btn.grid(row=0, column=3, pady=20)
add_anime_btn = Button(frame_buttons, text='Add anime', width=12, command=add_anime)
add_anime_btn.grid(row=1, column=0, pady=20)
add_studio_btn = Button(frame_buttons, text='Add studio', width=12, command=add_studio)
add_studio_btn.grid(row=1, column=1, pady=20)
delete_anime_btn = Button(frame_buttons, text='Delete anime', width=12, command=delete_anime)
delete_anime_btn.grid(row=1, column=2, pady=20)
delete_studio_btn = Button(frame_buttons, text='Delete studio', width=12, command=delete_studio)
delete_studio_btn.grid(row=1, column=3, pady=20)
refresh_btn = Button(frame_buttons, text='Refresh', width=12, command=refresh_table)
refresh_btn.grid(row=1, column=4, pady=20)

frame = Frame(app)
frame.grid(row=3, column=0, columnspan=4, rowspan=6, pady=20, padx=20)

tree = Treeview(frame, columns=('AnimeID', 'Name', 'StudioID', 'Episodes'))
tree.column('AnimeID', width=55)
tree.heading('AnimeID', text='AnimeID')
tree.column('Name', width=250)
tree.heading('Name', text='Name')
tree.column('StudioID', width=50)
tree.heading('StudioID', text='StudioID')
tree.column('Episodes', width=100)
tree.heading('Episodes', text='Episodes')
tree.grid(row=0, column=0, columnspan=4, rowspan=6, pady=20, padx=20)
anime_data()

tree2 = Treeview(frame, columns=('StudioId', 'StudioName'))
tree2.heading('StudioId', text='StudioId')
tree2.heading('StudioName', text='StudioName')
tree2.column('StudioId', width=50)
tree2.column('StudioName', width=250)
tree2.grid(row=0, column=20, columnspan=4, rowspan=6, pady=20, padx=20)
studio_data()

app.title('Anime Database')
app.geometry('1400x700')
app.mainloop()
