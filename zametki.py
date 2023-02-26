import json
import os
from datetime import datetime


def read_notes():
    if not os.path.exists("notes.json"):
        return []
    with open("notes.json") as f:
        return json.load(f)


def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=2)


def add_note():
    title = input("Введите название заметки: ")
    body = input("Введите текст заметки: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "body": body,
        "created_at": created_at,
        "updated_at": created_at,
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлено успешно!")


def edit_note():
    note_id = int(input("Введите id заметки: "))
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        print("Заметка не найдена!")
        return
    title = input(f"Введите новый заголовок для заметки {note_id}: ")
    body = input(f"Введите новый текс заметки {note_id}: ")
    note["title"] = title
    note["body"] = body
    note["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_notes(notes)
    print(f"Заметка {note_id} успешно обновлена!")


def delete_note():
    note_id = int(input("Введите идентификатор заметки: "))
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        print("Заметка не найдена!")
        return
    notes.remove(note)
    save_notes(notes)
    print(f"Заметка {note_id} успешно удалена!")


def list_notes():
    for note in notes:
        print(f"{note['id']}: {note['title']} - {note['body']} ({note['created_at']})")

notes = read_notes()

while True:
    action = input("Выбирите действие (Добавить заметку/Редактировать/Удалить/Список заметок/Выйти): ")
    if action == "Добавить заметку":
        add_note()
    elif action == "Редактировать":
        edit_note()
    elif action == "Удалить":
        delete_note()
    elif action == "Список заметок":
        list_notes()
    elif action == "Выйти":
        break
    else:
        print("Недопустимое действие, попробуйте еще раз.")
