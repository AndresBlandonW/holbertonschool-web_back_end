/* eslint-disable jest/valid-expect */
/* eslint-disable no-undef */
/* eslint-disable jest/no-hooks */
/* eslint-disable jest/prefer-expect-assertions */
import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();
const {
  testMode: {
    clear, enter, exit, jobs,
  },
} = queue;

describe('#createPushNotificationsJobs()', () => {
  before(() => enter());
  afterEach(() => clear());
  after(() => exit());

  it('should throw "Jobs is not an array" when jobs is not an Array', () => {
    const str = 'Not an array';
    const badFn = () => createPushNotificationsJobs(str, queue);
    expect(badFn).to.throw(Error, 'Jobs is not an array');
  });

  it('should create two new jobs to the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account',
      },
    ];
    createPushNotificationsJobs(list, queue);
    expect(jobs.length).to.equal(2);
    expect(jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(list[0]);
    expect(jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.eql(list[1]);
  });
});
