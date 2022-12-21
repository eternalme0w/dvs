
document.addEventListener('DOMContentLoaded', () => {

	const months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
	const days = ["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"];

	setInterval(() => {

		let date = new Date()
		let h = date.getHours()
		let m = date.getMinutes()
		let nm = date.getMonth()
		let nd = date.getDay()


		m = m.toString()

		if (m.length === 1) {

			m = '0' + m
		}

		let month = months[nm]
		let day = days[nd - 1]

		time = day + " " + h + ":" + m

		document.getElementById('time').innerHTML = time

	})
	
})
