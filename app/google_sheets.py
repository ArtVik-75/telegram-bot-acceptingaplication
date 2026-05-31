import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("Заявки ТГ бота тест").sheet1


def add_application(name, age, phone, comment):
    print("Пытаюсь записать в таблицу")

    sheet.append_row([
        name,
        age,
        phone,
        comment
    ])

    print("Запись добавлена")