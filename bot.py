import asyncio
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.types import Message, FSInputFile, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = os.getenv("BOT_TOKEN") or "8449771354:AAF6_ff8ZLNVUk1wYBlVzKTZZFbtYwIlY8I"

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# FSM: покупка UC
class BuyUC(StatesGroup):
    choosing_package = State()
    entering_id = State()

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    kb = ReplyKeyboardBuilder()
    kb.button(text="💎 Купить UC")
    kb.button(text="📦 Мои заказы")
    kb.button(text="ℹ️ Поддержка")
    kb.button(text="🎁 Бонусы")
    kb.button(text="📃 Политика конфиденциальности")
    kb.button(text="📄 Пользовательское соглашение")
    kb.button(text="📞 Контакты поддержки")
    kb.adjust(2)

    banner_path = "assets/ucshop_banner.jpg"
    if os.path.exists(banner_path):
        await message.answer_photo(
            FSInputFile(banner_path),
            caption="""
<b>🎮 Добро пожаловать в UC SHOP</b>
Пополняй UC безопасно через AI KASSA.
Выберите действие ниже:
""",
            reply_markup=kb.as_markup()
        )
    else:
        await message.answer("Добро пожаловать в UC SHOP!", reply_markup=kb.as_markup())

@dp.message(F.text == "💎 Купить UC")
async def buy_uc_handler(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="60 UC – 70₽", callback_data="buy_60")],
        [InlineKeyboardButton(text="325 UC – 320₽", callback_data="buy_325")],
        [InlineKeyboardButton(text="660 UC – 610₽", callback_data="buy_660")],
        [InlineKeyboardButton(text="1800 UC – 1650₽", callback_data="buy_1800")]
    ])
    await message.answer("Выберите нужный пакет UC:", reply_markup=markup)

@dp.callback_query(F.data.startswith("buy_"))
async def choose_package(callback: types.CallbackQuery, state: FSMContext):
    package = callback.data.replace("buy_", "")
    await state.update_data(package=package)
    await callback.message.answer(f"Введите ваш PUBG ID для {package} UC:")
    await state.set_state(BuyUC.entering_id)
    await callback.answer()

@dp.message(BuyUC.entering_id)
async def receive_pubg_id(message: Message, state: FSMContext):
    data = await state.get_data()
    package = data["package"]
    pubg_id = message.text

    fake_link = f"https://ai-kassa.example.com/pay?package={package}&id={pubg_id}"
    await message.answer(
        f"""✅ Ваш заказ: <b>{package} UC</b>
🎮 PUBG ID: <code>{pubg_id}</code>

💳 Оплатите по ссылке:
<a href='{fake_link}'>Перейти к оплате</a>

После оплаты UC будут зачислены в течение 5–10 минут.
""",
        disable_web_page_preview=True
    )
    await state.clear()

@dp.message(F.text == "📦 Мои заказы")
async def my_orders(message: Message):
    await message.answer("🕓 История заказов пока недоступна. Скоро будет доступна!")

@dp.message(F.text == "ℹ️ Поддержка")
async def support(message: Message):
    await message.answer("🔧 Поддержка: @OWNER_AIR\nПишите по любым вопросам.")

@dp.message(F.text == "🎁 Бонусы")
async def bonuses(message: Message):
    await message.answer("🎁 Бонус дня: скидка 10% при оплате через AI KASSA!\nАктивна до 23:59.")

@dp.message(F.text == "📃 Политика конфиденциальности")
async def privacy_policy(message: Message):
    await message.answer(
        "<b>Политика конфиденциальности</b>\n\n"
        "Мы уважаем вашу конфиденциальность и обязуемся защищать ваши данные. "
        "Вся информация, предоставленная вами, используется исключительно для обработки заказов и поддержки.\n\n"
        "Подробнее: https://example.com/privacy-policy"
    )

@dp.message(F.text == "📄 Пользовательское соглашение")
async def terms_of_service(message: Message):
    await message.answer(
        "<b>Пользовательское соглашение</b>\n\n"
        "Используя наш сервис, вы соглашаетесь с условиями предоставления услуг, "
        "которые регулируют взаимоотношения между вами и UC SHOP.\n\n"
        "Подробнее: https://example.com/terms-of-service"
    )

@dp.message(F.text == "📞 Контакты поддержки")
async def contact_support(message: Message):
    await message.answer(
        "<b>Контактные данные поддержки</b>\n\n"
        "📧 Email: k8988314@gmail.com\n"
        "📱 Telegram: @OWNER_AIR\n"
        "Наш TikTok: https://www.tiktok.com/@straxozavr?_t=ZS-8yLbVy6QnWp&_r=1\n"
        "⏰ Время работы: с 00:00 до 23:00 по МСК"
    )

async def start_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Для интеграции с FastAPI (если нужно)
if __name__ == "__main__":
    asyncio.run(start_bot())
