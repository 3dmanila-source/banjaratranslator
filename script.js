// ===================================
// DOM Elements
// ===================================
const englishInput = document.getElementById('englishInput');
const banjaraOutput = document.getElementById('banjaraOutput');
const translateBtn = document.getElementById('translateBtn');
const copyBtn = document.getElementById('copyBtn');
const charCount = document.getElementById('charCount');

// ===================================
// Character Counter
// ===================================
englishInput.addEventListener('input', () => {
    const count = englishInput.value.length;
    charCount.textContent = count;
    
    // Update button state
    if (count > 0) {
        translateBtn.disabled = false;
    } else {
        translateBtn.disabled = true;
    }
});

// ===================================
// Translation Function (Placeholder)
// ===================================
async function translateText(text) {
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 800));
    
    // Placeholder translation logic
    // TODO: Replace with actual translation API/logic
    return `[Banjara Translation]\n${text}\n\n(Translation engine coming soon...)`;
}

// ===================================
// Translate Button Handler
// ===================================
translateBtn.addEventListener('click', async () => {
    const inputText = englishInput.value.trim();
    
    if (!inputText) {
        return;
    }
    
    // Update UI to loading state
    translateBtn.disabled = true;
    translateBtn.innerHTML = `
        <span class="btn-text">Translating...</span>
        <svg class="btn-icon spinner" width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2" stroke-dasharray="31.4 31.4" stroke-linecap="round">
                <animateTransform attributeName="transform" type="rotate" from="0 12 12" to="360 12 12" dur="1s" repeatCount="indefinite"/>
            </circle>
        </svg>
    `;
    
    try {
        // Perform translation
        const translatedText = await translateText(inputText);
        
        // Update output
        banjaraOutput.innerHTML = translatedText;
        
        // Enable copy button
        copyBtn.disabled = false;
        
        // Add success animation
        banjaraOutput.style.animation = 'fadeInUp 0.5s ease-out';
        
    } catch (error) {
        console.error('Translation error:', error);
        banjaraOutput.innerHTML = `<span style="color: #ff3b30;">⚠️ Translation failed. Please try again.</span>`;
    } finally {
        // Reset button
        translateBtn.disabled = false;
        translateBtn.innerHTML = `
            <span class="btn-text">Translate</span>
            <svg class="btn-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M14 5L21 12M21 12L14 19M21 12H3" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
        `;
    }
});

// ===================================
// Copy Button Handler
// ===================================
copyBtn.addEventListener('click', async () => {
    const outputText = banjaraOutput.textContent;
    
    try {
        await navigator.clipboard.writeText(outputText);
        
        // Show success feedback
        const originalHTML = copyBtn.innerHTML;
        copyBtn.innerHTML = `
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M20 6L9 17L4 12" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>Copied!</span>
        `;
        copyBtn.style.color = '#34c759';
        
        // Reset after 2 seconds
        setTimeout(() => {
            copyBtn.innerHTML = originalHTML;
            copyBtn.style.color = '';
        }, 2000);
        
    } catch (error) {
        console.error('Copy failed:', error);
        alert('Failed to copy text');
    }
});

// ===================================
// Keyboard Shortcuts
// ===================================
englishInput.addEventListener('keydown', (e) => {
    // Ctrl/Cmd + Enter to translate
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        if (!translateBtn.disabled) {
            translateBtn.click();
        }
    }
});

// ===================================
// Initialize
// ===================================
document.addEventListener('DOMContentLoaded', () => {
    // Disable translate button initially
    translateBtn.disabled = true;
    
    // Focus input
    englishInput.focus();
    
    console.log('🌐 Banjara Translator initialized');
    console.log('💡 Tip: Press Ctrl/Cmd + Enter to translate');
});
