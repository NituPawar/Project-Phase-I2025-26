# Social Media Trend Analyzer

A real-time trend analyzer dashboard that tracks trending topics from Twitter/X and Reddit with interactive visualizations and advanced filtering capabilities.

## Features

- **Real-time Trend Tracking**: Monitor trending topics from Twitter/X and Reddit simultaneously
- **Dual Platform Support**: Toggle between Twitter/X, Reddit, or view combined trends
- **Interactive Visualizations**: Bar and line charts with live data updates
- **Advanced Filtering**: Search trends by name and filter by engagement volume
- **Auto-refresh**: Automatic data updates with configurable intervals
- **Trend Details**: Click any trend to view platform-specific information and direct links
- **Statistics Dashboard**: View engagement metrics and breakdown by platform
- **Dark Mode**: Professional dark-themed UI optimized for data analysis

## Tech Stack

- **Framework**: Next.js 16 (App Router)
- **UI Components**: shadcn/ui with Tailwind CSS
- **Data Visualization**: Recharts
- **Data Fetching**: SWR (Stale-While-Revalidate)
- **APIs**: Twitter/X v2 API, Reddit API
- **Language**: TypeScript

## Getting Started

### Prerequisites

You'll need API credentials from both platforms to enable real data fetching:

1. **Twitter/X API Access**
   - Visit [developer.twitter.com](https://developer.twitter.com)
   - Create an application and get approved for API v2 access
   - Generate your Bearer Token
   - Copy your `TWITTER_API_BEARER_TOKEN`

2. **Reddit API Credentials**
   - Visit [reddit.com/prefs/apps](https://reddit.com/prefs/apps)
   - Click "Create App" or "Create Another App"
   - Choose "Script" as the app type
   - Get your `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET`

### Installation

1. Clone the repository:
\`\`\`bash
git clone <repository-url>
cd social-media-analyzer
\`\`\`

2. Install dependencies:
\`\`\`bash
npm install
\`\`\`

3. Add Environment Variables:
   - In v0: Click **Vars** in the left sidebar and add:
     - `TWITTER_API_BEARER_TOKEN`: Your Twitter/X Bearer Token
     - `REDDIT_CLIENT_ID`: Your Reddit Client ID
     - `REDDIT_CLIENT_SECRET`: Your Reddit Client Secret

4. Run the development server:
\`\`\`bash
npm run dev
\`\`\`

5. Open [http://localhost:3000](http://localhost:3000) in your browser

## Configuration

### Environment Variables

\`\`\`env
# Twitter/X API (required for real Twitter data)
TWITTER_API_BEARER_TOKEN=your_bearer_token_here

# Reddit API (required for real Reddit data)
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
\`\`\`

**Note**: If environment variables are not configured, the app will use mock data for demonstration purposes.

## Usage

### Platform Selection
Use the platform selector buttons to toggle between:
- **Twitter/X**: See trending hashtags and topics from Twitter
- **Reddit**: See trending subreddits
- **All**: View combined trends from both platforms

### Filtering & Search
- **Search Box**: Search trends by name or hashtag
- **Volume Filter**: Set minimum engagement threshold to filter out low-volume trends
- **Auto-refresh**: Enable/disable automatic data updates

### Chart Interactions
- **Toggle Chart Type**: Switch between bar and line chart visualizations
- **Hover Details**: Hover over chart bars to see trend details
- **Responsive**: Charts automatically adjust to screen size

### View Trend Details
- Click on any trend in the list to open the details modal
- View platform-specific information
- Get direct links to Twitter/X search or Reddit subreddit pages

## Project Structure

\`\`\`
├── app/
│   ├── layout.tsx                 # Root layout with theme setup
│   ├── page.tsx                   # Main dashboard page
│   ├── globals.css               # Global styles and design tokens
│   └── api/
│       └── trends/
│           ├── route.ts          # Combined trends endpoint
│           ├── twitter/
│           │   └── route.ts      # Twitter/X API route
│           └── reddit/
│               └── route.ts      # Reddit API route
├── components/
│   ├── platform-selector.tsx     # Platform toggle buttons
│   ├── trending-topics-chart.tsx # Main visualization chart
│   ├── platform-stats.tsx        # Statistics cards
│   ├── trends-list.tsx           # Scrollable trends list
│   ├── trend-item.tsx            # Individual trend row
│   ├── trend-chart.tsx           # Chart configuration
│   ├── trend-search.tsx          # Search input
│   ├── trend-filter.tsx          # Volume filter
│   └── trend-details-modal.tsx   # Trend details popup
├── hooks/
│   └── use-trends.ts             # Data fetching hook with SWR
├── lib/
│   ├── twitter-service.ts        # Twitter/X API integration
│   └── reddit-service.ts         # Reddit API integration
└── public/
    └── placeholder.svg           # Placeholder images
\`\`\`

## API Routes

### GET `/api/trends`
Fetches combined trends from all enabled platforms.

**Response Example**:
\`\`\`json
{
  "trends": [
    {
      "name": "#TrendingTopic",
      "platform": "twitter",
      "volume": 45230,
      "url": "https://twitter.com/search?q=%23TrendingTopic"
    },
    {
      "name": "r/programming",
      "platform": "reddit",
      "volume": 34521,
      "subscribers": 3400000
    }
  ]
}
\`\`\`

### GET `/api/trends/twitter`
Fetches trending topics from Twitter/X only.

### GET `/api/trends/reddit`
Fetches trending topics from Reddit only.

## Features in Detail

### Real-time Updates
- Data auto-refreshes every 60 seconds (configurable)
- Manual refresh button for immediate updates
- SWR caching prevents unnecessary API calls

### Data Fallback
- If API credentials are missing, mock data displays automatically
- If API calls fail, cached data is used
- Error messages inform users of issues

### Performance Optimization
- API responses cached with 60-second TTL
- Client-side filtering prevents unnecessary re-renders
- Lazy-loaded components for improved initial load

### Mobile Responsive
- Fully responsive design for mobile, tablet, and desktop
- Touch-friendly controls and interactive elements
- Stacked layout on smaller screens

## Troubleshooting

### "Error loading trends" message
- Check that API credentials are correctly added to environment variables
- Verify Twitter/X and Reddit API keys are valid
- Check API rate limits haven't been exceeded
- The app will use mock data if APIs fail

### Chart not updating
- Click the "Refresh" button to manually fetch new data
- Check "Auto-refresh" is enabled for automatic updates
- Clear browser cache if data seems stale

### No trends displayed
- Ensure at least one platform is selected
- Try adjusting the volume filter to a lower value
- Click refresh to fetch new data

## Deployment

### Deploy to Vercel
1. Push your code to GitHub
2. Connect the repository to Vercel
3. Add environment variables in Vercel Project Settings:
   - `TWITTER_API_BEARER_TOKEN`
   - `REDDIT_CLIENT_ID`
   - `REDDIT_CLIENT_SECRET`
4. Deploy with `npm run build && npm run start`

### Deploy to Other Platforms
The app works on any platform supporting Node.js 18+:
- Railway
- Render
- DigitalOcean
- Self-hosted servers

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

MIT License - feel free to use this project for personal or commercial purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review API documentation for your platform:
   - [Twitter API Docs](https://developer.twitter.com/en/docs/api)
   - [Reddit API Docs](https://www.reddit.com/dev/api)
3. Open an issue in the repository

## Roadmap

- [ ] Support for additional platforms (TikTok, Instagram)
- [ ] Historical trend data and analytics
- [ ] Trend predictions and forecasting
- [ ] Custom alerts for specific trends
- [ ] Data export capabilities
- [ ] Advanced filtering and tagging system
