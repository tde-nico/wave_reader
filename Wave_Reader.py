import matplotlib.pyplot as plt
import numpy as np
import tkinter as tkr
import optparse

# Version: 1.1.1

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-f", "--file", dest="file_name", help='The file name to get to create a plot')
	(options, arguments) = parser.parse_args()
	return options


def generate_wave(file_name=None):
    if not file_name:
        file_name = entry.get()

    wave_data = np.genfromtxt(file_name, delimiter=',', names=['time','volt'])
    wave_data['volt'][0] = wave_data['volt'][1]
    
    max_volt = np.average(wave_data['volt']) * 2
    value_error = max_volt * (5 / 100)
    
    for volt in range(len(wave_data['volt'])):
        if wave_data['volt'][volt] > max_volt + value_error:
            wave_data['volt'][volt] = max_volt
        elif wave_data['volt'][volt] < -value_error:
            wave_data['volt'][volt] = 0
    
            
    plt.plot(wave_data['time'], wave_data['volt'])
    plt.show()


options = get_arguments()

if options.file_name:
    file_name = options.file_name
    generate_wave(file_name)
    
else:
    display = tkr.Tk()
    display.title('Wave Reader')
    display.geometry('200x100')
        
    text1 = tkr.Label(display, text = 'File Name')
    text1.pack()
    canvas = tkr.Canvas(display, width = 200, height = 25,  relief = 'raised')
    canvas.pack(fill='x')
    entry = tkr.Entry(display) 
    canvas.create_window(100, 10, window=entry)
        
    botton1 = tkr.Button(display, width = 5, height = 3, text = 'Generate', command = generate_wave)
    botton1.pack(fill='x')

    display.mainloop()
