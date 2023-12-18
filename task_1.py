def verification(text):
    opening_brackets = ['{']
    closing_brackets = ['}']
    stack = []

    for char in text:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return 'Ошибка: непарные скобки'
            stack.pop()

    if len(stack) != 0:
        return 'Ошибка: непарные скобки'

    placeholders = ['{' + key + '}' for key in list_keys]

    for placeholder in placeholders:
        if placeholder not in text:
            return 'Ошибка: отсутствует ключ ' + placeholder

    return 'Тест пройден'


Test_text = '''{name}, ваша запись изменена:
            ⌚️ {day_month} в {start_time}
            👩 {master}
            Услуги:
            {services}
            управление записью {record_link}'''

list_keys = ['name', 'day_month', 'day_of_week', 'start_time', 'end_time', 'master', 'services']

result = verification(Test_text)
print(result)
