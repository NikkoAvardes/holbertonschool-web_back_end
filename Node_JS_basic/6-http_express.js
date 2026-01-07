const expres = require('express');

const app = expres();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
}).listen(1245);

module.exports = app;
