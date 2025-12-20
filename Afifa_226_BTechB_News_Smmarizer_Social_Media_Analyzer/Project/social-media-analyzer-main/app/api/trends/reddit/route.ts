import { NextResponse } from "next/server"
import { getRedditTrends } from "@/lib/reddit-service"

export async function GET() {
  try {
    const trends = await getRedditTrends()
    return NextResponse.json(trends, {
      headers: {
        "Cache-Control": "public, s-maxage=300, stale-while-revalidate=600",
      },
    })
  } catch (error) {
    console.error("Error in Reddit trends API:", error)
    return NextResponse.json({ error: "Failed to fetch Reddit trends" }, { status: 500 })
  }
}
