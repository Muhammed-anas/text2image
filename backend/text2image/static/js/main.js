function setPrompt(text) {
    document.getElementById('promptInput').value = text;
}

document.getElementById('imageForm').addEventListener('submit', function() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('generateBtn').disabled = true;
    document.getElementById('generateBtn').textContent = 'Generating...';
});