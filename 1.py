def custom_write(file_name, strings):
  """
  Записывает строки в файл и возвращает словарь с позициями строк.

  Args:
    file_name: Название файла для записи.
    strings: Список строк для записи.

  Returns:
    Словарь, где ключ - кортеж (номер строки, байт начала), значение - строка.
  """
  strings_positions = {}
  with open(file_name, 'w', encoding='utf-8') as f:
    for i, string in enumerate(strings, start=1):
      position = f.tell()
      strings_positions[(i, position)] = string
      f.write(string + '\n')
  return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
