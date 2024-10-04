import tkinter as tk

def calculate_remainder():
  """Вычисляет длину незанятой части отрезка."""

  try:
    a = int(entry_a.get())
    b = int(entry_b.get())

    if a <= b:
      result_label.config(text="A должно быть больше B!")
      return

    remainder = a % b  # Взятие остатка от деления нацело
    result_label.config(text=f"Длина незанятой части: {remainder}")

  except ValueError:
    result_label.config(text="Введите целые положительные числа!")

# Создание окна приложения
window = tk.Tk()
window.title("Остаток отрезка")

# Элементы ввода
label_a = tk.Label(window, text="A:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

label_b = tk.Label(window, text="B:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

# Кнопка для расчета
calculate_button = tk.Button(window, text="Рассчитать", command=calculate_remainder)
calculate_button.grid(row=2, column=0, columnspan=2)

# Метка для вывода результата
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()
