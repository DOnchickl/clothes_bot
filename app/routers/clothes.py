from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from ..data import *
from ..keyboards import *

clothes_router = Router()

clothes_data = load_clothes_data()   

@clothes_router.message(Command("all"))
async def show_categories_command(message: Message):
    keyboard = build_category_keyboard(clothes_data)
    await message.answer(
        text="Виберіть категорію:",
        reply_markup=keyboard,
    )


@clothes_router.callback_query(F.data.startswith("category_"))
async def show_clothes_command(callback: CallbackQuery):
    category = callback.data.split("category_")[1].strip()
    clothes = clothes_data.get(category, [])
    if clothes:
        keyboard = build_clothes_keyboard(clothes, category)
        await callback.message.answer(
            text=f"Виберіть одяг з категорії {category}:",
            reply_markup=keyboard,
        )
    else:
        await callback.message.answer(
            text=f"У категорії {category} немає доступного одягу.",
        )


@clothes_router.callback_query(F.data.startswith("clothes_"))
async def show_clothes_details_command(callback: CallbackQuery):
    parts = callback.data.split("_")
    category = "_".join(parts[:-1])
    cloth_index = int(parts[-1])

    try:
        cloth = clothes_data[category][cloth_index]
    except (KeyError, IndexError):
        await callback.message.answer("Сталася помилка при спробі отримати інформацію про одяг.")
        return

    text = f"{cloth['title']}\n{cloth['desc']}"
    keyboard = build_details_keyboard(cloth)

    await callback.message.answer_photo(
        photo=cloth['photo'],
        caption=text,
        reply_markup=keyboard,
    )
@clothes_router.callback_query(F.data.startswith("clothes_"))
async def show_clothes_details_command(callback: CallbackQuery):
    parts = callback.data.split("_")
    category = "_".join(parts[:-1])
    cloth_index = int(parts[-1])

    print(f"Selected Cloth Index: {cloth_index}")
    print(f"Category: {category}")

    try:
        cloth = clothes_data[category][cloth_index]
    except (KeyError, IndexError):
        await callback.message.answer("Сталася помилка при спробі отримати інформацію про одяг.")
        return

    text = f"{cloth['title']}\n{cloth['desc']}"
    keyboard = build_details_keyboard(cloth)

    await callback.message.answer_photo(
        photo=cloth['photo'],
        caption=text,
        reply_markup=keyboard,
    )