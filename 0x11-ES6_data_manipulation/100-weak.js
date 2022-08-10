const weakMap = new WeakMap();
const queryAPI = (endpoint) => {
  if (!weakMap.get(endpoint)) {
    weakMap.set(endpoint, 1);
  } else {
    weakMap.set(endpoint, weakMap.get(endpoint) + 1);
  }

  if (weakMap.get(endpoint) >= 5) throw new Error('Endpoint load is high');
};

export { weakMap, queryAPI };
