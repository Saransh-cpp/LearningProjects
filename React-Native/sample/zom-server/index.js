// const bodyParser = require("body-parser");
const express = require("express");
// const { json } = require("body-parser");
const csv = require("csvtojson");

const app = express();

// app.use(bodyParser);

// app.get('/', function (request, response) {
//   response.send({name : "Happy"})
// })

function middle (req, res, next) {
  console.log("This is a middleware");
  next();
}

app.use(middle);

// app.use('/photos', express.static('photos'));

app.get("/", function (req, res) {
  // res.send({name : 'Happy'})
  const csvFilePath = "zomato_with_images.csv";
  csv()
    .fromFile(csvFilePath)
    .then((jsonObj) => {
      // res.send(jsonObj.slice(0, 10));
      res.send(jsonObj);
    });
});

app.listen(3000);
