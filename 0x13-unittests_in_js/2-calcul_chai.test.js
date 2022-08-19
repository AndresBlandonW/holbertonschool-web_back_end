const expect = require("chai").expect;
const calculateNumber = require('./2-calcul_chai');

describe("#calculateNumber() with type SUM", function () {
  it('should return 5 when calculateNumber adds 1 and 3.7', function () {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('should return 5 when calculateNumber adds 1 and 3.7', function () {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });
  it('should return 6 when calculateNumber adds 1 and 3.7', function () {
    expect(calculateNumber('SUM', 1.5, 3.7)).to.equal(6);
  });
  it('should return 3 when calculateNumber adds -1 and 3.7', function () {
    expect(calculateNumber('SUM', -1, 3.7)).to.equal(3);
  });
  it('should return 0 when calculateNumber adds 0.1 and 0.3', function () {
    expect(calculateNumber('SUM', 0.1, 0.3)).to.equal(0);
  });
  it('should return -5 when calculateNumber adds -1 and -3.7', function () {
    expect(calculateNumber('SUM', -1, -3.7)).to.equal(-5);
  });
  it('should return -1 when calculateNumber adds -0.1 and -0.7', function () {
    expect(calculateNumber('SUM', -0.1, -0.7)).to.equal(-1);
  });
});

describe("#calculateNumber() with type SUBTRACT", function () {
  it('should return -3 when calculateNumber subtracts 1 and 3.7', function () {
    expect(calculateNumber('SUBTRACT', 1, 3.7)).to.equal(-3);
  });
  it('should return 3 when calculateNumber subtracts 3.7 and 1.2', function () {
    expect(calculateNumber('SUBTRACT', 3.7, 1.2)).to.equal(3);
  });
  it('should return 2 when calculateNumber subtracts 3.7 and 1.5', function () {
    expect(calculateNumber('SUBTRACT', 3.7, 1.5)).to.equal(2);
  });
  it('should return 5 when calculateNumber subtracts 3.7 and -1', function () {
    expect(calculateNumber('SUBTRACT', 3.7, -1)).to.equal(5);
  });
  it('should return 0 when calculateNumber subtracts 0.1 and 0.3', function () {
    expect(calculateNumber('SUBTRACT', 0.1, 0.3)).to.equal(0);
  });
  it('should return 3 when calculateNumber subtracts -1 and -3.7', function () {
    expect(calculateNumber('SUBTRACT', -1, -3.7)).to.equal(3);
  });
  it('should return 1 when calculateNumber subtracts -0.7 and -0.1', function () {
    expect(calculateNumber('SUBTRACT', -0.7, -0.1)).to.equal(-1);
  });
});

describe("#calculateNumber() with type DIVIDE", function () {
  it('should return 0.25 when calculateNumber divides 1 and 3.7', function () {
    expect(calculateNumber('DIVIDE', 1, 3.7)).to.equal(0.25);
  });
  it('should return 4 when calculateNumber divides 3.7 and 1.2', function () {
    expect(calculateNumber('DIVIDE', 3.7, 1.2)).to.equal(4);
  });
  it('should return 2 when calculateNumber divides 3.7 and 1.5', function () {
    expect(calculateNumber('DIVIDE', 3.7, 1.5)).to.equal(2);
  });
  it('should return -4 when calculateNumber divides 3.7 and -1', function () {
    expect(calculateNumber('DIVIDE', 3.7, -1)).to.equal(-4);
  });
  it('should return "Error" when calculateNumber divides 0.1 and 0.3', function () {
    expect(calculateNumber('DIVIDE', 0.1, 0.3)).to.equal('Error');
  });
  it('should return -1 when calculateNumber divides -1 and -3.7', function () {
    expect(calculateNumber('DIVIDE', -1, 0.7)).to.equal(-1);
  });
  it('should return "Error" when calculateNumber divides -0.7 and -0.1', function () {
    expect(calculateNumber('DIVIDE', -0.7, -0.1)).to.equal('Error');
  });
});