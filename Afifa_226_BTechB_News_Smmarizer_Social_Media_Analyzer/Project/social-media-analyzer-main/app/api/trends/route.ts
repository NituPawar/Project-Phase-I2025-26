import { type NextRequest, NextResponse } from "next/server"
import { getTwitterTrends } from "@/lib/twitter-service"
import { getRedditTrends } from "@/lib/reddit-service"

export async function GET(request: NextRequest) {
  try {
    const searchParams = request.nextUrl.searchParams
    const platform = searchParams.get("platform") || "all"

    let trends: any[] = []

    if (platform === "twitter" || platform === "all") {
      const twitterTrends = await getTwitterTrends()
      trends = [...trends, ...twitterTrends]
    }

    if (platform === "reddit" || platform === "all") {
      const redditTrends = await getRedditTrends()
      trends = [...trends, ...redditTrends]
    }

    // Sort by volume descending
    trends.sort((a, b) => {
      const aVolume = a.volume || a.score || 0
      const bVolume = b.volume || b.score || 0
      return bVolume - aVolume
    })

    return NextResponse.json(trends, {
      headers: {
        "Cache-Control": "public, s-maxage=300, stale-while-revalidate=600",
      },
    })
  } catch (error) {
    console.error("Error in trends API:", error)
    return NextResponse.json({ error: "Failed to fetch trends" }, { status: 500 })
  }
}
