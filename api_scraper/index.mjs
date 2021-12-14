import {
  print,
  createDriver,
  waitForElementId,
  getCookieString,
  getUberSearchFeed,
  writeJson,
  pause,
  formPrint,
  makeDir,
} from "./helper.js";

import { categories, regions } from "./data.js";
let locations = [];

regions.forEach((region) => {
  const localeCode = region.href.split("/")[1];
  locations = locations.concat(
    region.cities.map((city) => ({
      title: `${city.title}, ${region.title}`,
      localeCode,
    }))
  );
});

makeDir("../output/feed/");

for (const i in locations) {
  const { title: location, localeCode } = locations[i];

  const driver = await createDriver();
  await driver.get(`https://ubereats.com/${localeCode}`);

  const locationInput = await waitForElementId(
    driver,
    "#location-typeahead-home-input"
  );
  locationInput.sendKeys(location);
  driver.executeScript("arguments[0].click();", locationInput);

  const locationItem0 = await waitForElementId(
    driver,
    "#location-typeahead-home-item-0"
  );
  driver.executeScript("arguments[0].click();", locationItem0);

  await waitForElementId(driver, "#search-suggestions-typeahead-input", 5000);

  const cookieString = await getCookieString(driver);

  driver.close();

  print("Scraping Uber search feed for " + location);
  print("----------------------------------------");
  for (const i in categories) {
    print(location);
    const fileName = `${localeCode}${location
      .substring(0, location.indexOf(","))
      .replaceAll(" ", "")}.json`;
    let resp = await getUberSearchFeed(cookieString, categories[i], localeCode);

    formPrint(resp, categories, i);
    if (resp?.status !== "success") continue;

    writeJson(
      fileName,
      resp?.data?.feedItems.map(({ store }) => ({
        title: store?.title?.text,
        url: `https://ubereats.com/${localeCode}${store?.actionUrl}`,
        image: store?.image,
      }))
    );

    while (resp?.data?.meta?.hasMore) {
      resp = await getUberSearchFeed(
        cookieString,
        categories[i],
        localeCode,
        resp?.data?.meta?.offset ?? 0
      );

      formPrint(resp, categories, i);
      if (resp?.status !== "success") break;

      writeJson(
        fileName,
        resp?.data?.feedItems.map(({ store }) => ({
          title: store?.title?.text,
          url: `https://ubereats.com/${localeCode}${store?.actionUrl}`,
          image: store?.image,
        }))
      );

      pause(250);
    }
  }
}
