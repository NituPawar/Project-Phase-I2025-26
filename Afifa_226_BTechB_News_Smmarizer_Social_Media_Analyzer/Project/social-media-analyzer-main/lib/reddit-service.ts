// Reddit API service
// Requires REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET environment variables

interface RedditTrend {
  name: string
  platform: "reddit"
  volume: number
  score?: number
  subscribers?: number
}

let redditAccessToken: string | null = null
let tokenExpiry = 0

async function getRedditAccessToken(): Promise<string> {
  // Return cached token if still valid
  if (redditAccessToken && Date.now() < tokenExpiry) {
    return redditAccessToken
  }

  const clientId = process.env.REDDIT_CLIENT_ID
  const clientSecret = process.env.REDDIT_CLIENT_SECRET

  if (!clientId || !clientSecret) {
    return ""
  }

  try {
    const auth = Buffer.from(`${clientId}:${clientSecret}`).toString("base64")

    const response = await fetch("https://www.reddit.com/api/v1/access_token", {
      method: "POST",
      headers: {
        Authorization: `Basic ${auth}`,
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "TrendAnalyzer/1.0",
      },
      body: "grant_type=client_credentials",
    })

    if (!response.ok) {
      throw new Error(`Reddit auth failed: ${response.statusText}`)
    }

    const data = await response.json()
    redditAccessToken = data.access_token
    tokenExpiry = Date.now() + data.expires_in * 1000

    return redditAccessToken
  } catch (error) {
    console.error("Error getting Reddit access token:", error)
    throw error
  }
}

export async function getRedditTrends(): Promise<RedditTrend[]> {
  try {
    const token = await getRedditAccessToken()

    if (!token) {
      console.log("Reddit API credentials not configured. Using mock data.")
      return getMockRedditTrends()
    }

    // Fetch trending subreddits
    const response = await fetch("https://oauth.reddit.com/trending", {
      headers: {
        Authorization: `Bearer ${token}`,
        "User-Agent": "TrendAnalyzer/1.0",
      },
    })

    if (!response.ok) {
      console.warn("Reddit API error. Using mock data.")
      return getMockRedditTrends()
    }

    const data = await response.json()

    return (data.data?.children || []).map((subreddit: any) => ({
      name: subreddit.data.display_name,
      platform: "reddit" as const,
      volume: subreddit.data.subscribers || 0,
      score: subreddit.data.public_description_html ? 1 : 0,
      subscribers: subreddit.data.subscribers,
    }))
  } catch (error) {
    console.error("Error fetching Reddit trends:", error)
    return getMockRedditTrends()
  }
}

function getMockRedditTrends(): RedditTrend[] {
  return [
    { name: "r/programming", platform: "reddit", volume: 34521, score: 8234, subscribers: 3400000 },
    { name: "r/webdev", platform: "reddit", volume: 28901, score: 7156, subscribers: 850000 },
    { name: "r/AI", platform: "reddit", volume: 27500, score: 6890, subscribers: 920000 },
    { name: "r/Advocacy", platform: "reddit", volume: 26543, score: 6543, subscribers: 680000 },
    { name: "r/learnprogramming", platform: "reddit", volume: 24567, score: 6234, subscribers: 1200000 },
    { name: "r/javascript", platform: "reddit", volume: 21345, score: 5678, subscribers: 750000 },
    { name: "r/reactjs", platform: "reddit", volume: 18234, score: 4832, subscribers: 500000 },
    { name: "r/RemoteWork", platform: "reddit", volume: 17890, score: 4321, subscribers: 420000 },
    { name: "r/nextjs", platform: "reddit", volume: 15678, score: 3921, subscribers: 350000 },
    { name: "r/typescript", platform: "reddit", volume: 13456, score: 3245, subscribers: 280000 },
  ]
}
