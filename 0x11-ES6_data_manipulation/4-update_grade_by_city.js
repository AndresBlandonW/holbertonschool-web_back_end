const updateStudentGradeByCity = (students, city, grades) => students
  .filter((student) => student.location === city)
  .map((student) => {
    let studentGrade;
    grades.forEach((grade) => {
      if (grade.studentId === student.id) {
        studentGrade = grade.grade;
      }
    });
    return studentGrade ? { ...student, grade: studentGrade } : { ...student, grade: 'N/A' };
  });

export default updateStudentGradeByCity;
