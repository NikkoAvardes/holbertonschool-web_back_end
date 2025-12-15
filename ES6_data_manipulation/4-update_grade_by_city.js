export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const flic = newGrades.find((grade) => grade.studentId === student.id);
      return {
        ...student,
        grade: flic ? flic.grade : 'N/A',
      };
    });
}
