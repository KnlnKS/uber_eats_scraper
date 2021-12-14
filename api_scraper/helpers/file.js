const fs = require("fs");

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
    if (err) return console.error(err);

    var data = JSON.parse(data.toString());
    data = data.concat(array);
    fs.writeFile(filePath, JSON.stringify(data), (err, result) =>
      err ? console.error(err) : console.log("write success")
    );
  });
};
