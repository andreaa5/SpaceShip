import os
from dotenv import load_dotenv
import requests 
from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import threading


api_key = #add your api key here - can be found on https://api.nasa.gov/
api_url = f"https://api.nasa.gov/neo/rest/v1/neo/browse"
api_search_url = f'https://api.nasa.gov/neo/rest/v1/feed'
#start_date=START_DATE&end_date=END_DATE&api_key=API_KEY 
weather_api = 'https://api.nasa.gov/DONKI/'

red_color = "#470e09"
gray_color = "#2b2b2b"
black = "#000"
black_second = "#1c1c1c"
dark_mode = "#1f1e1d"
purple = "#1e0430"

def fetch_asteroid_news():
    response = requests.get(api_search_url + '?api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        return data
    else:
        print("Couldn't receive the data.")


class SpaceShipCommanderApp():
#Window
    def __init__(self):
        self.win = Tk()
        self.win.title("Welcome commander")
        self.win.geometry("1920x1080")
        self.win.resizable(width=False, height=False)
        #win["bg"] = "black"

        self.search_term = tk.StringVar()
        self.start_date = tk.StringVar()
        self.end_date = tk.StringVar()

        self.api_processing = False

        self.weather_start_date = tk.StringVar()
        self.weather_end_date = tk.StringVar()

        self.start_date_string = self.start_date.get()
        self.end_date_string = self.end_date.get()
        self.size = 0
        self.names_array = []
        self.hazardous_status = []
        self.last_observation_dates = []
        self.weather_type = tk.StringVar()

        self.cme_activity_ids = []
        self.cme_start_time = []
        self.cme_note = []
        
        #GST VARIABLES 
        self.gst_ids = []
        self.gst_start_time = []
        
        #FLR VARIABLES
        self.flr_ids = []
        self.flr_begin_time = []
        self.flr_peak_time = []
        self.flr_end_time = []
        self.flr_class_type = []
        self.flr_source_location = []
        self.flr_notes = []

        #SEP VARIABLES
        
        self.sep_ids = []
        self.sep_event_time = []

        #MPC VARIABLES

        self.mpc_ids = []
        self.mpc_event_time = []

        #RBE VARIABLES

        self.rbe_ids = []
        self.rbe_event_time = []
        
        #HSS VARIABLES

        self.hss_ids = []
        self.hss_event_time = []

        self.main_frame = tk.Frame(self.win, bg=dark_mode, pady=40)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        button1 = tk.Button(self.main_frame, 
                    command=lambda:openNewWindow(self, self.start_date, self.end_date),
                    background=black_second, 
                    foreground='#3a34eb', 
                    activebackground=gray_color,
                    highlightthickness=2,
                    highlightbackground=black_second,
                    highlightcolor='#3a36ad',
                    width=13,
                    height=4,
                    border=0,
                    cursor='hand1',
                    text = 'Asteroids',
                    font=('Arial', 20, 'bold')
                   )
        button1.grid(column=0, row=0)

        button2 = tk.Button(self.main_frame, 
                            command=lambda:weatherWindow(self, self.weather_start_date, self.weather_end_date),
                            background=black, 
                            foreground='#3a36ad', 
                            activebackground=gray_color,
                            highlightthickness=2,
                            highlightbackground=black_second,
                            highlightcolor='WHITE',
                            width=13,
                            height=4,
                            border=0,
                            cursor='hand1',
                            text = 'Weather',
                            font=('Arial', 20, 'bold')
                        )
        button2.grid(column=1, row=0)
        
        def flash(self):
            color="blue"
            if self.color_ind:
                color="red"
            self.canvas.itemconfigure(self.circle, fill=color)
            self.color_ind=not self.color_ind
            self.canvas.after(1500, lambda:flash(self))

        self.canvas = tk.Canvas(self.main_frame, height=400, width=400, bg=dark_mode, border=0, highlightthickness=0)
        self.canvas.grid(column=0, row=1)
        self.circle = self.canvas.create_oval(50,40,350,350,outline = "black",fill = "blue",width = 4)
        self.color_ind=True
        flash(self)

        self.second_canvas = tk.Canvas(self.main_frame, height=400, width=400, bg=dark_mode, border=0, highlightthickness=0)
        self.second_canvas.grid(column=1, row=1)
        self.second_canvas.create_line(200,350,200,35, fill="black", width=5)
        self.second_canvas.create_rectangle(80,350,320,300, fill='red')

        def bt1_enter(event):
            button1.config(
                highlightcolor='#3a36ad'
            )

        def bt1_leave(event):
            button1.config(
                highlightcolor=black_second
            )

        def bt2_enter(event):
            button2.config(
                highlightcolor=gray_color
            )

        def bt2_leave(event):
            button2.config(
                highlightcolor=black_second
            )

        button1.bind('<Enter>', bt1_enter)
        button1.bind('<Leave>', bt1_leave)

        button2.bind('<Enter>', bt2_enter)
        button2.bind('<Leave>', bt2_leave)

        def choose_type(type):
            print(type)
            self.weather_type.set(type)
        
        #open asteroids window
        def openNewWindow(self, start_date, end_date):

            newWindow = Toplevel(self.win)
            newWindow.configure(bg=dark_mode)
            
            main_frame = tk.Frame(newWindow, bg=dark_mode, pady=40)
            main_frame.pack(fill=tk.BOTH, expand=True)
            main_frame.columnconfigure(0, weight=1)
            main_frame.columnconfigure(1, weight=1)
            main_frame.columnconfigure(2, weight=1)
            main_frame.rowconfigure(0, weight=1)
            main_frame.rowconfigure(1, weight=1)
            main_frame.rowconfigure(2, weight=1)
            main_frame.rowconfigure(3, weight=1)
            main_frame.rowconfigure(4, weight=1)
            main_frame.rowconfigure(5, weight=1)
            main_frame.rowconfigure(6, weight=1)

        
            #newWindow.title("Astronomy picture of the day")
            newWindow.title("Asteroid data")
            
            # sets the geometry of toplevel
            newWindow.geometry("2500x1000")

            ttk.Label(main_frame, text = 'Enter the start and end date in the format like year-month-day', 
                      background=dark_mode, 
                      foreground='#3b73cc', 
                      font =("Courier", 15)).grid(column=1,row=0)


            ttk.Label(main_frame, text = 'Greetings! Give me information on near earth objects that we observed in the period between',
                      background=dark_mode, 
                      foreground='#3b73cc', 
                      font =("Courier", 15)).grid(column=1,row=1)

        
            '''ttk.Label(newWindow, text = 'Start date:',
                      background=dark_mode, 
                      foreground='#3b73cc', 
                      font =("Courier", 15)).grid(column=0, row=2)'''
            
            tk.Entry(main_frame,textvariable = start_date, 
                     font=('calibre',10,'normal'),
                     background=black, 
                     foreground='#3a36ad',
                     border=0).grid(column=1, row=2)
            
            start_date.set("Enter the start date") 
            #start_date.insert(0, "Enter the start date")
            
            #start_date_entry.bind('<FocusIn>', focus_entry)
            #start_date_entry.bind("<FocusIn>", clear_default)
            #start_date_entry.insert(0, 'Enter the start date')
            #start_date_entry.bind('<FocusIn>', start_date.set(""))


            ttk.Label(main_frame, text = 'and',
                      background=dark_mode, 
                      foreground='#3b73cc', 
                      font =("Courier", 15)).grid(column=1,row=3)

            '''ttk.Label(newWindow, text = 'Enter the end date',
                      background=dark_mode, 
                      foreground='#3b73cc', 
                      font =("Courier", 15)).pack(expand=True)'''
            
            tk.Entry(main_frame,textvariable = end_date, 
                     font=('calibre',10,'normal'),
                     background=black, 
                     foreground='#3a36ad',
                     border=0).grid(column=1,row=4)
            
            end_date.set("Enter the end date") 

            reply_button = tk.Button(main_frame,text = 'Show reply', 
                      command = lambda:getResultsAnswer(self),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=10,
                      height=2,
                      border=0).grid(column=1, row=6)

            tk.Button(main_frame,text = 'Send', 
                      #command = lambda:fetch_search_data(start_date.get(), end_date.get(), self),
                      command = lambda:start_api_processing(self, start_date.get(), end_date.get(), button=reply_button),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=10,
                      height=2,
                      border=0).grid(column=1, row=5)  

        #weather window

        def weatherWindow(self, start_date, end_date):

            weatherWindow = Toplevel(self.win)
        
            weatherWindow.title("Space weather")

            weatherWindow.geometry("2000x1000")

            weatherWindow.configure(bg=dark_mode)

            main_frame = tk.Frame(weatherWindow, bg=dark_mode, pady=40)
            main_frame.pack(fill=tk.BOTH, expand=True)
            main_frame.columnconfigure(0, weight=1)
            main_frame.columnconfigure(1, weight=1)
            main_frame.columnconfigure(2, weight=1)
            main_frame.rowconfigure(0, weight=1)
            main_frame.rowconfigure(1, weight=1)
            main_frame.rowconfigure(2, weight=1)
            main_frame.rowconfigure(3, weight=1)
            main_frame.rowconfigure(4, weight=1)
            
            tk.Entry(main_frame,textvariable = self.weather_start_date, 
                     font=('calibre',10,'normal'),
                     background=black, 
                     foreground='#3a36ad',
                     border=0).grid(column=0, row=0)
            
            self.weather_start_date.set("Enter the start date")
            
            tk.Entry(main_frame,textvariable = self.weather_end_date, 
                     font=('calibre',10,'normal'),
                     background=black, 
                     foreground='#3a36ad',
                     border=0).grid(column=2, row=0)
            
            self.weather_end_date.set("Enter the end date")

            tk.Button(main_frame,text = 'CME', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='cme'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=0,row=1)
            
            tk.Button(main_frame,text = 'GST', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='gst'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=1,row=1)
            
            tk.Button(main_frame,text = 'FLR', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='flr'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=2,row=1)
            
            tk.Button(main_frame,text = 'SEP', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='sep'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=0,row=2)
            
            tk.Button(main_frame,text = 'MPC', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='mpc'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=1,row=2)
            
            tk.Button(main_frame,text = 'RBE', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='rbe'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=2,row=2)
            
            tk.Button(main_frame,text = 'HSS', 
                      command = lambda:start_donki_api(self=self, start_date=self.weather_start_date.get(), end_date=self.weather_end_date.get(), type='hss'),
                      background=black, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=1,row=3)
            
            tk.Button(main_frame,text = 'See reply', 
                      command = lambda:getWeatherResponse(self),
                      background=black_second, 
                      foreground='#3a36ad', 
                      activebackground=gray_color,
                      highlightthickness=2,
                      highlightbackground=black_second,
                      highlightcolor='WHITE',
                      width=13,
                      height=4,
                      border=0).grid(column=1,row=4)

            self.weather_canvas = tk.Canvas(main_frame, height=200, width=250, bg=dark_mode, border=0, highlightthickness=0)
            self.weather_canvas.grid(column=1, row=0)
            #self.second_canvas.create_rectangle(10,150,100,100, fill='#40100f')
            self.rectangle = self.weather_canvas.create_rectangle(10,150,100,100, fill=black)
            self.weather_canvas.create_rectangle(240,150,150,100, fill='#3a36ad')
            
            
def fetch_cme_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'CME' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        print(start_date)
        print(end_date)
        self.weather_type.set('cme')
        for entry in data:
            print(len(data))
            print(entry['activityID'])
            print(entry['startTime'])
            print(entry['note'])
            self.cme_activity_ids.append(entry['activityID'])
            self.cme_start_time.append(entry['startTime'])
            self.cme_note.append(entry['note'])
            #window.destroy()

        with open('cme_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    print("Couldn't receive the data.")
    window.destroy()
            
def fetch_gst_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'GST' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        self.weather_type.set('gst')
        for entry in data:
            print(len(data))
            print(entry['gstID'])
            print(entry['startTime'])
            self.gst_ids.append(entry['gstID'])
            self.gst_start_time.append(entry['startTime'])
            #window.destroy()
            
        with open('gst_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    print("Couldn't receive the data.")
    window.destroy()

def fetch_flr_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'FLR' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        print(start_date)
        print(end_date)
        self.weather_type.set('flr')
        for entry in data:
            print(len(data))
            print(entry['flrID'])
            print(entry['beginTime'])
            print(entry['peakTime'])
            print(entry['classType'])
            print(entry['sourceLocation'])
            print(entry['note'])

            self.flr_ids.append(entry['flrID'])
            self.flr_begin_time.append(entry['beginTime'])
            self.flr_peak_time.append(entry['peakTime'])
            self.flr_class_type.append(entry['classType'])
            self.flr_source_location.append(entry['sourceLocation'])
            self.flr_notes.append(entry['note'])
            #window.destroy()


        with open('flr_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    print("Couldn't receive the data.")
    window.destroy()
    

def fetch_sep_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'SEP' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        print(start_date)
        print(end_date)

        self.weather_type.set('sep')

        for entry in data:
            print(len(data))
            print(entry['sepID'])
            print(entry['eventTime'])
            self.sep_ids.append(entry['sepID'])
            self.sep_event_time.append(entry['eventTime'])
            #window.destroy()
        
        with open('sep_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    print("Couldn't receive the data.")
    window.destroy()

def fetch_mpc_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'MPC' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        
        self.weather_type.set('mpc')
        
        for entry in data:
            print(len(data))
            print(entry['mpcID'])
            print(entry['eventTime'])
            self.mpc_ids.append(entry['mpcID'])
            self.mpc_event_time.append(entry['eventTime'])
            #window.destroy()

        with open('mpc_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    print("Couldn't receive the data.")
    window.destroy()

def fetch_rbe_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'RBE' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        self.weather_type.set('rbe')
        for entry in data:
            print(len(data))
            print(entry['rbeID'])
            print(entry['eventTime'])
            self.rbe_ids.append(entry['rbeID'])
            self.rbe_event_time.append(entry['eventTime'])#
            #window.destroy()

        
        with open('rbe_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

    print("Couldn't receive the data.")
    window.destroy()

def fetch_hss_data(self, start_date, end_date, window):
    response = requests.get(weather_api + 'HSS' + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        self.weather_type.set('hss')
        for entry in data:
            print(len(data))
            print(entry['hssID'])
            print(entry['eventTime'])
            self.hss_ids.append(entry['hssID'])
            self.hss_event_time.append(entry['eventTime'])
            #window.destroy()

        with open('hss_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    print("Couldn't receive the data.")
    window.destroy()

def fetch_weather_data(self, start_date, end_date, type):
    print(type)
    print(start_date)
    print(end_date)
    response = requests.get(weather_api + type + '?startDate=' + start_date + '&endDate=' + end_date + '&api_key=' + api_key)
    if(response.status_code == 200):
        data = response.json()
        print(data)
        for entry in data:
            print(len(data))
            print(entry['gstID'])
            print(entry['startTime'])
        with open('space_weather_data.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

def start_api_processing(self, start_date, end_date, button):
    loadingWindow = Toplevel(self.win)
    loadingWindow.title('Loading the request')
    loadingWindow.configure(bg=dark_mode)

    loadingWindow.geometry("800x800")

    ttk.Label(loadingWindow, text = 'Got it, working on it commander!',
                    background=dark_mode, 
                    foreground='#3b73cc', 
                    font =("Courier", 15)).pack(expand=True)
    ttk.Label(loadingWindow, text = 'This might take a moment.',
                    background=dark_mode, 
                    foreground='#3b73cc', 
                    font =("Courier", 15)).pack(expand=True)
    self.progress = ttk.Progressbar(loadingWindow, mode='indeterminate')
    self.progress.pack(expand=True)
    self.progress.start()

    threading.Thread(target=lambda:fetch_search_data(start_date=start_date, end_date=end_date, self=self, window=loadingWindow, button = button)).start()

def start_donki_api(self, start_date, end_date, type):
    loadingWindow = Toplevel(self.win)
    loadingWindow.title('Loading the request')
    loadingWindow.configure(bg=dark_mode)

    loadingWindow.geometry("800x800")

    ttk.Label(loadingWindow, text = 'Got it, working on it commander!',
                    background=dark_mode, 
                    foreground='#3b73cc', 
                    font =("Courier", 15)).pack(expand=True)
    ttk.Label(loadingWindow, text = 'This might take a moment.',
                    background=dark_mode, 
                    foreground='#3b73cc', 
                    font =("Courier", 15)).pack(expand=True)
    self.progress = ttk.Progressbar(loadingWindow, mode='indeterminate')
    self.progress.pack(expand=True)
    self.progress.start()

    if(type == 'cme'):
        threading.Thread(target=lambda:fetch_cme_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    elif(type == 'gst'):
        threading.Thread(target=lambda:fetch_gst_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    elif(type == 'flr'):
        threading.Thread(target=lambda:fetch_flr_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    elif(type == 'sep'):
        threading.Thread(target=lambda:fetch_sep_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    elif(type == 'mpc'):
        threading.Thread(target=lambda:fetch_mpc_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    elif(type == 'rbe'):
        threading.Thread(target=lambda:fetch_rbe_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    elif(type == 'hss'):
        threading.Thread(target=lambda:fetch_hss_data(self=self, start_date=start_date, end_date=end_date, window=loadingWindow)).start()
    else:
        print("No valid type")
    

    
    

def fetch_search_data(start_date, end_date, self, window, button):
    
    response = requests.get(api_url + '?start_date=' + start_date + '&end_date=' + end_date + '&api_key=' + api_key)

    if(response.status_code == 200):
        data = response.json()
        page = data.get('page')
        links = data.get('links')
        near_earth_objects = data.get('near_earth_objects')
        for neos in near_earth_objects:
            print(len(near_earth_objects))
            print(neos['name'])
            self.names_array.append(neos['name'])
            self.hazardous_status.append(neos['is_potentially_hazardous_asteroid'])
            self.last_observation_dates.append(neos['orbital_data']['last_observation_date'])
        size = page.get('size')
        self.size = size
        print(size)
        with open('nasa_neo_response.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)
    else:
        print("Couldn't receive the data.")
    window.destroy()
         


#Results answer window

def getResultsAnswer(self):
    answerWindow = Toplevel(self.win)

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)

    canvas = tk.Canvas(frame, bg='black', highlightthickness=0)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = ttk.Frame(canvas)

    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    answerWindow.title("Reply on your request")

    self.win.columnconfigure(0, weight=1)
    self.win.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("1900x1900")
    
    if(self.size == 0):
        ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 15)).pack(expand=True)
        ttk.Label(answerWindow, text = 'No near earth objects were detected in that period!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 15)).pack(expand=True)
    else:

        ttk.Label(answerWindow, text = 'Greetings commander!', 
                                background='black', 
                                foreground='#3b73cc', 
                                font =("Courier", 15)).pack(expand=True)
        ttk.Label(answerWindow, text = f'There are {self.size} near earth objects for given period of time.', 
                                background='black', 
                                foreground='#3b73cc', 
                                font =("Courier", 15)).pack(expand=True)
        ttk.Label(answerWindow, text = 'Here is the list of them:', 
                                background='black', 
                                foreground='#3b73cc', 
                                font =("Courier", 15)).pack(expand=True)
        for name in range(self.size):
            ttk.Label(answerWindow, text = f'{self.names_array[name]} ( hazardous: {self.hazardous_status[name]}, last seen: {self.last_observation_dates[name]} )', 
                                background='black', 
                                foreground='#3b73cc', 
                                font =("Courier", 15)).pack(expand=True)
            
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    #canvas.grid(row=0, column=0, sticky="nsew")
    # scrollbar.grid(row=0, column=1, sticky="ns")

    def _on_mousewheel(event):
      canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
      canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
def getWeatherResponse(self):
    
    print(self.weather_type.get())

    if(self.weather_type.get() == 'cme'):
        cmeReply(self)
    elif(self.weather_type.get() == 'gst'):
        gstReply(self)
    elif(self.weather_type.get() == 'flr'):
        flrReply(self)
    elif(self.weather_type.get() == 'sep'):
        sepReply(self)
    elif(self.weather_type.get() == 'mpc'):
        mpcReply(self)
    elif(self.weather_type.get() == 'rbe'):
        rbeReply(self)
    elif(self.weather_type.get() == 'hss'):
        hssReply(self)
    else:
        print("No valid type")
    

#CME REPLY

def cmeReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your cme request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    if(len(self.cme_activity_ids) == 0):
        ttk.Label(answerWindow, text = 'There is no data on coronal mass ejection in that period.', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    else:
        ttk.Label(answerWindow, text = f'Here is the information about coronal mass ejection in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.cme_activity_ids)):
        ttk.Label(answerWindow, text = f'id:{self.cme_activity_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'start time:{self.cme_start_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'note:{self.cme_note[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12),
                            wraplength=500).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")
    
     
#GST REPLY

def gstReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your gst request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    ttk.Label(answerWindow, text = f'Here is the information about geomagnetic storm in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.gst_ids)):
        ttk.Label(answerWindow, text = f'id:{self.gst_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'start time:{self.gst_start_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")
        
#FLR REPLY 

def flrReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your flr request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    ttk.Label(answerWindow, text = f'Here is the information about solar flare in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.flr_ids)):
        ttk.Label(answerWindow, text = f'id:{self.flr_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'begin time:{self.flr_begin_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'peak time:{self.flr_peak_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'class type:{self.flr_class_type[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'source_location:{self.flr_source_location[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'note:{self.flr_notes[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12),
                            wraplength=500).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")
        
#SEP REPLY

def sepReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your sep request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    ttk.Label(answerWindow, text = f'Here is the information about Solar Energetic Particle in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.sep_ids)):
        ttk.Label(answerWindow, text = f'id:{self.sep_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'event time:{self.sep_event_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")
 
#MPC REPLY

def mpcReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your mpc request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    ttk.Label(answerWindow, text = f'Here is the information about Magnetopause Crossing in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.mpc_ids)):
        ttk.Label(answerWindow, text = f'id:{self.mpc_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'event time:{self.mpc_event_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")

#RBE REPLY

def rbeReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your rbe request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    ttk.Label(answerWindow, text = f'Here is the information about Radiation Belt Enhancement in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.rbe_ids)):
        ttk.Label(answerWindow, text = f'id:{self.rbe_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'event time:{self.rbe_event_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")


#HSS REPLY

def hssReply(self):
    answerWindow = Toplevel(self.win)
    
    answerWindow.title("Reply on your hss request")

    frame = tk.Frame(answerWindow, bg='black')
    frame.place(relwidth=1, relheight=1)
    
    # sets the geometry of toplevel
    answerWindow.geometry("3000x2000")
    ttk.Label(answerWindow, text = 'Greetings commander!', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    ttk.Label(answerWindow, text = f'Here is the information about Hight Speed Stream in that period:', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
    for item in range(len(self.hss_ids)):
        ttk.Label(answerWindow, text = f'id:{self.hss_ids[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = f'event time:{self.hss_event_time[item]}', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        ttk.Label(answerWindow, text = '----------------------------------', 
                            background='black', 
                            foreground='#3b73cc', 
                            font =("Courier", 12)).pack(expand=True)
        self.weather_type.set("")


if __name__ == "__main__":
    app = SpaceShipCommanderApp()
    app.win.mainloop()
