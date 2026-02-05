// ===================================
// ENHANCED BANJARA TRANSLATOR
// With Grammar Rules + Phrase Matching
// ===================================

// DOM Elements (same as original)
const englishInput = document.getElementById('englishInput');
const banjaraOutput = document.getElementById('banjaraOutput');
const translateBtn = document.getElementById('translateBtn');
const copyBtn = document.getElementById('copyBtn');
const charCount = document.getElementById('charCount');

// Character Counter
englishInput.addEventListener('input', () => {
    const count = englishInput.value.length;
    charCount.textContent = count;
    translateBtn.disabled = count === 0;
});

// ===================================
// DICTIONARY + PHRASES
// ===================================
let dictionary = {};
let phraseDict = {};

function buildPhraseDictionary() {
    return {
        // Greetings
        'good morning': 'sorer parbati',
        'good evening': 'sorer sanj',
        'good night': 'sorer rat',
        'hello': 'namaste',

        // Common phrases
        'how are you': 'tum kaise ho',
        'thank you': 'dhanyavad',
        'i am fine': 'me theek hun',
        'very good': 'bahut achchha',

        // Pronouns with auxiliaries  
        'i am': 'me hun',
        'you are': 'tum ho',
        'he is': 'vo hai',
        'she is': 'vo hai',
        'we are': 'hum hain',
        'they are': 've hain',

        // Common questions
        'what is': 'kya hai',
        'where is': 'kahan hai',
        'who is': 'kaun hai',
        'how is': 'kaise hai'
    };
}

// Grammar rules for better translation
const grammar = {
    ignore: ['the', 'a', 'an'],

    pronouns: {
        'i': 'me', 'you': 'tum', 'he': 'vo', 'she': 'vo',
        'we': 'hum', 'they': 've', 'it': 'ye',
        'my': 'mera', 'your': 'tumhara', 'his': 'uska',
        'her': 'uski', 'our': 'hamara', 'their': 'unka'
    },

    auxiliaries: {
        'am': 'hun', 'is': 'hai', 'are': 'ho',
        'was': 'tha', 'were': 'the', 'been': 'raha',
        'will': 'ga', 'would': 'ga', 'can': 'sakta',
        'should': 'chahiye', 'must': 'zaroor'
    },

    prepositions: {
        'in': 'me', 'on': 'par', 'at': 'pe', 'to': 'ko',
        'from': 'se', 'with': 'ke saath', 'for': 'ke liye',
        'of': 'ka', 'by': 'se', 'under': 'niche'
    }
};

// Load dictionary
async function loadDictionary() {
    try {
        const response = await fetch('dictionary.json');
        dictionary = await response.json();
        phraseDict = buildPhraseDictionary();
        console.log(`📚 Loaded ${Object.keys(dictionary).length} words`);
        console.log(`💬 Built ${Object.keys(phraseDict).length} phrases`);
    } catch (error) {
        console.error('Error loading dictionary:', error);
        dictionary = {};
    }
}

loadDictionary();

// ===================================
// ENHANCED TRANSLATION LOGIC
// ===================================
async function translateText(text) {
    await new Promise(resolve => setTimeout(resolve, 300));

    if (!text || !text.trim()) return '';

    const input = text.toLowerCase().trim();

    // STEP 1: Check exact phrase match
    if (phraseDict[input]) {
        return `${phraseDict[input]}\n\n✅ Exact phrase match`;
    }

    // STEP 2: Check partial phrase matches  
    for (const [phrase, translation] of Object.entries(phraseDict)) {
        if (input.includes(phrase)) {
            const before = input.substring(0, input.indexOf(phrase));
            const after = input.substring(input.indexOf(phrase) + phrase.length);

            let parts = [];
            if (before.trim()) parts.push(translateWords(before));
            parts.push(translation);
            if (after.trim()) parts.push(translateWords(after));

            return `${parts.join(' ')}\n\n✨ Phrase + word match`;
        }
    }

    // STEP 3: Word-by-word with grammar
    return translateWords(input);
}

function translateWords(text) {
    const words = text
        .replace(/[.,!?;:"']/g, ' ')
        .split(/\s+/)
        .filter(w => w.length > 0);

    let translated = [];
    let foundWords = 0;

    for (const word of words) {
        // Skip articles
        if (grammar.ignore.includes(word)) {
            continue;
        }

        let trans = null;

        // Check grammar rules first
        if (grammar.pronouns[word]) {
            trans = grammar.pronouns[word];
            foundWords++;
        } else if (grammar.auxiliaries[word]) {
            trans = grammar.auxiliaries[word];
            foundWords++;
        } else if (grammar.prepositions[word]) {
            trans = grammar.prepositions[word];
            foundWords++;
        } else if (dictionary[word]) {
            trans = dictionary[word];
            foundWords++;
        } else {
            // Handle verb forms: -ing, -ed, -s
            let baseWord = word;
            let suffix = '';

            if (word.endsWith('ing')) {
                baseWord = word.slice(0, -3);
                suffix = ' raha';
            } else if (word.endsWith('ed')) {
                baseWord = word.slice(0, -2);
                suffix = ' gaya';
            } else if (word.endsWith('s') && word.length > 2) {
                baseWord = word.slice(0, -1);
            }

            if (dictionary[baseWord]) {
                trans = dictionary[baseWord] + suffix;
                foundWords++;
            } else {
                trans = `[${word}]`;
            }
        }

        translated.push(trans);
    }

    const totalWords = words.filter(w => !grammar.ignore.includes(w)).length;
    const coverage = totalWords > 0 ? Math.round((foundWords / totalWords) * 100) : 0;

    const emoji = coverage >= 80 ? '🎯' : coverage >= 50 ? '📊' : '⚠️';

    return `${translated.join(' ')}\n\n${emoji} ${foundWords}/${totalWords} words (${coverage}% coverage)`;
}

// ===================================
// EVENT HANDLERS (same as original)
// ===================================
translateBtn.addEventListener('click', async () => {
    const inputText = englishInput.value.trim();
    if (!inputText) return;

    translateBtn.disabled = true;
    translateBtn.innerHTML = `<span class="btn-text">Translating...</span>`;

    try {
        const translatedText = await translateText(inputText);
        banjaraOutput.innerHTML = translatedText;
        copyBtn.disabled = false;
        banjaraOutput.style.animation = 'fadeInUp 0.5s ease-out';
    } catch (error) {
        console.error('Translation error:', error);
        banjaraOutput.innerHTML = `<span style="color: #ff3b30;">⚠️ Translation failed</span>`;
    } finally {
        translateBtn.disabled = false;
        translateBtn.innerHTML = `<span class="btn-text">Translate</span>`;
    }
});

copyBtn.addEventListener('click', async () => {
    const outputText = banjaraOutput.textContent;
    try {
        await navigator.clipboard.writeText(outputText);
        const original = copyBtn.innerHTML;
        copyBtn.innerHTML = `<span>Copied!</span>`;
        copyBtn.style.color = '#34c759';
        setTimeout(() => {
            copyBtn.innerHTML = original;
            copyBtn.style.color = '';
        }, 2000);
    } catch (error) {
        console.error('Copy failed:', error);
        alert('Failed to copy text');
    }
});

englishInput.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        if (!translateBtn.disabled) translateBtn.click();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    translateBtn.disabled = true;
    englishInput.focus();
    console.log('🌐 Enhanced Banjara Translator v2.0 initialized');
    console.log('💡 Now with grammar rules and phrase matching!');
});
