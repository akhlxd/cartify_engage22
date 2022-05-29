// setting up the required modules

const express = require('express');
const PORT = process.env.PORT || 5000;
const path = require('path');
const exphbs = require('express-handlebars');

const app = express();

//setting up templating engine

app.engine('handlebars', exphbs.engine({ defaultLayout: 'main' }));
app.set('view engine', 'handlebars');

//setting directory path

app.use(express.static(path.join(__dirname, '/public')));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

//setting up the module which will run python scripts

const spawn = require('child_process').spawn;

//variables to collect from website

let budget = 0;
let body_t = 0;
let disp = 0;
let cyl = 0;
let mil = 0;
let fuel = 0;
let fuel_t = 0;
let hei = 0;
let leng = 0;
let wid = 0;
let doors = 0;
let powe = 0;
let tor = 0;
let seat_c = 0;
let wheel = 0;
let price = [];

//homepage

app.get('/', function (req, res) {
  budget = 0;
  body_t = 0;
  price = 0;

  res.render('index');
});

//collect data from homepage

app.post('/', function (req, res) {
  console.log(req.body);

  if (Object.keys(req.body).length !== 2) {
    console.log('Missing Data on top');
    return res.redirect('/');
  }

  budget = req.body['budget'];
  body_t = req.body['body_t'];
  price = [];

  console.log(`budget: ${budget}`);
  console.log(`body_t: ${body_t}`);

  res.redirect('/feat');
});

//redirect to other part of the form

app.get('/feat', function (req, res) {
  res.render('param');
});

//use the data obtained to run python script

app.post('/feat', function (req, res) {
  console.log(req.body);

  if (Object.keys(req.body).length !== 13) {
    console.log('Missing Data in params');
    return res.redirect('/feat');
  }

  disp = req.body['disp'];
  cyl = req.body['cyl'];
  mil = req.body['mil'];
  fuel = req.body['fuel'];
  fuel_t = req.body['fuel_t'];
  hei = req.body['hei'];
  leng = req.body['leng'];
  wid = req.body['wid'];
  doors = req.body['doors'];
  powe = req.body['powe'];
  tor = req.body['tor'];
  seat_c = req.body['seat_c'];
  wheel = req.body['wheel'];

  //runs the python script for getting price

  const ls = spawn('python', [
    'App.py',
    budget,
    body_t,
    disp,
    cyl,
    mil,
    fuel,
    fuel_t,
    hei,
    leng,
    wid,
    doors,
    powe,
    tor,
    seat_c,
    wheel,
  ]);

  ls.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
    let final_p = parseInt(Math.round(data) / 1000) * 1000;
    price.push(final_p);
    console.log(price.join(''));
  });

  ls.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
  });

  ls.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    console.log('Price: ', price[0]);
    res.redirect('/result'); //waits till price is calculated before going to the result page
    // price = [];
  });
});

//result page calculates the numerical values and generates the graphs

app.get('/result', (req, res) => {
  console.log('Price = ', price[0]);
  let per = [];
  const python = spawn('python', [
    'graphs.py',
    budget,
    body_t,
    disp,
    mil,
    fuel,
    powe,
    tor,
    price,
  ]);

  python.stdout.on('data', function (data) {
    console.log('Pipe data from python script ...');
    per.push(data);
    console.log(per.join(''));
  });

  python.stderr.on('data', (data) => {
    console.log(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    console.log(per);
    let disp1 = parseFloat(per[0]); //get the percentages to be displayed in the page
    console.log('disp1: ', disp1);
    let mil1 = per[1];
    console.log('mil1: ', mil1);
    let fuel1 = parseFloat(per[2]);
    console.log('fuel1: ', fuel1);
    let powe1 = parseFloat(per[3]);
    console.log('powe1: ', powe1);
    let tor1 = parseFloat(per[4]);
    console.log('tor1: ', tor1);
    let price1 = parseFloat(per[5]);
    console.log('price1: ', price1);

    res.render('result', { price, disp1, mil1, fuel1, powe1, tor1, price1 });
    per = [];
    // res.send(per.join(''));
  });

  // res.send(dataToSend);
});

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));
