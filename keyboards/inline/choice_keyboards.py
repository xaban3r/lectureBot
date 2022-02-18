from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

subject_keyboard = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="ТС ППО",
                                                    callback_data="btn_ТС ППО"
                                                ),
                                                InlineKeyboardButton(
                                                    text="МЛ и ТА",
                                                    callback_data="btn_МЛ и ТА"
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="ЭТ",
                                                    callback_data="btn_ЭТ"
                                                ),
                                                InlineKeyboardButton(
                                                    text="СКК",
                                                    callback_data="btn_СКК"
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Электроника и схемотехника",
                                                    callback_data="btn_Электроника и схемотехника"
                                                    ),
                                                InlineKeyboardButton(
                                                    text="ОС",
                                                    callback_data="btn_ОС"
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Дискр. матем.",
                                                    callback_data="btn_Дискр. матем."
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Отмена",
                                                    callback_data="cancel"
                                                )
                                            ]
                                        ])


