const fs = require("fs");

exports.makeDir = (dir) => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir);
  }
};

exports.writeJson = (fileName, array) => {
  filePath = `../output/feed/${fileName}`;

  if (!fs.existsSync(filePath)) fs.writeFileSync(filePath, "[]");

  fs.readFile(filePath, (err, data) => {
    if (err) return console.error(err);

    var newData = JSON.parse(data.toString());
    newData = newData.concat(array);
    fs.writeFileSync(filePath, JSON.stringify(newData));
    console.log("write success");
  });
};

exports.removeDupeFromJson = (fileName) => {
  filePath = `../output/feed/${fileName}`;

  fs.readFile(filePath, (err, data) => {
    if (err) return console.error(err);

    var data = JSON.parse(data.toString());
    var unique = [];
    var setList = new Set();
    data.forEach((item) => {
      if (!setList.has(item.url)) {
        setList.add(item.url);
        unique.push(item);
      }
    });

    console.log(`Reduced ${data.length} to ${unique.length}`);

    fs.writeFile(filePath, JSON.stringify(unique), (err, result) =>
      err ? console.error(err) : console.log("remove dupe success")
    );
  });
};
