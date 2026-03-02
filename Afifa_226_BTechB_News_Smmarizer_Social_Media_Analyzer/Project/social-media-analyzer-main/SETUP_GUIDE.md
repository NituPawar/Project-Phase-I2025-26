# Local Environment Setup Guide

## System Requirements

Before you begin, ensure you have the following installed on your PC:

- **Node.js** (v18 or higher) - [Download here](https://nodejs.org/)
- **npm** (comes with Node.js) or **yarn**
- **Git** (optional but recommended) - [Download here](https://git-scm.com/)
- **Text Editor/IDE** - VS Code recommended - [Download here](https://code.visualstudio.com/)

---

## Step 1: Verify Node.js & npm Installation

Open Command Prompt or PowerShell and run:

\`\`\`bash
node --version
npm --version
\`\`\`

You should see version numbers for both. If not, install Node.js from the link above.

---

## Step 2: Extract and Navigate to Project

1. Extract the downloaded ZIP file to your desired location
2. Open Command Prompt/PowerShell
3. Navigate to the project folder:

\`\`\`bash
cd C:\Users\Test\Downloads\social-media-analyzer
\`\`\`

Replace the path with your actual project location.

---

## Step 3: Install Dependencies

Run the following command to install all project dependencies:

\`\`\`bash
npm install
\`\`\`

If you encounter peer dependency errors, use:

\`\`\`bash
npm install --legacy-peer-deps
\`\`\`

Wait for the installation to complete. This may take 2-5 minutes.

---

## Step 4: Get API Credentials

### 4A. Twitter/X API Credentials

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new app or use existing one
3. Navigate to **Keys and Tokens**
4. Copy your **Bearer Token** (it starts with `AAAA...`)
5. Keep this token safe - you'll need it in the next step

**Note:** If you don't have developer access, apply for elevated access on the same page.

### 4B. Reddit API Credentials

1. Go to [Reddit App Preferences](https://www.reddit.com/prefs/apps)
2. Click **"Create App"** or **"Create Another App"**
3. Fill in the form:
   - **Name**: Social Media Analyzer (or any name)
   - **App type**: Select "Script"
   - **Redirect URI**: `http://localhost:3000` (for local development)
   - Click **"Create App"**
4. You'll see:
   - **Client ID**: Below the app name (copy this)
   - **Client Secret**: Click "show" to reveal (copy this)
5. Keep both values safe - you'll need them in the next step

---

## Step 5: Create Environment Variables File

1. In your project root folder, create a new file named `.env.local`
2. Add the following content and replace with your actual credentials:

\`\`\`
# Twitter/X API
TWITTER_API_BEARER_TOKEN=your_twitter_bearer_token_here

# Reddit API
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
\`\`\`

**Example (with fake credentials for reference):**

\`\`\`
TWITTER_API_BEARER_TOKEN=AAAAAu4y8c%2Fj8AAAA%2FG2A%2BV7W8u%2B%2FE%2Fj8AAAA
REDDIT_CLIENT_ID=aBcDeFgHiJkLmNoPqRsT
REDDIT_CLIENT_SECRET=xYzAbCdEfGhIjKlMnOpQrStUvWxYz
\`\`\`

3. Save the file as `.env.local` (not `.env.local.txt`)

**IMPORTANT SECURITY NOTES:**
- Never commit `.env.local` to git
- The `.gitignore` file should already include it
- Never share these credentials with anyone
- If compromised, regenerate them immediately from the respective platforms

---

## Step 6: Verify Environment Variables Are Loaded

1. In your project root, open Command Prompt/PowerShell
2. Run:

\`\`\`bash
npm run dev
\`\`\`

The application should start. Watch for any errors mentioning missing environment variables.

---

## Step 7: Start the Development Server

With your `.env.local` file in place, run:

\`\`\`bash
npm run dev
\`\`\`

You should see output like:

\`\`\`
> next dev
  ▲ Next.js 15.x.x
  - Local:        http://localhost:3000
\`\`\`

---

## Step 8: Access the Application

1. Open your web browser
2. Go to `http://localhost:3000`
3. You should see the Social Media Trend Analyzer dashboard
4. The app will now fetch real trends from Twitter/X and Reddit

---

## Troubleshooting

### "Cannot find module" Error

**Solution:**
\`\`\`bash
npm install --legacy-peer-deps
\`\`\`

### Port 3000 Already in Use

**Solution:** Use a different port:
\`\`\`bash
npm run dev -- -p 3001
\`\`\`

Then visit `http://localhost:3001`

### Environment Variables Not Loading

**Verify your `.env.local` file:**
1. It must be in the project root (same level as `package.json`)
2. Filename must be exactly `.env.local` (not `.env.local.txt`)
3. After creating/editing `.env.local`, restart the dev server

**To check if variables are loaded:**
- Check your browser console for debug logs
- Look at the terminal output for warnings about missing credentials

### "Reddit API credentials not configured"

**Solution:**
1. Double-check your `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET` in `.env.local`
2. Ensure there are no extra spaces or quotes around the values
3. Restart the dev server after saving `.env.local`
4. Clear browser cache (Ctrl+Shift+Delete)

### "Twitter API Bearer Token Invalid"

**Solution:**
1. Verify the bearer token is copied completely (very long string)
2. Ensure it hasn't expired in Twitter Developer Portal
3. Generate a new one if needed
4. Update `.env.local` with the new token
5. Restart dev server

### Charts Not Displaying Data

**Solution:**
1. Check browser console for errors (F12 → Console tab)
2. Verify both API credentials are correct
3. Wait 10-15 seconds for data to load
4. If using mock data only, ensure env variables are set
5. Try refreshing the page

---

## Production Deployment

When ready to deploy to production:

1. Use **Vercel** (recommended):
   - Push your code to GitHub
   - Connect GitHub to Vercel
   - Add environment variables in Vercel Dashboard → Settings → Environment Variables
   - Deploy with one click

2. Add your real API credentials in Vercel (not in code):
   - `TWITTER_API_BEARER_TOKEN`
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`

---

## Project Structure

\`\`\`
social-media-analyzer/
├── app/
│   ├── api/
│   │   └── trends/              # API routes for fetching trends
│   ├── globals.css              # Global styles
│   ├── layout.tsx               # Root layout
│   └── page.tsx                 # Main dashboard page
├── components/
│   ├── trending-topics-chart.tsx
│   ├── trend-item.tsx
│   ├── trends-list.tsx
│   ├── platform-selector.tsx
│   └── ...                       # Other components
├── lib/
│   ├── twitter-service.ts       # Twitter API integration
│   ├── reddit-service.ts        # Reddit API integration
│   └── utils.ts
├── hooks/
│   └── use-trends.ts            # Data fetching hook
├── .env.local                    # Environment variables (CREATE THIS)
├── .gitignore
├── package.json
├── tsconfig.json
└── README.md
\`\`\`

---

## Quick Command Reference

\`\`\`bash
# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Install dependencies
npm install

# Clear npm cache (if issues occur)
npm cache clean --force
\`\`\`

---

## Need Help?

- **Next.js Documentation**: https://nextjs.org/docs
- **Twitter API Docs**: https://developer.twitter.com/en/docs
- **Reddit API Docs**: https://www.reddit.com/dev/api
- **Common Issues**: Check the Troubleshooting section above

---

## Security Reminders

✓ Never commit `.env.local` to version control  
✓ Never share API credentials  
✓ Keep credentials in `.env.local` only  
✓ Regenerate credentials if they're compromised  
✓ Use `.gitignore` to prevent accidental commits  

Happy analyzing! 🚀
