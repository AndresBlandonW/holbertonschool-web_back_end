const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.status(200);
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.status(200);
  res.set('Content-Type', 'text/plain');
  await countStudents(process.argv[2])
    .then((value) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${value.lines.length}\n`);
      res.write(`Number of students in CS: ${value.cs.length}. List: ${value.cs.join(', ')}\n`);
      res.write(`Number of students in SWE: ${value.swe.length}. List: ${value.swe.join(', ')}`);
      res.end();
    })
    .catch((err) => {
      res.write('This is the list of our students\n');
      res.end(err.message);
    });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

module.exports = app;
