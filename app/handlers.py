from aiogram import F, Router
from aiogram.types import Message, InputFile
from aiogram.filters import CommandStart, Command 
import os

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import app.keyboards as kb

router=Router()

# список команд на клавиатуре
@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer(
    "👋 Привет!\n\n"
    "Ты попал в Eco-Scan — бот, который помогает нам строить экологичное будущее 🌍♻️.\n\n"
    "📌 Наша цель — собрать фотографии повседневного мусора, чтобы обучить нейросеть различать отходы и подсказывать, как их правильно сортировать.\n\n"
    "📸 Что нужно делать?\n"
    "1️⃣ Нажми кнопку «Отправить фото 📷».\n"
    "2️⃣ Сфотографируй или загрузи мусор, который у тебя под рукой: бутылки 🍼🥤, пачки от сладостей 🍫, стаканчики ☕, пакеты и многое другое ♻️.\n"
    "3️⃣ Отправь фото в чат — и ты внесёшь свой вклад в наш датасет.\n\n"
    "✨ Каждое фото помогает нам сделать мир чище.\n"
    "Спасибо, что присоединился к нам 💚!",
                        reply_markup=kb.main_kb)
    
@router.message(F.text == kb.CALLBACK_BUTTON_ABOUT)
async def get_info(message:Message):
    await message.answer(
        '🌍 Мы — студенческая команда, работающая над экологичным проектом Eco Scan.\n'
        'Наша цель — научить искусственный интеллект распознавать отходы и помочь людям сортировать мусор правильно ♻️.\n'
        'Почему это важно?\n\n'
        '✨ Сегодня огромная часть отходов оказывается на свалках и загрязняет природу.\n'
        '✨ Многие люди не знают, как правильно сортировать мусор, и нуждаются в простом инструменте-помощнике.\n'
        '✨ Мы верим, что технологии могут стать союзником экологии 🌱.\n\n'
        '📸 Каждое фото, которое вы отправляете через бота, попадает в датасет и помогает нам обучать нейросеть.\n'
        'Чем больше изображений — тем умнее становится модель, тем точнее она сможет подсказывать, куда выбросить бутылку, стакан или бумагу.\n\n'
        'Ваш вклад = чище планета 💚.\n\n'
        'Спасибо, что вы вместе с нами создаёте будущее без лишнего мусора 🌍✨.\n'
        )


@router.message(F.text == kb.CALLBACK_BUTTON_HELP)
async def get_info(message:Message):
    await message.answer(
    "📸 Как пользоваться ботом:\n"
    "1️⃣ Нажмите кнопку «Отправить фото 📷».\n"
    "2️⃣ Сфотографируйте или загрузите изображение любого повседневного мусора, который у вас есть под рукой:\n\n"
    "   • пластиковые бутылки 🍼🥤,\n"
    "   • пачки от сладостей 🍫,\n"
    "   • стаканчики ☕,\n"
    "   • бумажки, пакеты и другое ♻️.\n\n"
    '3️⃣ Отправьте фото в чат — бот автоматически сохранит его в наш датасет.\n\n'
    "Почему это важно?\n"
    "✨ Чем больше разнообразных фото, тем лучше обучается наша нейросеть.\n"
    "✨ Даже одно ваше фото приближает нас к тому, чтобы бот в будущем сам подсказывал, куда выбросить тот или иной предмет.\n\n"
    "💡 Подсказка: фотографируйте так, чтобы предмет был хорошо виден, но необязательно идеально — нам нужны реальные снимки из повседневной жизни.\n\n"
    "Спасибо, что помогаете нам строить экологичное будущее 🌍💚!"
    )

@router.message(F.text == kb.CALLBACK_BUTTON_SEND)
async def send_phot(message: Message):
    await message.answer('Отправка фотографий 📸',
                        reply_markup=kb.recycling_kb)
    
@router.message(F.text == 'Назад')
async def exit_kb(message: Message):
    await message.answer('Выход ⬅️',
                        reply_markup=kb.main_kb)

class DataForm(StatesGroup):
    waiting_photo = State()

async def ask_for_photo(message: Message, state: FSMContext, category: str):
    await  message.answer("Можете отправить ваше фото 😇",
                        reply_markup = kb.recycling_all)
    await state.update_data(category=category)
    await state.set_state(DataForm.waiting_photo)

async def ask_for_trash_photo(message: Message, state: FSMContext, category: str):
    await  message.answer("Можете отправить ваше фото 😇",
                        reply_markup = kb.recycling_trash_all)
    await state.update_data(category=category)
    await state.set_state(DataForm.waiting_photo)

@router.message(F.text == kb.CALLBACK_BUTTON_PLASTIC)
async def plastic_handler(message: Message, state: FSMContext):
    await ask_for_photo(message, state, "plastic")

@router.message(F.text == kb.CALLBACK_BUTTON_GLASS)
async def glass_handler(message: Message, state: FSMContext):
    await ask_for_photo(message, state, "glass")

@router.message(F.text == kb.CALLBACK_BUTTON_PAPER)
async def paper_handler(message:Message, state: FSMContext):
    await ask_for_photo(message, state, "paper")

#попытка сделать сохранение общего мусора
@router.message(F.text == kb.CALLBACK_BUTTON_ALL)
async def trash_handler(message:Message, state: FSMContext):
    # await message.answer('Можете отправить ваше фото 😇')
    await ask_for_trash_photo(message, state, "trash")

@router.message(F.photo, DataForm.waiting_photo)
async def save_photo(message:Message, state: FSMContext):
    data = await state.get_data()
    category = data.get("category", "other")
    photo = message.photo[-1]
    safe_id = photo.file_unique_id.strip('-')
    base_dir = os.path.join(os.path.dirname(__file__), "..", "photos", category)
    file_name = os.path.join(base_dir, f"{message.from_user.id}_{safe_id}.jpg")
    file = await message.bot.get_file(photo.file_id)
    await message.bot.download_file(file.file_path, destination=file_name)
    await message.answer('Фото успешно сохранено, спасибо 💚!')
    await state.clear()

@router.message(F.text == kb.CALLBACK_BUTTON_BACK)
async def exit_kb(message: Message):
    await message.answer(kb.CALLBACK_BUTTON_BACK,
                        reply_markup=kb.recycling_kb)
    
@router.message(F.text == kb.CALLBACK_BUTTON_ALL_WHAT)
async def tell_info(message: Message):
    await message.answer(
        '🌍♻ Что нельзя сортировать и сдавать на переработку?\n'
        'Есть предметы, которые относятся к общему мусору и не принимаются на переработку:\n\n'
        '🚫 Неожиданные примеры:\n'
        '   •Зеркала и стеклянная посуда (имеют специальные покрытия и примеси).\n'
        '   •Пенопласт и пенополистирол (очень трудно перерабатываются).\n'
        '   •Одноразовая посуда с жировыми/пищевыми остатками.\n'
        '   •Фарфор, керамика и термостойкое стекло.\n'
        '   •Грязные пакеты от молока/кефира, тетрапак без промывки.\n'
        '   •Средства личной гигиены (маски, перчатки, ватные палочки, подгузники).\n\n'
        '❗Такие вещи не принимают пункты переработки и их нужно выбрасывать в общий контейнер.\n'
    )
    
