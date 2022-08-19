function calculateNumber(type, a, b) {
  const operations = ['SUM', 'SUBTRACT', 'DIVIDE'];
  if (operations.indexOf(type) === -1) throw Error('Cannot perform that operation');
  if (type === 'SUM') return Math.round(a) + Math.round(b);
  if (type === 'SUBTRACT') return Math.round(a) - Math.round(b);
  if (type === 'DIVIDE') {
    if (Math.round(b) === 0) {
      return 'Error';
    } else {
      return Math.round(a) / Math.round(b);
    }
  }
}

module.exports = calculateNumber;
