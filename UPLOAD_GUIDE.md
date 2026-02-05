# How to Upload Sentences to Firebase

## Option 1: Using Firebase Console (Recommended for first time)

### Method A: Manual Import (Easy)
1. Go to Firebase Console: https://console.firebase.google.com/
2. Select your project: `banjaraAI`
3. Click **"Firestore Database"** in left sidebar
4. Click **"Start collection"**
5. Collection ID: `sentences`
6. Click **"Next"**
7. Document ID: `1`
8. Add fields:
   - `id` (number): `1`
   - `english` (string): `Hello`
   - `category` (string): `greeting`
   - `difficulty` (string): `easy`
   - `assignedTo` (array): empty
   - `completedBy` (number): `0`
9. Click **"Save"**

**Problem:** This will take forever for 10,000 sentences!

---

## Option 2: Using Node.js Script (BEST - Automated)

### If npm doesn't work, try this:

**Step 1**: Open PowerShell as Administrator
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Step 2**: Navigate and install
```powershell
cd "i:\Banjara AI"
npm install
```

**Step 3**: Run upload script
```powershell
node upload_sentences.js
```

This will upload all 10,000 sentences in ~2-3 minutes!

---

## Option 3: Use Firebase CLI (Alternative)

### Install Firebase CLI
```powershell
npm install -g firebase-tools
```

### Login and deploy
```powershell
firebase login
firebase firestore:import sentences_firestore_export/ --project banjaraai
```

---

## Quick Test (Without uploading all 10,000)

For testing, I can create a smaller version with just 50 sentences:

**Want me to create**:
- `sentences_50_test.json` (50 sentences only)
- `upload_test.js` (quick test upload)

Then you can test the system with 50 sentences first, and upload all 10,000 later!

**Which option would you prefer?**
