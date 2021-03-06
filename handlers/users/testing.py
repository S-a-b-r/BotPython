from aiogram import types

from loader import dp

from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from states.tests import Test

@dp.message_handler(Command("test"), state = None)
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестирование.\n"
                         "Вопрос №1 \n\n"
                         "Вы часто заниметесь бессмысленными делами(бесцельно блуждаете по интернету, клацаете пультом телевизора, бесконечно листаете ленту новостей)?")
    await Test.first()

@dp.message_handler(state = Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
        answer = message.text
        async with state.proxy() as data:
            data["answer1"] = answer
        await message.answer("Вопрос №2. \n\n"
        "Ваша память ухудшилась и вы помните то, что было давно, но забываете недавние события?")
        await Test.next()

@dp.message_handler(state = Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer2 = message.text
    data = await state.get_data()
    answer1 = data.get("answer1")
    await message.answer("Спасибо за ваши ответы!")
    await state.finish()