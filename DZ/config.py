from enum import Enum

# Токент бота
TOKEN = '5025555758:AAGyQBKiYzbYYH3QkeU_sj9P78sOzn_Ipcs'

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
#CURRENT_STATE = "CURRENT_STATE"

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_NAME = "STATE_NAME"
    STATE_AGE = "STATE_AGE"
    STATE_OPERATION = "STATE_OPERATION"