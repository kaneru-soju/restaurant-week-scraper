# Restaurant Week Scraper

Scrapes the restaurant names from the Restaurant Week - DC webpage | [ramw](https://www.ramw.org/restaurantweek)

## Install:
### venv:
```sh
git clone https://github.com/kaneru-soju/restaurant-week-scraper.git
cd restaurant-week-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### normal:
```sh
git clone https://github.com/kaneru-soju/restaurant-week-scraper.git
cd restaurant-week-scraper
pip install -r requirements.txt
```

## Usage:
Before using, make sure to modify the `main.py` script with the API_KEY and website relevant to yourself.
```sh
sudo python3 ./main.py > restaurant_data.txt
```
After starting the script in the terminal, the data will be scraped and output to the console. Recommended usage is to append the output to a file.

## Documentation
To exit venv, use this command while in venv
```sh
deactivate
```

## OS Supported:
```
Linux
MacOS
```

Important packages used:
- [bs4](https://pypi.org/project/beautifulsoup4/)
- [requests](https://pypi.org/project/requests/)