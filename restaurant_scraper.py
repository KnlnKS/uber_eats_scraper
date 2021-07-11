from selenium import webdriver
import os

from joblib import Parallel, delayed
from selenium.common.exceptions import NoSuchElementException


def get_urls(cat_url):
    try:
        driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
        driver.get(cat_url)
        temp_urls = driver.find_element_by_xpath("/html/body/div/div/main/div[5]").find_elements_by_tag_name("a")
        for url in temp_urls:
            out_file = open("temp_urls.txt", "a")
            out_file.write(str(url.get_attribute("href")) + "\n")
    except NoSuchElementException:
        print("Skipped " + cat_url)


def scrape_restaurants(base_url, location):
    driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
    driver.get(base_url + location)

    categories = driver.find_element_by_xpath("/html/body/div/div/main/div[2]/div[3]"). \
        text.replace(" ", "-").lower().splitlines()

    Parallel(n_jobs=5)(delayed(get_urls)(base_url + location + "/" + cat) for cat in categories)

    lines_seen = set()  # holds lines already seen
    out_file = open(location + "_restaurant_urls.txt", "w+")
    for line in open("temp_urls.txt", "r"):
        if line not in lines_seen:  # not a duplicate
            out_file.write(line)
            lines_seen.add(line)
    out_file.close()

    os.remove("temp_urls.txt")
