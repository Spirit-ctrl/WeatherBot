from aiogram.fsm.state import StatesGroup, State

class StartStates(StatesGroup):
    AWAITING_CITY = State()