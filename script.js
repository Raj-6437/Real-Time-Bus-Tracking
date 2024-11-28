document.getElementById('busSearchForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const busStop = document.getElementById('busStop').value;
    const busResults = document.getElementById('busResults');

    // Sample logic to display bus information based on stop
    let message = '';

    if (busStop.toLowerCase() === 'station a') {
        message = 'Next bus at Station A: Bus 1 at 10:30 AM';
    } else if (busStop.toLowerCase() === 'station b') {
        message = 'Next bus at Station B: Bus 2 at 11:00 AM';
    } else {
        message = 'No bus found at this stop.';
    }

    busResults.innerHTML = `<p>${message}</p>`;
});
