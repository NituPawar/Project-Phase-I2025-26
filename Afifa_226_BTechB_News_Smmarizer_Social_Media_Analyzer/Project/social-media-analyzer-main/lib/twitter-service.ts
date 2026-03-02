// Twitter/X API service
// Requires TWITTER_API_BEARER_TOKEN environment variable

interface TwitterTrend {
  name: string
  platform: "twitter"
  volume: number
  url?: string
}

export async function getTwitterTrends(): Promise<TwitterTrend[]> {
  const bearerToken = process.env.TWITTER_API_BEARER_TOKEN

  if (!bearerToken) {
    console.warn("Twitter API token not configured. Using mock data.")
    return getMockTwitterTrends()
  }

  try {
    const response = await fetch("https://api.twitter.com/2/trends/trending", {
      headers: {
        Authorization: `Bearer ${bearerToken}`,
      },
    })

    if (!response.ok) {
      console.warn("Twitter API error. Using mock data.")
      return getMockTwitterTrends()
    }

    const data = await response.json()

    // Transform Twitter API response
    return (data.trends || []).map((trend: any) => ({
      name: trend.name,
      platform: "twitter" as const,
      volume: trend.volume || trend.tweet_volume || 0,
      url: trend.url,
    }))
  } catch (error) {
    console.error("Error fetching Twitter trends:", error)
    return getMockTwitterTrends()
  }
}

function getMockTwitterTrends(): TwitterTrend[] {
  return [
    { name: "#TrendingNow", platform: "twitter", volume: 45230 },
    { name: "#programming", platform: "twitter", volume: 34521 },
    { name: "#WebDevelopment", platform: "twitter", volume: 32156 },
    { name: "#AI", platform: "twitter", volume: 28942 },
    { name: "#Advocacy", platform: "twitter", volume: 27654 },
    { name: "#React", platform: "twitter", volume: 25634 },
    { name: "#RemoteWork", platform: "twitter", volume: 23876 },
    { name: "#JavaScript", platform: "twitter", volume: 22108 },
    { name: "#NextJS", platform: "twitter", volume: 18234 },
    { name: "#TypeScript", platform: "twitter", volume: 15672 },
  ]
}
