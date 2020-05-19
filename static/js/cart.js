var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var courseName = this.dataset.course
		var action = this.dataset.action
		console.log('CourseName:', courseName, 'Action:', action)
		console.log('USER:', user)

		if (user == 'AnonymousUser'){
			
		}else{
			updateUserOrder(courseName, action)
		}

		})
		}

function updateUserOrder(courseName, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item'

		fetch(url,{
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'courseName':courseName, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		   console.log('data:', data)
		   location.reload()
		});
}