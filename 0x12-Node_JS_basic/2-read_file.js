const fs = require('fs');

const countStudents = (path) => {
  try {
    const data = fs.readFileSync(path, 'utf8');

    let lines = data.split(/\r?\n/);
    lines.shift();
    lines = lines.filter((line) => line !== '');

    console.log(`Number of students: ${lines.length}`);

    const cs = lines
      .filter((line) => line.endsWith('CS'))
      .map((line) => {
        const student = line.split(',');
        return student[0];
      });
    console.log(`Number of students in CS: ${cs.length}. List: ${cs.join(', ')}`);

    const swe = lines
      .filter((line) => line.endsWith('SWE'))
      .map((line) => {
        const student = line.split(',');
        return student[0];
      });
    console.log(`Number of students in SWE: ${swe.length}. List: ${swe.join(', ')}`);
  } catch (err) {
    throw Error('Cannot load the database');
  }
};

module.exports = countStudents;
