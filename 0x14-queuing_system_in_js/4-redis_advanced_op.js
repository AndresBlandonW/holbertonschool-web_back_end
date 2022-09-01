import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const hashVal = ['HolbertonSchools', 'Portland', '50', 'Seattle', '80', 'New York', '20',
  'Bogota', '20', 'Cali', '40', 'Paris', '2'];

client.hset(hashVal, redis.print);
client.hgetall('HolbertonSchools', (error, value) => {
  console.log(value);
});
