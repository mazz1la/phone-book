import json
import os

FILENAME = "contacts.json"

def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

def add_contact():
    print("\n--- Добавление контакта ---")
    name = input("Введите имя: ").strip()
    phone = input("Введите номер телефона: ").strip()
    if not name or not phone:
        print("Ошибка: имя и номер не могут быть пустыми.")
        return
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Контакт '{name}' уже существует.")
            return
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"Контакт '{name}' успешно добавлен!")

def view_contacts():
    print("\n--- Список контактов ---")
    contacts = load_contacts()
    if not contacts:
        print("Телефонная книга пуста.")
        return
    print(f"{'№':<5} {'Имя':<20} {'Телефон':<15}")
    print("-" * 40)
    for i, contact in enumerate(contacts, start=1):
        print(f"{i:<5} {contact['name']:<20} {contact['phone']:<15}")

def search_contact():
    print("\n--- Поиск контакта ---")
    query = input("Введите имя для поиска: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if query in c["name"].lower()]
    if not results:
        print("Контакты не найдены.")
        return
    print(f"\nНайдено {len(results)} контакт(ов):")
    print(f"{'№':<5} {'Имя':<20} {'Телефон':<15}")
    print("-" * 40)
    for i, contact in enumerate(results, start=1):
        print(f"{i:<5} {contact['name']:<20} {contact['phone']:<15}")

def delete_contact():
    print("\n--- Удаление контакта ---")
    name = input("Введите имя контакта для удаления: ").strip()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    if len(new_contacts) == len(contacts):
        print(f"Контакт '{name}' не найден.")
        return
    save_contacts(new_contacts)
    print(f"Контакт '{name}' успешно удалён!")

def main():
    print("=" * 40)
    print("      ТЕЛЕФОННАЯ КНИГА - ПРОСМОТР")
    print("=" * 40)
    while True:
        print("\nВыберите действие:")
        print(" 1. Добавить контакт")
        print(" 2. Просмотреть все контакты")
        print(" 3. Найти контакт")
        print(" 4. Удалить контакт")
        print(" 0. Выход")
        choice = input("\nВаш выбор: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
