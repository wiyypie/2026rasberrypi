const img = document.querySelector('#myImage');
const btn = document.querySelector('#changeBtn');
const bt = document.querySelector('#changeBt');

btn.addEventListener('click', function() {
	fetch('/on',{
		method:'GET'})
	.then(response=>{
		if (!response.ok){
			throw new Error("HTTP error "+response.status);
		}
		return response.text();
	})
	.then(result =>{
  img.src = '/static/b.png';
})
	.catch(error => {
		alert(error);
	});
});

bt.addEventListener('click',function(){
	   fetch('/off',{
                method:'GET'})
        .then(response=>{
                if (!response.ok){
                        throw new Error("HTTP error "+response.status);
                }
                return response.text();
        })
        .then(result =>{
  img.src = '/static/a.png';
})
        .catch(error => {
                alert(error);
        });

});
