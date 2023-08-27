import requests
from bs4 import BeautifulSoup

# NOTE: DC's restaurant week has 14 pages for 2023, adjust accordingly
# TODO: Use selenium to click through all pages
restaurant_names = []
for page in range(14):
    if page == 0:
        response = requests.get(f"https://www.ramw.org/restaurantweek")
    else: 
        response = requests.get(f"https://www.ramw.org/restaurantweek?page={page}")

    soup = BeautifulSoup(response.content, "html.parser")

    # The class name for the html element needed to parse will vary
    span_elements = soup.find_all("span", class_="field-content")

    # The element to extract text from will vary
    for span in span_elements:
        h3_element = span.find("h3")
        if h3_element:
            restaurant_names.append(h3_element.text)

# Input your own Yelp API key, can generate one by going to yelp developers webpage and signing in and "creating" an app
headers = {
    "accept": "application/json",
    "Authorization": "Bearer <API_KEY>"
}

output = []
# Yelp Fusion API subject to change, may not work forever
# Modify location and modify or add any other search params
# TODO: Modify the request call so that the first result is not always chosen, or modify the web scraping to get a more accurate/detailed list of names
#       There were some duplicates when initially running the call, and the data had to be manually cleaned
for name in restaurant_names:
    url = f"https://api.yelp.com/v3/businesses/search?location=DC&term={name.replace(' ', '%20')}&sort_by=best_match&limit=20"
    response = requests.get(url, headers=headers)
    data = response.json()

    if "businesses" in data:
        businesses = data["businesses"]
        if len(businesses) > 0:
            business = businesses[0]
            # Grab the useful data, include more if necessary
            output.append({
                "name": business["name"],
                "review_count": business["review_count"],
                "avg_rating": business["rating"],
                "image_url": business["image_url"],
                "url": business["url"]
            })
        else:
            output.append({
                "name": name,
                "message": "ERROR: No information found"
            })
    else:
        output.append({
            "name": name,
            "message": "ERROR: API Request failed"
        })

print(output)
