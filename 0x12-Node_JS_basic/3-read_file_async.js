const fsp = require('fs').promises;

const countStudents = async (path) => {
  try {
    const promise = await fsp.readFile(path, 'utf8');

    let lines = promise.split(/\r?\n/);
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

    return { lines, cs, swe };
  } catch (err) {
    throw Error('Cannot load the database');
  }
};

module.exports = countStudents;
