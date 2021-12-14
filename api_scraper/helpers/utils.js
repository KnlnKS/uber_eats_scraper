const fetch = require("node-fetch");

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

exports.pause = (time) => new Promise((resolve) => setTimeout(resolve, time));

exports.formPrint = (resp, categories, i) =>
  this.print(
    `${resp?.status} - ${categories[i]} - hasMore: ${resp?.data?.meta?.hasMore}`
  );
