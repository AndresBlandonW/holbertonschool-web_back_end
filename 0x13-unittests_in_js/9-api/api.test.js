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

describe('Cart route', () => {
  const goodRoute = 'http://localhost:7865/cart/1'
  const badRoute = 'http://localhost:7865/cart/hello'

  it('should return status 200', done => {
    request(goodRoute, (err, res, body) => {
      (res.statusCode).should.equal(200);
      done();
    });
  });

  it('should return Payment methods for cart 1', done => {
    request(goodRoute, (err, res, body) => {
      (body).should.equal('Payment methods for cart 1');
      done();
    });
  });

  it('should return status 404', done => {
    request(badRoute, (err, res, body) => {
      (res.statusCode).should.equal(404);
      done();
    });
  });

  it('should return Not a number', done => {
    request(badRoute, (err, res, body) => {
      (body).should.equal('Not a number');
      done();
    });
  });
});
