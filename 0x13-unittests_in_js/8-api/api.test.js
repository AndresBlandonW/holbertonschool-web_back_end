const should = require('chai').should();
const request = require('request');

describe('Home route', () => {
  const route = 'http://localhost:7865';

  it('should return status 200', function (done) {
    request(route, function (err, res, body) {
      (res.statusCode).should.equal(200);
      done();
    });
  });

  it('should return "Welcome to the payment system"', function (done) {
    request(route, function (err, res, body) {
      (body).should.equal('Welcome to the payment system');
      done();
    });
  });
});
