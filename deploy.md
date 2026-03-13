# Langkah Deploy Flask ke Vercel

## 1. Install Vercel CLI
```bash
npm install -g vercel
```

## 2. Login ke Vercel
```bash
vercel login
```
Ikuti instruksi untuk login via browser/email.

## 3. Deploy
```bash
cd /home/mardommah/Documents/makassar-coding/backend-firebase
vercel
```
Saat pertama kali, Vercel akan bertanya:
- **Set up and deploy?** → `Y`
- **Which scope?** → pilih akun kamu
- **Link to existing project?** → `N`
- **Project name?** → ketik nama project
- **In which directory is your code located?** → `./` (tekan Enter)

## 4. Deploy ke Production
```bash
vercel --prod
```

## 5. Setup Firebase Credentials di Vercel

File `creds.json` **tidak** boleh di-push ke git. Sebagai gantinya, simpan sebagai environment variable.

### Encode creds.json ke Base64
```bash
base64 -w 0 creds.json
```
Copy seluruh output-nya.

### Tambahkan ke Vercel

**Via CLI:**
```bash
vercel env add FIREBASE_CREDENTIALS
```
Paste nilai base64 saat diminta.

**Via Dashboard:**
1. Buka vercel.com → pilih project
2. **Settings → Environment Variables**
3. Name: `FIREBASE_CREDENTIALS`
4. Value: paste hasil base64
5. Centang **Production**, **Preview**, **Development**
6. Klik **Save**

### Redeploy setelah set env var
```bash
vercel --prod
```
