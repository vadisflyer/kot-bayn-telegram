def handle(msg):
    return verbatimTable.get(msg.lower())

# Matches the key exactly, ignoring the case
verbatimTable = {
    'спасибо павлу': 'Согласен)',
    'хорошо': 'Кругом пошло это чудо "хорошо"',
    'нет': 'Не солнечный ответ('
}
