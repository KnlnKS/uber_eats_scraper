from selenium import webdriver


def scrape_menu(url):
    driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe")
    driver.maximize_window()
    driver.get(url)

    # ===== Header details =====
    detail = ''
    rating = ''
    num = ''

    try:
        detail = driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/div/div[2]/div/div[2]/div[1]").text
    except:
        detail = ''

    try:
        rating = driver.find_element_by_xpath(
            "/html/body/div/div/div/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]").text
    except:
        rating = 'N/A'

    try:
        num = driver.find_element_by_xpath(
            "/html/body/div/div/div/main/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]").text
    except:
        num = '(0)'

    breakpoint()
    # after this still not working false xpath

    restaurant = {
        'title': driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/div/div[2]/div/div[2]/h1").text,
        'detail': detail,
        'rating': rating,
        'num_reviews': num,
        'menu': []
    }

    # ===== Menu =====
    list_item_element = driver.find_element_by_xpath("/html/body/div/div/div/main/div[2]/ul").find_element_by_tag_name("li")
    menu = driver.find_element_by_xpath("/html/body/div/div/div/main/div[2]/ul").find_elements_by_class_name(
        list_item_element.get_attribute("class"))

    name = ''
    description = ''
    status = ''
    price = ''
    img_url = ''

    for x in range(len(menu) - 1):
        category = driver.find_element_by_xpath("/html/body/div/div/div/main/div[2]/ul/li[" + str(x + 1) + "]/h2").text
        restaurant['menu'].append({
            category: []
        })
        section = driver.find_element_by_xpath(
            "/html/body/div/div/div/main/div[2]/ul/li[" + str(x + 1) + "]/ul").find_elements_by_tag_name("li")

        for y in range(len(section)):

            # Get Product Name
            try:
                name = str(driver.find_element_by_xpath(
                    "/html/body/div/div/div/main/div[2]/ul/li[" + str(x + 1) + "]/ul/li[" + str(
                        y + 1) + "]/a/div/div[1]/h4").text)
            except:
                name = ''

            # Get Product Description
            try:
                description = str(driver.find_element_by_xpath(
                    "/html/body/div/div/div/main/div[2]/ul/li[" + str(x + 1) + "]/ul/li[" + str(
                        y + 1) + "]/a/div/div[1]/div[1]").text)
            except:
                description = ''

            # Get Product Price
            try:
                price = str(driver.find_element_by_xpath(
                    "/html/body/div/div/div/main/div[2]/ul/li[" + str(x + 1) + "]/ul/li[" + str(
                        y + 1) + "]/a/div/div[1]/div[2]").text)

                if price == description:
                    description = ''

                if "Sold" in price:
                    status = "Sold out"
                    price = "$" + price.split("$", 1)[1]
                else:
                    status = "In stock"

            except:

                if "$" in description:
                    price = description
                    description = ''
                else:
                    price = ''

            # Get Image URL
            try:
                img_url = str(driver.find_element_by_xpath(
                    "/html/body/div/div/div/main/div[2]/ul/li[" + str(x + 1) + "]/ul/li[" + str(
                        y + 1) + "]/a/div/div[2]/img").get_attribute("src"))
            except:
                img_url = ''

            restaurant['menu'][x][category].append({
                'name': name,
                'description': description,
                'price': price,
                'status': status,
                'img_url': img_url
            })

    return restaurant
