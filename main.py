from data import pump_list
from pump_model import PumpModel
from pump_checker import PumpChecker
from tkinter import *


pumps = []


def calculate():
    answer = float(txt.get())
    # Make a pump list from database
    for pump in pump_list:
        pump_model = pump["model"]
        pump_mph = pump["M3PH"]
        pump_lph = pump["LPH"]
        pump_connect = pump["connect"]
        pump_size = pump["size"]
        new_pump = PumpModel(pump_model, pump_mph, pump_lph, pump_connect, pump_size)
        pumps.append(new_pump)

    # Request vessel volume
    user_answer = answer

    # Add pump checker
    check_pump = PumpChecker(user_answer, pumps)

    needed_pump = check_pump.pump_finder()

    # Take info from a needed pump
    model = needed_pump.model
    mph = needed_pump.mph
    lph = needed_pump.lph
    connect = needed_pump.connect
    size = needed_pump.size

    info['text'] = f"Объем рубашки составит: {check_pump.jacket_volume} л. \n " \
                   f"Минимальная производительность насоса: {check_pump.circulate_volume} л. \n" \
                   f"----- \n" \
                   f"Харатеристики подходящего насоса: \n" \
                   f"Модель: {model} \n" \
                   f"Производительность м3/ч: {mph} \n" \
                   f"Производительность л/мин: {lph} \n" \
                   f"Присоединение: {connect} \n" \
                   f"Диаметр трубопровода: {size}" \


root = tkinter.Tk()
root.title("Подбор насоса")
root.geometry("300x200")

title = tkinter.Label(root, text="Введите объем сосуда в литрах")
title.grid(column=0, row=0, columnspan=2)

txt = tkinter.Entry(root)
txt.grid(column=0, row=1)

btn = tkinter.Button(root, text="Расчет", command=calculate)  # функция указывается без вызова
btn.grid(column=1, row=1)

info = tkinter.Label(root, text="Результаты расчета", anchor='nw')
info.grid(column=0, row=2, columnspan=2, rowspan=2)

root.mainloop()
