from tkinter import *
from tkinter import font


currencies = ["Euro", "Dollar US", "Pound", "Franc FRF", "Peso", "Yen"]
# ref euro
# 20 janv., 09:22 UTC
currencies_value = [1.0, 1.08355, 0.877777645, 6.5595679391, 20.5785434, 140.2063117]   # 1E8
currencies_symbol = ["€", "$", "£", "FRF", "$ MXN", "¥"]


def convert():
    global converted_field
    if len(to_convert_field.get()) > 0:
        try:
            to_convert = float(to_convert_field.get())
            converted_field.delete(0, END)

            value_from = currencies_value[currencies.index(currency_from.get())]
            value_to = currencies_value[currencies.index(currency_to.get())]

            result = (to_convert / value_from) * value_to
            converted_field.insert(0, result)
            add_to_history(str(to_convert) + " " + currencies_symbol[currencies.index(currency_from.get())] + " → " + str(result) + " " + str(currencies_symbol[currencies.index(currency_to.get())]))

        except:
            converted_field.delete(0, END)
            converted_field.insert(0, "Donnée invalide !")


def intervert_from_to():
    from_old = currency_from.get()
    to_old = currency_to.get()
    currency_from.set(to_old)
    currency_to.set(from_old)


def add_to_history(text):
    history_list.insert(END, text)


window = Tk(className="Convertisseur de Monnaie")
font.nametofont("TkDefaultFont").configure(size=12)
window.geometry("564x472")
window.resizable(width=False, height=False)

convert_frame = Frame(window, padx=16, pady=24)
result_frame = Frame(window, padx=16, pady=8)

# Frames
amount_label = Label(convert_frame, text="Quantité:", padx=16)
amount_label.grid(row=1, column=1, pady=8)
to_convert_field = Entry(convert_frame, relief="sunken", borderwidth=6, font=('Arial', 14))
to_convert_field.grid(row=1, column=2, pady=8)

# OptionMenu FROM
currency_from_label = Label(convert_frame, text="De:", padx=16)
currency_from_label.grid(row=2, column=1)
currency_from = StringVar()
currency_from.set(currencies[0])
convert_from_option = OptionMenu(convert_frame, currency_from, *currencies)
convert_from_option.grid(row=2, column=2)

# OptionMenu TO
currency_to_label = Label(convert_frame, text="À:", padx=16)
currency_to_label.grid(row=3, column=1)
currency_to = StringVar()
currency_to.set(currencies[1])
convert_to_option = OptionMenu(convert_frame, currency_to, *currencies)
convert_to_option.grid(row=3, column=2)

# intervert Button
intervert_button = Button(convert_frame, text="↕", borderwidth=4, font=('Arial', 18), command=lambda :intervert_from_to())
intervert_button.grid(row=2, column=3, rowspan=2)

# CONVERT Button
convert_button = Button(result_frame, borderwidth=6, text="Convertir", command=lambda :convert())
convert_button.grid(row=1, column=1, columnspan=2, pady=16)

# Converted FIELD
amount_converted_label = Label(result_frame, text="Quantité Convertie:", padx=16)
amount_converted_label.grid(row=2, column=1)
converted_field = Entry(result_frame, relief="sunken", borderwidth=6, font=('Arial', 14))
converted_field.grid(row=2, column=2)

# History
history_frame = Frame(window, pady=8)
history_list = Listbox(history_frame, width=50, height=6)
history_list.grid(column=0, row=0, sticky=(N, W, E, S))
scrollbar = Scrollbar(history_frame, orient=VERTICAL, command=history_list.yview)
scrollbar.grid(column=1, row=0, sticky=(N, S))
history_list['yscrollcommand'] = scrollbar.set
history_frame.grid_columnconfigure(0, weight=1)
history_frame.grid_rowconfigure(0, weight=1)

convert_frame.pack()
result_frame.pack()
history_frame.pack()

window.mainloop()