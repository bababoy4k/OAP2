import sqlite3

# Создание базы данных и таблицы
def create_database():
  conn = sqlite3.connect('industrial_companies.db')
  cursor = conn.cursor()

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Companies (
      Code INTEGER PRIMARY KEY,
      Name TEXT,
      PhysicalAddress TEXT,
      NumberOfBranches INTEGER,
      TotalPersonnel INTEGER,
      TotalEquipmentValue REAL,
      ProductionVolume REAL,
      RegistrationDate DATE
    )
  ''')
  conn.commit()
  conn.close()

# Добавление записи в таблицу
def add_company(code, name, address, branches, personnel, equipment_value, volume, date):
  conn = sqlite3.connect('industrial_companies.db')
  cursor = conn.cursor()

  cursor.execute('''
    INSERT OR REPLACE INTO Companies (Code, Name, PhysicalAddress, NumberOfBranches, TotalPersonnel, TotalEquipmentValue, ProductionVolume, RegistrationDate)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
  ''', (code, name, address, branches, personnel, equipment_value, volume, date))

  conn.commit()
  conn.close()

# Поиск записей по различным критериям
def search_companies(criteria, value):
  conn = sqlite3.connect('industrial_companies.db')
  cursor = conn.cursor()

  cursor.execute(f'''
    SELECT * FROM Companies
    WHERE {criteria} LIKE ?
  ''', (f'%{value}%',))

  results = cursor.fetchall()
  conn.close()

  return results

# Вывод результатов поиска
def print_results(results):
  if results:
    print("Найденные предприятия:")
    for row in results:
      print(f"Код: {row[0]}, Наименование: {row[1]}, Адрес: {row[2]}, Филиалов: {row[3]}, Персонала: {row[4]}, Оборудование: {row[5]}, Выпуск: {row[6]}, Дата: {row[7]}")
  else:
    print("Предприятий не найдено.")

# Пример использования приложения
create_database()

# Добавление примеров записей
add_company(1, "АО \"Завод имени Ленина\"", "г. Москва, ул. Ленина, 1", 2, 500, 10000000, 10000000, "2023-03-15")
add_company(2, "ООО \"Технопром\"", "г. Санкт-Петербург, ул. Невского, 5", 1, 200, 5000000, 5000000, "2022-07-20")

# Поиск по названию
search_results = search_companies("Name", "Завод")
print_results(search_results)

# Поиск по адресу
search_results = search_companies("PhysicalAddress", "Москва")
print_results(search_results)
