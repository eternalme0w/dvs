
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

	document.getElementById('open-folder-capacity').addEventListener('click', () => {

		document.getElementById('capacity-page').classList.add('page-show')
	})

	document.getElementById('open-folder-routes').addEventListener('click', () => {

		document.getElementById('routes-page').classList.add('page-show')
	})

	document.getElementById('open-folder-schedule').addEventListener('click', () => {

		document.getElementById('schedule-page').classList.add('page-show')
	})

	document.getElementById('close-capacity-page').addEventListener('click', () => {

		document.getElementById('capacity-page').classList.remove('page-show')
	})

	document.getElementById('close-routes-page').addEventListener('click', () => {

		document.getElementById('routes-page').classList.remove('page-show')
	})

	document.getElementById('close-schedule-page').addEventListener('click', () => {

		document.getElementById('schedule-page').classList.remove('page-show')
	})

	document.getElementById('open-login-form').addEventListener('click', () => {

		document.getElementById('shield').classList.add('page-show')
		document.getElementById('login-section').classList.add('page-show')
	})

	document.getElementById('close-login-section').addEventListener('click', () => {

		document.getElementById('shield').classList.remove('page-show')
		document.getElementById('login-section').classList.remove('page-show')
	})
	
})
