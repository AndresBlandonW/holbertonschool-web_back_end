const sinon = require("sinon");
const sendPaymentRequestToApi = require('./5-payment');
const should = require('chai').should();

describe('#sendPaymentRequestToApi()', function () {
  let spy;
  beforeEach(function () {
    spy = sinon.spy(console, 'log');
  });

  afterEach(function () {
    spy.calledOnce.should.equal(true);
    spy.restore();
  });

  it('should output "The total is: 120"', function () {
    sendPaymentRequestToApi(100, 20);
    spy.calledWith('The total is: 120').should.equal(true);
  });

  it('should output "The total is: 20"', function () {
    sendPaymentRequestToApi(10, 10);
    spy.calledWith('The total is: 20').should.equal(true);
  });

});
