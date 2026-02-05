/**
 * Upload 10,000 sentences to Firebase Firestore
 * 
 * Setup:
 * 1. Install Node.js
 * 2. Run: npm install firebase
 * 3. Run: node upload_sentences.js
 */

const firebase = require('firebase/compat/app');
require('firebase/compat/firestore');
const fs = require('fs');

// Firebase config
const firebaseConfig = {
    apiKey: "AIzaSyAeW0tNBQay4Q24QTzJoyBu0FcxyAhodSQ",
    authDomain: "banjaraai.firebaseapp.com",
    projectId: "banjaraai",
    storageBucket: "banjaraai.firebasestorage.app",
    messagingSenderId: "669417689803",
    appId: "1:669417689803:web:5c9c222d91b0e95e7f814e"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

async function uploadSentences() {
    console.log('Loading sentences from JSON...');

    // Load sentences
    const sentencesData = fs.readFileSync('sentences_10k.json', 'utf8');
    const sentences = JSON.parse(sentencesData);

    console.log(`Loaded ${sentences.length} sentences`);
    console.log('Starting upload to Firestore...\n');

    // Upload in batches of 500 (Firestore limit is 500 per batch)
    const batchSize = 500;
    const batches = Math.ceil(sentences.length / batchSize);

    for (let i = 0; i < batches; i++) {
        const batch = db.batch();
        const start = i * batchSize;
        const end = Math.min(start + batchSize, sentences.length);

        console.log(`Batch ${i + 1}/${batches}: Uploading sentences ${start + 1} to ${end}...`);

        for (let j = start; j < end; j++) {
            const sentence = sentences[j];
            const docRef = db.collection('sentences').doc(sentence.id.toString());
            batch.set(docRef, {
                id: sentence.id,
                english: sentence.text,
                category: sentence.category,
                difficulty: sentence.difficulty,
                assignedTo: [],
                completedBy: 0,
                createdAt: firebase.firestore.FieldValue.serverTimestamp()
            });
        }

        await batch.commit();
        console.log(`✓ Batch ${i + 1} uploaded successfully\n`);

        // Small delay to avoid rate limits
        if (i < batches - 1) {
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    }

    // Initialize global stats
    console.log('Initializing global stats...');
    await db.collection('stats').doc('global').set({
        totalSentences: sentences.length,
        totalTranslations: 0,
        totalUsers: 0,
        lastUpdated: firebase.firestore.FieldValue.serverTimestamp()
    });

    console.log('\n✅ Upload complete!');
    console.log(`Total sentences uploaded: ${sentences.length}`);
    console.log('\nYour crowdsourcing platform is ready to use! 🎉');

    process.exit(0);
}

uploadSentences().catch(error => {
    console.error('Error uploading sentences:', error);
    process.exit(1);
});
