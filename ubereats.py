import json
import menu_scraper
import restaurant_scraper


base_url = "https://www.ubereats.com/category/"
city_list = ["new-york-city", "toronto", "kingston", "hamilton", "brooklyn"]
restaurant_data = {
    'cities': []
}
temp_array = []

""" ===== Restaurant Menu Scraper ===== """
for city in city_list:

    restaurant_scraper.scrape_restaurants(base_url, city)

    file = open(city + '_restaurant_urls.txt', 'r')
    lines = file.readlines()

    for line in lines:
        temp_array.append(menu_scraper.scrape_menu(line))

    restaurant_data['cities'].append({
        city: temp_array
    })

with open('data.json', 'w+', encoding='utf-8') as outfile:
    json.dump(restaurant_data, outfile, indent=4, ensure_ascii=False)
