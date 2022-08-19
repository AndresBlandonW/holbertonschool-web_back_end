
const sinon = require("sinon");
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');
const should = require('chai').should();

describe('#sendPaymentRequestToApi()', function () {
  it('should validate the usage of the Utils function', function () {
    const spy = sinon.spy(console, 'log');
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.returns(10);
    sendPaymentRequestToApi(100, 20);

    spy.calledWith('The total is: 10').should.equal(true);
    stub.calledWith('SUM', 100, 20).should.equal(true);
    stub.alwaysReturned(10).should.equal(true);
    spy.restore();
    stub.restore();
  })
});
