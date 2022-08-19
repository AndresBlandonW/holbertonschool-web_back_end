const chai = require('chai');
const sinon = require("sinon");
const should = chai.should();
const getPaymentTokenFromAPI = require('./6-payment_token');

describe.only('#getPaymentTokenFromAPI()', function () {
  it('should return "Successful response from the API" if true passed in', function (done) {
    getPaymentTokenFromAPI(true)
      .then(function (value) {
        value.data.should.equal("Successful response from the API");
        done();
      });
  });
});
