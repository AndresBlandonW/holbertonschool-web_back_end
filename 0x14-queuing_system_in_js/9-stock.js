/* eslint-disable radix */
/* Data */
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

/* Data access */
const getItemById = (id) => {
  for (const item of listProducts) {
    if (item.itemId === id) return item;
  }
  return null;
};

/* Server */
const express = require('express');

const app = express();
const port = 1245;
app.listen(port);

/* Products */
app.get('/list_products', (req, res) => res.json(listProducts));

/* In stock in Redis */
const client = require('redis').createClient();

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

const reserveStockById = (itemId, stock) => client.set(itemId, stock);

const getCurrentReservedStockById = async (itemId) => getAsync(itemId);

/* Product detail */
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  const quantity = await getCurrentReservedStockById(parseInt(itemId));

  if (item) {
    if (quantity) {
      item.currentQuantity = quantity;
    } else {
      item.currentQuantity = item.initialAvailableQuantity;
      reserveStockById(itemId, item.initialAvailableQuantity);
    }
    res.json(item);
  } else {
    res.json({ status: 'Product not found' });
  }
});

/* Reserve a product */
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  const quantity = await getCurrentReservedStockById(parseInt(itemId));

  if (!item) res.json({ status: 'Product not found' });

  if (!quantity) {
    reserveStockById(itemId, item.initialAvailableQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId: `${itemId}` });
  } else if (quantity > 0) {
    reserveStockById(itemId, quantity - 1);
    res.json({ status: 'Reservation confirmed', itemId: `${itemId}` });
  } else if (quantity < 1) {
    res.json({ status: 'Not enough stock available', itemId: `${itemId}` });
  }
});
