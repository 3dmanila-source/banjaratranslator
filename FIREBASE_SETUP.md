# Firebase Setup Guide

## Step 1: Create Firebase Project

1. Go to: https://console.firebase.google.com/
2. Click **"Add project"**
3. Project name: `banjara-translation`
4. **Disable Google Analytics** (not needed, simpler)
5. Click **"Create project"**

---

## Step 2: Enable Authentication

1. In Firebase Console, click **"Authentication"** (left sidebar)
2. Click **"Get started"**
3. Enable **"Email/Password"**:
   - Click on it
   - Toggle **"Enable"**
   - Click **"Save"**
4. Enable **"Google"** (optional but recommended):
   - Click on it
   - Toggle **"Enable"**
   - Project public-facing name: `Banjara Translation`
   - Support email: Your email
   - Click **"Save"**

---

## Step 3: Enable Firestore Database

1. Click **"Firestore Database"** (left sidebar)
2. Click **"Create database"**
3. Security rules: **"Start in test mode"** (we'll add proper rules later)
4. Location: Choose closest region (e.g., `asia-south1` for India)
5. Click **"Enable"**

---

## Step 4: Get Firebase Configuration

1. Click **⚙️ (Settings icon)** → **"Project settings"**
2. Scroll down to **"Your apps"**
3. Click **"</>" (Web icon)**
4. App nickname: `Banjara Translation Web`
5. **DO NOT** check "Firebase Hosting"
6. Click **"Register app"**
7. **COPY** the Firebase configuration object:

```javascript
const firebaseConfig = {
  apiKey: "AIza...",
  authDomain: "your-project.firebaseapp.com",
  projectId: "your-project-id",
  storageBucket: "your-project.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123:web:abc123"
};
```

8. **SAVE THIS** - you'll need it in the code!

---

## Step 5: Set Security Rules (Important!)

Go to **Firestore Database** → **Rules** tab and paste:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Sentences: authenticated users can read
    match /sentences/{sentenceId} {
      allow read: if request.auth != null;
      allow write: if false;
    }
    
    // Translations: users can create their own
    match /translations/{translationId} {
      allow read: if request.auth != null;
      allow create: if request.auth != null 
        && request.resource.data.userId == request.auth.uid;
      allow update, delete: if false;
    }
    
    // Users: users can read all, write their own
    match /users/{userId} {
      allow read: if request.auth != null;
      allow write: if request.auth.uid == userId;
    }
    
    // Stats: everyone can read (for global progress)
    match /stats/{doc} {
      allow read: if request.auth != null;
      allow write: if false;
    }
  }
}
```

Click **"Publish"**

---

## Step 6: Upload Initial Data

We'll create a script to upload the 10,000 sentences. You'll need:

1. Install Node.js (if not already installed)
2. Run the upload script (I'll create this)

---

## Step 7: Deploy to GitHub Pages

Once everything is ready:
1. Push all files to GitHub
2. Enable GitHub Pages (Settings → Pages → main branch)
3. Your app will be live!

---

## ✅ Checklist

- [ ] Firebase project created
- [ ] Authentication enabled (Email + Google)
- [ ] Firestore database created
- [ ] Firebase config copied
- [ ] Security rules set
- [ ] Ready for sentence upload

**Next**: Once you complete these steps, paste your Firebase config and I'll integrate it into the code!
