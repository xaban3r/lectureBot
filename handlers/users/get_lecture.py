from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, state
from aiogram.types import ContentType, Message, CallbackQuery


from keyboards.inline.choice_keyboards import subject_keyboard
from loader import dp, bot, db
from states import Lecture


@dp.message_handler(content_types=ContentType.VIDEO)
async def get_video_id(message: Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("lecture"))
async def get_keyboard(message: types.Message):
    await message.answer("Выберите предмет: ",
                         reply_markup=subject_keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("btn_"))
async def select_subject(call=types.CallbackQuery, state=FSMContext):
    subject_name = call.data.replace("btn_", "")
    subject = await db.select_subject(subject_name=subject_name)
    try:
        lectures_count = len(subject.get("video_id"))
    except TypeError:
        await bot.send_message(call.from_user.id, f"Нет записанных лекций по предмету {subject_name}")
        await state.finish()

    await bot.send_message(call.from_user.id, f"Записанных лекций по предмету {subject_name} - "
                                              f"{lectures_count}.\nВведите номер лекции.")
    async with state.proxy() as data:
        data["subject_name"] = subject_name
        data["lectures_count"] = lectures_count
    await Lecture.S1.set()


@dp.message_handler(state=Lecture.S1)
async def send_lecture(message: types.Message, state=FSMContext):
    data = await state.get_data()
    subject_name = data.get("subject_name")
    lectures_count = data.get("lectures_count")
    subject = await db.select_subject(subject_name=subject_name)
    try:
        users_input = int(message.text)
    except ValueError:
        await message.answer("Введите число!")

    if int(message.text) <= 0 or int(message.text) > lectures_count:
        await message.answer("Число не подходит, введите еще раз")
    else:
        await message.answer(f"Предмет: {subject_name}\n"
                             f"Номер выбранной лекции: {message.text}\n")
        file_id = subject.get("video_id")[int(message.text)-1]
        await message.answer_video(video=file_id)
        await state.finish()


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("Вы отменили выбор предмета", show_alert=True)
    await call.message.edit_reply_markup()
