import requests 
from dotenv import load_dotenv
import os
import json
from tkinter import *
from tkinter import ttk
import threading

load_dotenv()
api_key = os.getenv('NASA_API_KEY')
if not api_key:
    raise ValueError("NASA_API_KEY not found in .env file")

api_url = f"https://api.nasa.gov/neo/rest/v1/neo/browse"
api_search_url = f'https://api.nasa.gov/neo/rest/v1/feed'
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
    else:
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
    else:
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
    else:
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
    else:
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
    else:
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
    else:
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
    else:
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