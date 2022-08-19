const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('#calculateNumber()', function () {
  it('should return 5 when calculateNumber adds 1 and 3.7', function () {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('should return 5 when calculateNumber adds 1 and 3.7', function () {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('should return 6 when calculateNumber adds 1 and 3.7', function () {
    assert.equal(calculateNumber('SUM', 1.5, 3.7), 6);
  });
  it('should return 3 when calculateNumber adds -1 and 3.7', function () {
    assert.equal(calculateNumber('SUM', -1, 3.7), 3);
  });
  it('should return 0 when calculateNumber adds 0.1 and 0.3', function () {
    assert.equal(calculateNumber('SUM', 0.1, 0.3), 0);
  });
  it('should return -5 when calculateNumber adds -1 and -3.7', function () {
    assert.equal(calculateNumber('SUM', -1, -3.7), -5);
  });
  it('should return -1 when calculateNumber adds -0.1 and -0.7', function () {
    assert.equal(calculateNumber('SUM', -0.1, -0.7), -1);
  });
  it('should return -3 when calculateNumber subtracts 1 and 3.7', function () {
    assert.equal(calculateNumber('SUBTRACT', 1, 3.7), -3);
  });
  it('should return 3 when calculateNumber subtracts 3.7 and 1.2', function () {
    assert.equal(calculateNumber('SUBTRACT', 3.7, 1.2), 3);
  });
  it('should return 2 when calculateNumber subtracts 3.7 and 1.5', function () {
    assert.equal(calculateNumber('SUBTRACT', 3.7, 1.5), 2);
  });
  it('should return 5 when calculateNumber subtracts 3.7 and -1', function () {
    assert.equal(calculateNumber('SUBTRACT', 3.7, -1), 5);
  });
  it('should return 0 when calculateNumber subtracts 0.1 and 0.3', function () {
    assert.equal(calculateNumber('SUBTRACT', 0.1, 0.3), 0);
  });
  it('should return 3 when calculateNumber subtracts -1 and -3.7', function () {
    assert.equal(calculateNumber('SUBTRACT', -1, -3.7), 3);
  });
  it('should return 1 when calculateNumber subtracts -0.7 and -0.1', function () {
    assert.equal(calculateNumber('SUBTRACT', -0.7, -0.1), -1);
  });
  it('should return 0.25 when calculateNumber divides 1 and 3.7', function () {
    assert.equal(calculateNumber('DIVIDE', 1, 3.7), 0.25);
  });
  it('should return 4 when calculateNumber divides 3.7 and 1.2', function () {
    assert.equal(calculateNumber('DIVIDE', 3.7, 1.2), 4);
  });
  it('should return 2 when calculateNumber divides 3.7 and 1.5', function () {
    assert.equal(calculateNumber('DIVIDE', 3.7, 1.5), 2);
  });
  it('should return -4 when calculateNumber divides 3.7 and -1', function () {
    assert.equal(calculateNumber('DIVIDE', 3.7, -1), -4);
  });
  it('should return "Error" when calculateNumber divides 0.1 and 0.3', function () {
    assert.equal(calculateNumber('DIVIDE', 0.1, 0.3), 'Error');
  });
  it('should return -1 when calculateNumber divides -1 and -3.7', function () {
    assert.equal(calculateNumber('DIVIDE', -1, 0.7), -1);
  });
  it('should return "Error" when calculateNumber divides -0.7 and -0.1', function () {
    assert.equal(calculateNumber('DIVIDE', -0.7, -0.1), 'Error');
  });
});
