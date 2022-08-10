import getListStudentIds from './1-get_list_student_ids';

const getStudentIdsSum = (students) => {
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  const ids = getListStudentIds(students);

  return ids.reduce(reducer);
};

export default getStudentIdsSum;
