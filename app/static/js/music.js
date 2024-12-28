document.addEventListener('DOMContentLoaded', function() {
    var music = document.getElementById('backgroundMusic');
    var musicToggle = document.getElementById('musicToggle');
    var isPlaying = false;

    musicToggle.addEventListener('click', function() {
        if (isPlaying) {
            music.pause();
            musicToggle.textContent = '배경음악 켜기';
        } else {
            music.play();
            musicToggle.textContent = '배경음악 끄기';
        }
        isPlaying = !isPlaying;
    });
});
