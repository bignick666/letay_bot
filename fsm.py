from aiogram.fsm.state import StatesGroup, State


class OtherStates(StatesGroup):
    client_name = State()
    client_phone = State()


class TryingStates(StatesGroup):
    client_name = State()
    client_phonenumber = State()
    client_experince = State()
    client_goal = State()
    comfort_place = State()
