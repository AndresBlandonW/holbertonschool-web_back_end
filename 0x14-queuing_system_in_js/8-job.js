const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  jobs.forEach((item) => {
    const job = queue.create('push_notification_code_3', item);

    job
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('failed', (errorMessage) => console.log(`Notification job ${job.id} failed: ${errorMessage}`))
      .on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`))
      .save((err) => {
        if (!err) console.log(`Notification job created: ${job.id}`);
      });
  });
};

export default createPushNotificationsJobs;
