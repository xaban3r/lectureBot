from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

up_subject_keyboard = InlineKeyboardMarkup(row_width=2,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text="ТС ППО",
                                                    callback_data="upbtn_ТС ППО"
                                                ),
                                                InlineKeyboardButton(
                                                    text="МЛ и ТА",
                                                    callback_data="upbtn_МЛ и ТА"
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="ЭТ",
                                                    callback_data="upbtn_ЭТ"
                                                ),
                                                InlineKeyboardButton(
                                                    text="СКК",
                                                    callback_data="upbtn_СКК"
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Электроника и схемотехника",
                                                    callback_data="upbtn_Электроника и схемотехника"
                                                    ),
                                                InlineKeyboardButton(
                                                    text="ОС",
                                                    callback_data="upbtn_ОС"
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Дискр. матем.",
                                                    callback_data="upbtn_Дискр. матем."
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text="Отмена",
                                                    callback_data="cancel"
                                                )
                                            ]
                                        ])
