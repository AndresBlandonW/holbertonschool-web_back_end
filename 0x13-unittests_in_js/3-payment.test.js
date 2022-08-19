
const sinon = require("sinon");
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');
const should = require('chai').should();

describe('#sendPaymentRequestToApi()', function () {
  it('should validate the usage of the Utils function', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);

    spy.calledWith('SUM', 100, 20).should.equal(true);
    spy.restore();
  })
});
