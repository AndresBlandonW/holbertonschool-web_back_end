const createInt8TypedArray = (length, position, value) => {
  const buffer = new ArrayBuffer(length);
  const int8View = new DataView(buffer);

  try {
    int8View.setInt8(position, value);
  } catch (e) {
    throw Error('Position outside range');
  }

  return int8View;
};

export default createInt8TypedArray;
