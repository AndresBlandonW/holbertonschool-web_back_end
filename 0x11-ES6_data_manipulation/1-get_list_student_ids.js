const getListStudentIds = (objects) => {
  if (!Array.isArray(objects)) return [];

  return objects.map((object) => object.id);
};

export default getListStudentIds;
