from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from .states import StartStates
from .keyboard import keyboard

from request import current_weather, forecast_weather
from .service import change_city, get_city  # DB-backed service functions (accept user_tg_id)


start_router = Router()



@start_router.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext) -> None:
    await message.answer("Привет я бот для получения информации о погоде отправь свой город")
    await state.set_state(StartStates.AWAITING_CITY)


@start_router.message(StartStates.AWAITING_CITY)
async def process_city(message: Message, state: FSMContext) -> None:
    city = message.text.strip()
    user_id = message.from_user.id

    weather = await current_weather(city=city)
    if weather.get("cod") != 200:
        await message.answer("Город не найден, попробуйте еще раз.")
        return

    # Save city in DB for this user
    await change_city(user_id, city)

    await message.answer(f"Вы выбрали город: {city}", reply_markup=keyboard)
    await state.clear()


@start_router.message(F.text == "Погода 🌍")
async def process_weather(message: Message) -> None:
    user_id = message.from_user.id
    city = await get_city(user_id)
    if not city:
        await message.answer("Город не установлен. Отправьте /start и укажите город.")
        return

    await message.answer("Погода сейчас")
    weather = await current_weather(city=city)
    if weather.get("cod") != 200:
        await message.answer("Город не найден, попробуйте еще раз.")
        return
    description = weather['weather'][0]['description']
    temp = weather['main']['temp']
    await message.answer(f"Погода в городе {city}:\nОписание: {description}\nТемпература: {temp}°C")


@start_router.message(F.text == "Кол-во Осадков 🌧️")
async def process_rain(message: Message) -> None:
    user_id = message.from_user.id
    city = await get_city(user_id)
    if not city:
        await message.answer("Город не установлен. Отправьте /start и укажите город.")
        return

    await message.answer("Считаю осадки на следующие 24 часа...")
    weather = await forecast_weather(city=city)
    cod = weather.get("cod")
    if str(cod) != "200":
        await message.answer("Город не найден, попробуйте еще раз.")
        return

    forecasts = weather.get("list", [])
    if not forecasts:
        await message.answer("Прогноз недоступен.")
        return

    # Sum precipitation for next 24 hours (8 entries * 3h each)
    rain_total = 0.0
    snow_total = 0.0
    for entry in forecasts[:8]:
        rain_total += float(entry.get("rain", {}).get("3h", 0) or 0)
        snow_total += float(entry.get("snow", {}).get("3h", 0) or 0)

    total = round(rain_total + snow_total, 2)
    await message.answer(
        f"Ожидаемое количество осадков в городе {city} за следующие 24 часа:\n"
        f"Дождь: {round(rain_total,2)} мм\n"
        f"Снег: {round(snow_total,2)} мм\n"
        f"Всего: {total} мм"
    )


@start_router.message(F.text == "Сменить город ◀️")
async def change_city_cmd(message: Message, state: FSMContext) -> None:
    await message.answer("Пожалуйста, введите новый город для получения информации о погоде.")
    await state.set_state(StartStates.AWAITING_CITY)
@start_router.message(F.text == "Help 🚑")
async def help_command(message: Message) -> None:
    await message.answer("Этот бот предоставляет информацию о погоде. Вы можете выбрать город и получить текущую погоду или прогноз. Используйте кнопки на клавиатуре для навигации.")

   

# You can add more handlers as needed

