const { chromePath } = require("chromedriver");
const { Builder, Capabilities, until, By } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const fetch = require("node-fetch");
const fs = require("fs");

exports.waitForElementId = async (driver, id, timeout = 5000) =>
  driver.wait(until.elementLocated(By.css(id)), timeout);

exports.createDriver = async () => {
  options = new chrome.Options();
  options.addArguments("headless");
  options.addArguments("disable-gpu");
  options.addArguments("disable-dev-shm-usage");
  options.excludeSwitches("enable-logging");
  options.addEx;

  const chromeCapabilities = Capabilities.chrome()
    .set("chrome.binary", chromePath)
    .set("acceptInsecureCerts", true);

  return await new Builder()
    .forBrowser("chrome")
    .withCapabilities(chromeCapabilities)
    .setChromeOptions(options)
    .build();
};

exports.getCookieString = async (driver) => {
  let cookieString = "";
  const allCookies = await driver.manage().getCookies();
  const wantedCookieList = new Set([
    "uev2.id.xp",
    "dId",
    "uev2.id.session",
    "uev2.ts.session",
    "jwt-session",
    "marketing_vistor_id",
    "uev2.gg",
    "utm_medium",
    "CONSENTMGR",
    "_userUuid",
    "_rdt_uuid",
    "_scid",
    "_gcl_au",
    "_ga",
    "_gid",
    "_fbp",
    "_gat_tealium_0",
    "_ts_yjad",
    "_sctr",
    "uev2.loc",
    "utag_main",
    "_uetsid",
    "_uetvid",
  ]);

  const filteredCookies = allCookies.filter((cookie) =>
    wantedCookieList.has(cookie.name)
  );

  filteredCookies.forEach((cookie, i) => {
    cookieString += `${i === 0 ? "" : "; "}${cookie.name}=${cookie.value}`;
  });

  return cookieString;
};

exports.print = console.log;

exports.getUberSearchFeed = async (cookie, userQuery, localeCode, offset = 0) =>
  await (
    await fetch(
      `https://www.ubereats.com/api/getFeedV1?localeCode=${localeCode}`,
      {
        headers: {
          accept: "*/*",
          "accept-language": "en-US,en;q=0.9",
          "content-type": "application/json",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "x-csrf-token": "x",
          cookie,
          Referer: "https://www.ubereats.com",
          "Referrer-Policy": "strict-origin-when-cross-origin",
        },
        body: JSON.stringify({
          feedSessionCount: { announcementCount: 0, announcementLabel: "" },
          showSearchNoAddress: false,
          userQuery,
          date: "",
          startTime: 0,
          endTime: 0,
          carouselId: "",
          sortAndFilters: [],
          marketingFeedType: "",
          billboardUuid: "",
          feedProvider: "",
          promotionUuid: "",
          targetingStoreTag: "",
          venueUuid: "",
          favorites: "",
          vertical: "",
          searchSource: "",
          pageInfo: { offset, pageSize: 80 },
        }),
        method: "POST",
      }
    )
  ).json();

exports.makeDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir);
  }
};

exports.writeJson = (fileName, array) => {
  filePath = `../output/feed/${fileName}`;
  this.print(fs.existsSync(filePath));
  if (!fs.existsSync(filePath)) fs.writeFileSync(filePath, "[]");
  this.print(fs.existsSync(filePath));
  fs.readFile(filePath, (err, data) => {
    // READ
    if (err) {
      return console.error(err);
    }

    var data = JSON.parse(data.toString());
    data = data.concat(array);
    fs.writeFile(filePath, JSON.stringify(data), (err, result) =>
      err ? console.error(err) : console.log("write success")
    );
  });
};

exports.pause = (time) => new Promise((resolve) => setTimeout(resolve, time));

exports.formPrint = (resp, categories, i) =>
  this.print(
    `${resp?.status} - ${categories[i]} - hasMore: ${resp?.data?.meta?.hasMore}`
  );
