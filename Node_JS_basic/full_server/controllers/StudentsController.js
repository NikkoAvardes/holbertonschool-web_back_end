const readDatabase = require("../utils")

class StudentsController {
	static getAllStudents(request, response) {
		readDatabase(process.argv[2])
			.then((data) => {
				let output = 'This is the list of our students';
				const keys = Object.keys(data).sort((a, b) => 
				a.toLowerCase().localeCompare(b.toLowerCase())
			);
			keys.forEach((keys) => {
				const students = data[key];
				output += `\nNumber of students in ${key}: ${students.length}. List: ${students.join(', ')}`;
			});
			response.status(200).send(output);
		})
		.catch(() => {
			response.status(500).send('Cannot load the database');
		});

	}
	static getAllStudentsByMajor(request, response) {
		response.status(200);
		

	}
}

module.exports = StudentsController;