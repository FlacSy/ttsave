const videoElement = document.querySelector('video');

if (videoElement) {
    const sourceElement = videoElement.querySelector('source');

    if (sourceElement) {
        const videoUrl = sourceElement.src;

        const link = document.createElement('a');
        link.href = videoUrl;

        link.download = 'video_file_name';

        document.body.appendChild(link);
        link.click();

        document.body.removeChild(link);
    } else {
        console.error('Не удалось найти элемент <source> внутри элемента <video>.');
    }
} else {
    console.error('Не удалось найти элемент <video> на странице.');
}
