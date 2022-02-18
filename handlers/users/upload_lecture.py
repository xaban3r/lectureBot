from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentType

from filters import AdminFilter
from keyboards.inline.upload_keyboard import up_subject_keyboard
from loader import dp, bot, db
from aiogram.dispatcher.filters import Command

from states import UploadLecture


@dp.message_handler(Command("upload"), AdminFilter())
async def lecture_upload(message: types.Message, state=FSMContext):
    await message.answer("Загрузить лекцию по предмету: ",
                         reply_markup=up_subject_keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("upbtn_"))
async def select_subject(call=types.CallbackQuery, state=FSMContext):
    subject_name = call.data.replace("upbtn_", "")
    await bot.send_message(call.from_user.id, f" Отправляй видос по предмету {subject_name}, бро")
    async with state.proxy() as data:
        data["subject_name"] = subject_name
    await UploadLecture.U1.set()


@dp.message_handler(state=UploadLecture.U1, content_types=ContentType.VIDEO)
async def send_lecture(message: types.Message, state=FSMContext):
    data = await state.get_data()
    subject_name = data.get("subject_name")
    video_id = message.video.file_id
    subject = await db.select_subject(subject_name=subject_name)
    file_id = subject.get("video_id")
    if type(file_id) == type(None):
        file_id = []
    file_id.append(video_id)
    await db.add_lecture(subject_name=str(subject_name), video_id=file_id)
    await state.finish()


@dp.message_handler(state=UploadLecture.U1, content_types=ContentType.ANY)
async def try_again(message: types.Message, state=FSMContext):
    await message.answer("Братишка, все ошибаются, отправь видос :)")
    await state.finish()
