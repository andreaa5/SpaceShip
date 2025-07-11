# SpaceShip

This is a fun interface for astronomy 
enthusiasts. It allows to receive information on space weather and near earth objects within specified
range of days for example.

---

## Features

- Enter start day and end day for near earth objects
  * The answer contains the name of the object, if it is hazardous and when it was last seen
  * Or if no objects found it communicates that
- Enter start day and end day for the space weather. Here there are multiple options:
  1. Coronal Mass Ejection (CME)
  2. Geometric Storm (GST)
  3. Interplanatery Shock (IPS)
  4. Solar Flare (FLR)
  5. Solar Energetic Particle (SEP)
  6. Magnetopause Crossing (MPC)
  7. Radiation Belt Enhancement (RBE)
  8. Hight Speed Stream (HSS)

  * The answer contains the start time of the specified event and notes as additional information for it

---

## Technologies Used

- NASA API
- Python

---

## Installation

### Prerequisites
- python 3.12.9
- tkinter 8.6
- certifi 2025.7.9
- charset-normalizer 3.4.2
- idna 3.10
- python-dotenv 1.1.1
- requests 2.32.4
- urllib3 2.5.0

### Clone the Repository

```bash
https://github.com/andreaa5/SpaceShip
cd SpaceShip
``` 
###  Setup

1. **Create and activate a virtual environment**

* On Linux/mac0S:
  ```bash
  python3 -m venv venv
  source venv/bin/activate


* On Windows:
  ```bash
  python -m venv venv
  .\venv\Scripts\Activate.ps1
```

2. **Install required packages - you can simply use the requirements.txt as well**

```bash
pip install -r requirements.txt
```

In case you need to install tkinter:
```bash
sudo apt-get install python3-tk
```

3. **Running the project**

```bash
python3 starship_interface.py
```

### API

Don't forget to get your api key and include it in .env as NASA_API_KEY = '*your_api_key' (replace your_api_key with your actual api key string)