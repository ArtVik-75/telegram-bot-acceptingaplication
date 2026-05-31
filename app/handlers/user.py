from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Bot


from app.keyboards.reply import main_keyboard
from app.states.form import Form
from app.config import ADMIN_ID
from app.google_sheets import add_application


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выбери действие:",
        reply_markup=main_keyboard
    )

@router.message(F.text == "Оставить заявку")
async def start_form(message: Message, state: FSMContext):

    await state.set_state(Form.name)

    await message.answer("Введите ваше имя:")

@router.message(Form.name)
async def get_name(message: Message, state: FSMContext):

    await state.update_data(name=message.text)

    await state.set_state(Form.age)

    await message.answer("Введите ваш возраст:")

@router.message(Form.age)
async def get_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
       return await message.answer("Ошибка! Введите, пожалуйста ваш  возраст только цифрами (Например: 25)")

    await state.update_data(age=int(message.text))

    await state.set_state(Form.phone)

    await message.answer("Введите ваш номер телефона:")

@router.message(Form.phone)
async def get_phone(message: Message, state: FSMContext):

    await state.update_data(phone=message.text)

    await state.set_state(Form.comment)

    await message.answer("Введите ваш комментарий к заказу:")

@router.message(Form.comment)
async def get_comment(message: Message, state: FSMContext):

    await state.update_data(comment=message.text)

    data = await state.get_data()

    
    add_application(
        data["name"],
        data["age"],
        data["phone"],
        data["comment"]
    )

    await message.answer(
        f"Спасибо за заявку!\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Телефон: {data['phone']}\n"
        f"Комментраий: {data['comment']}"
    )

    await message.bot.send_message(
      ADMIN_ID,
        f"Новая заявка!\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Телефон: {data['phone']}\n"
        f"Комментарий: {data['comment']}"
)

    await state.clear()
