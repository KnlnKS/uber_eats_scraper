const { chromePath } = require("chromedriver");
const { Builder, Capabilities, until, By } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");

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

exports.waitForElementId = async (driver, id, timeout = 5000) =>
  driver.wait(until.elementLocated(By.css(id)), timeout);
