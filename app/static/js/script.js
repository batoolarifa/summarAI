function copySummary() {
    const textElement = document.getElementById('summary-text');
    if (!textElement) return;

    const text = textElement.innerText.trim();
    if (!text) return;

    navigator.clipboard.writeText(text).then(() => {
        const btn = document.getElementById('copy-btn');
        const originalHTML = btn.innerHTML;

        // Apply CSS class only
        btn.classList.add('copied');
        btn.innerHTML = '✔ Copied!';

        setTimeout(() => {
            btn.classList.remove('copied');
            btn.innerHTML = originalHTML;
        }, 2400);
    });
}

// Loading state
document.getElementById('summarize-form').addEventListener('submit', function() {
    const btn = document.getElementById('submit-btn');
    btn.disabled = true;
    btn.classList.add('loading');

    btn.innerHTML = `
        Summarizing with T5 Model
        <span class="spinner"></span>
    `;
});

// Attach event
const copyBtn = document.getElementById('copy-btn');
if (copyBtn) {
    copyBtn.addEventListener('click', copySummary);
}