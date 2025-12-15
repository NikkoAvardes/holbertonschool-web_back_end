export default function getListStudentIds(getListStudents) {
	if (getListStudents !== Array) {
		return []
	}
	return [map(getListStudentIds, getListStudents)]
}