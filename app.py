from tkinter import *


def convert_to_km():
    miles = float(miles_input.get())
    km = float(miles) * 1.609
    kilometer_result_label.config(text=f'{str(round(km))}')


window = Tk()
window.title('Miles converter')
# window.minsize(width=400, height=400)
window.config(padx=100, pady=25)

miles_input = Entry(width=7)
miles_input.grid(columns=2, row=1)

miles_label = Label(text='Miles: ')
miles_label.grid(columns=1, row=0)

is_equal_label = Label(text='is equal to (km): ')
is_equal_label.grid(columns=1, row=2)

kilometer_result_label = Label(text='0')
kilometer_result_label.grid(columns=2, row=3)

# kilometer_label = Label(text='km')
# kilometer_label.grid(columns=3, row=3)
# kilometer_label.config(padx=2, pady=0)

calculate_button = Button(text='Calculate', command=convert_to_km)
calculate_button.grid(columns=2, row=5)

window.mainloop()
