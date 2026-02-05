# Banjara Translation Crowdsourcing Platform

## Quick Start

### 1. Setup Firebase

Follow the instructions in `FIREBASE_SETUP.md` to:
- Create Firebase project
- Enable Authentication & Firestore
- Get your Firebase config
- Set security rules

### 2. Configure

Edit `firebase_auth.html` and `translate.html` - replace the Firebase config:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    // ... paste your config here
};
```

### 3. Upload Sentences

Upload the 10,000 sentences to Firestore using Node.js:

```bash
npm install firebase-admin
node upload_sentences.js
```

### 4. Deploy

```bash
git add .
git commit -m "Add Firebase crowdsourcing platform"
git push origin main
```

Enable GitHub Pages (Settings → Pages → main branch)

### 5. Share

Your platform will be live at:
```
https://YOUR_USERNAME.github.io/banjaratranslator/firebase_auth.html
```

Share this link with contributors!

---

## Files

| File | Purpose |
|------|---------|
| `firebase_auth.html` | Login/SignUp page |
| `translate.html` | Translation interface |
| `sentences_10k.json` | 10,000 English sentences |
| `upload_sentences.js` | Script to upload to Firebase |
| `FIREBASE_SETUP.md` | Detailed setup guide |

---

## How It Works

1. User signs up/logs in
2. System automatically assigns 200 unique sentences
3. User translates sentences one by one
4. All data saved to Firebase Firestore
5. Admin can export all translations to CSV

---

## For Contributors

- **Time needed**: ~4-6 hours for 200 sentences
- **Progress saved**: Auto-saves after each translation
- **Resume anytime**: Progress persists across sessions

---

## For Admin (You)

Access Firestore Console to:
- View all translations
- Export data to CSV
- Monitor progress
- Manage users

---

## Support

If contributors have issues, check:
1. Firebase config is correct
2. Authentication is enabled
3. Firestore rules are set
4. Sentences are uploaded
