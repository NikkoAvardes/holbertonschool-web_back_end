const express = require('express');
const fs = require('fs');

const app = express();
const dbFile = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  fs.readFile(dbFile, 'utf-8', (err, data) => {
    if (err) {
      res.status(500).send('Cannot load the database');
      return;
    }

    const lines = data.trim().split('\n');
    const students = lines.slice(1);

    let outputBuffer = `Number of students: ${students.length}\n`;
    const fields = {};

    for (const line of students) {
      if (!line || line.length === 0) return;

      const student = line.split(',');
      const firstName = student[0];
      const field = student[3];

      if (field) {
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }
    }

    for (const [field, names] of Object.entries(fields)) {
      outputBuffer += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
    }

    res.send(outputBuffer);
  });
});

app.listen(1245);
module.exports = app;
