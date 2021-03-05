const bodyParser = require("body-parser");
const express = require("express");
// const { json } = require("body-parser");

const app = express();
const csv = require("csvtojson");

// app.use(bodyParser);

app.use('/photos', express.static('photos'));

app.get("/", function (req, res) {
  // res.send({name : 'Happy'})
  const csvFilePath = "zomato_with_images.csv";
  csv()
    .fromFile(csvFilePath)
    .then((jsonObj) => {
      res.send(jsonObj.slice(0, 10));
    });
});

app.listen(3000);
