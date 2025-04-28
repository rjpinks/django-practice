// add listeners to the collapsed buttons
const btn1 = document.querySelector('#interest-button1')
const btn2 = document.querySelector('#interest-button2')
const btn3 = document.querySelector('#interest-button3')
const btn4 = document.querySelector('#interest-button4')
btn1.addEventListener('click', (e) => {
	console.log('clicked!')
	const pEl = document.querySelector('#interest-details1')
	if (pEl.className == 'hidden-details') {
		pEl.className = 'appeared-details'
		e.currentTarget.innerHTML = '↑'
	} else if (pEl.className == 'appeared-details') {
		pEl.className = 'hidden-details'
		e.currentTarget.innerHTML = '↓'
	}
})
btn2.addEventListener('click', (e) => {
	const pEl = document.querySelector('#interest-details2')
	if (pEl.className == 'hidden-details') {
		pEl.className = 'appeared-details'
		e.currentTarget.innerHTML = '↑'
	} else if (pEl.className == 'appeared-details') {
		pEl.className = 'hidden-details'
		e.currentTarget.innerHTML = '↓'
	}
})
btn3.addEventListener('click', (e) => {
	const pEl = document.querySelector('#interest-details3')
	if (pEl.className == 'hidden-details') {
		pEl.className = 'appeared-details'
		e.currentTarget.innerHTML = '↑'
	} else if (pEl.className == 'appeared-details') {
		pEl.className = 'hidden-details'
		e.currentTarget.innerHTML = '↓'
	}
})
btn4.addEventListener('click', (e) => {
	const pEl = document.querySelector('#interest-details4')
	if (pEl.className == 'hidden-details') {
		pEl.className = 'appeared-details'
		e.currentTarget.innerHTML = '↑'
	} else if (pEl.className == 'appeared-details') {
		pEl.className = 'hidden-details'
		e.currentTarget.innerHTML = '↓'
	}
})
