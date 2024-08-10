
from aiogram.utils.keyboard import InlineKeyboardBuilder

def build_category_keyboard(categories: dict):
    builder = InlineKeyboardBuilder()
    for category in categories.keys():
        builder.button(text=category, callback_data=f"category_{category}")
    return builder.as_markup()

def build_clothes_keyboard(clothes: list, category: str):
    builder = InlineKeyboardBuilder()
    for index, cloth in enumerate(clothes):
        builder.button(text=cloth.get("title"), callback_data=f"{category}_{index}")
    return builder.as_markup()

def build_details_keyboard(cloth: dict):
    builder = InlineKeyboardBuilder()
    builder.button(text="Перейти за посиланням", url=cloth.get("url"))
    return builder.as_markup()