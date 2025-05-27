// display comments
const commentBtn = document.querySelector('#see-comments')
commentBtn.addEventListener('click', (e) => {
	const commentSection = document.querySelector('#comments-container')
	commentSection.style.display = 'block'
})

// display Add Comment form
const commentFormBtn = document.querySelector('#add-comment')
commentFormBtn.addEventListener('click', (e) => {
	const commentFormContainer = document.querySelector('#comment-form-container')
	commentFormContainer.style.display = 'block'
})

// hide Add Comment form
const cancelFormBtn = document.querySelector('#cancel-form-button')
cancelFormBtn.addEventListener('click', (e) => {
	const commentFormContainer = document.querySelector('#comment-form-container')
	commentFormContainer.style.display = null
})

// load more comments
function createLoadComments() {
	let commentCount = 10
	return function loadFn() {
		console.log('clicked!')
		const splitUrl = window.location.pathname.split('/')
		const last = splitUrl.length - 1
		const urlString = '/blog/api/comments/' + splitUrl[last] + '/' + commentCount
		fetch(urlString, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
			}
		}).then(response => {
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`)
			}
			return response.json()
		}).then(datas => {
			function dateCleaner(date) {
				let result = ''
				const slicedDate = date.slice(0, 10)
				const monthMap = new Map([
					['01', 'January'],
					['02', 'February'],
					['03', 'March'],
					['04', 'April'],
					['05', 'May'],
					['06', 'June'],
					['07', 'July'],
					['08', 'August'],
					['09', 'September'],
					['10', 'October'],
					['11', 'November'],
					['12', 'December']
				])
				result += monthMap.get(slicedDate.slice(5,7)) + ' ' + slicedDate.slice(8,10) + ', ' + slicedDate.slice(0,4) + ', '
				const slicedTime = date.slice(11, 17).split(':')
				let pm = false
				let parsedTime = parseInt(slicedTime[0])
				if (parsedTime > 12) {
					pm = true
					slicedTime[0] = parsedTime - 12
				}
				result += '' + slicedTime[0] + ':' + slicedTime[1]
				if (!pm) {
					result += ' a.m.'
				} else {
					result += ' p.m.'
				}
				return result
			}

			for (data of datas) {
				// create elements
				const publishedP = document.createElement('p')
				const authorP = document.createElement('p')
				const strongEl = document.createElement('strong')
				const contentP = document.createElement('p')
				// create text nodes
				const strongText = document.createTextNode(data.author__display_name)
				const contentText = document.createTextNode(data.content)
				const cleanedDate = dateCleaner(data.date_pub)
				const publishedText = document.createTextNode(cleanedDate)
				// append nodes
				authorP.appendChild(strongEl)
				publishedP.appendChild(publishedText)
				contentP.appendChild(contentText)
				strongEl.appendChild(strongText)
				// give appropriate classes
				publishedP.className = 'comment-date'
				authorP.className = 'comment-author'
				contentP.className = 'comment-content'
				// create and append to a section
				const newSection = document.createElement('section')
				newSection.className = 'comment-section'
				newSection.id = `comment-${data.id}`
				newSection.appendChild(authorP)
				newSection.appendChild(contentP)
				newSection.appendChild(publishedP)
				// append section to the comment container
				const commentContainer = document.querySelector('#comment-container')
				const seeMoreSec = document.querySelector('#see-more-sec')
				commentContainer.insertBefore(newSection, seeMoreSec)
			}
		}).catch(error => {
			const btn = document.querySelector('#see-more-btn')
			btn.removeEventListener('click', loadFn)
			btn.innerHTML = 'Out of Comments'
		})
		commentCount += 10
	}
}
const seeMoreBtn = document.querySelector('#see-more-btn')
const loadComments = createLoadComments()
seeMoreBtn.addEventListener('click', loadComments)
