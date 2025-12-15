export default function getStudentIdsSum(students) {
  return students.reduce((acum, student) => acum + student.id, 0);
}