var setAngle = document.querySelector('#setAngle');

setAngle.addEventListener('click', function() {
    const angle = document.querySelector('#angle').value;

    if (angle !== '' && angle >= 0 && angle <= 180 && Number.isInteger(Number(angle))) {
        fetch('/api/angle', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ angle: angle })
        })
        .then(function(response) {
            if (!response.ok) {
                throw new Error('HTTP ' + response.status);
            }
            return response.json();
        })
        .then(function(result) {
            alert(result.message);
        })
        .catch(function(error) {
            console.log(error);
            alert('Failed to set angle!');
        });
    }
    else {
        alert("Please enter an angle between 0 and 180!!!");
    }
});
