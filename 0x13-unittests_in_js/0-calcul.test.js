const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('#calculateNumber()', function () {
  it('should return 5 when calculateNumber adds 1 and 3.7', function () {
    assert.strictEqual(calculateNumber(1, 3.7), 5);
  });
  it('should return 5 when calculateNumber adds 1 and 3.7', function () {
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
  });
  it('should return 6 when calculateNumber adds 1 and 3.7', function () {
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it('should return 3 when calculateNumber adds -1 and 3.7', function () {
    assert.strictEqual(calculateNumber(-1, 3.7), 3);
  });
  it('should return 0 when calculateNumber adds 0.1 and 0.3', function () {
    assert.strictEqual(calculateNumber(0.1, 0.3), 0);
  });
  it('should return -5 when calculateNumber adds -1 and -3.7', function () {
    assert.strictEqual(calculateNumber(-1, -3.7), -5);
  });
  it('should return -1 when calculateNumber adds -0.1 and -0.7', function () {
    assert.strictEqual(calculateNumber(-0.1, -0.7), -1);
  });
});
