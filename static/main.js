document.getElementById('voiceBtn').addEventListener('click', function() {
    fetch('/api/voice', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        changeFaceIcon();
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('symptomsBtn').addEventListener('click', function() {
    fetch('/api/symptoms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        changeFaceIcon();
    })
    .catch(error => console.error('Error:', error));
});

function changeFaceIcon() {
    var faceImg = document.getElementById('faceImg');
    if (faceImg.src.includes('normal-face.png')) {
        faceImg.src = faceImg.src.replace('normal-face.png', 'happy-face.png');
    } else {
        faceImg.src = faceImg.src.replace('happy-face.png', 'normal-face.png');
    }
}
