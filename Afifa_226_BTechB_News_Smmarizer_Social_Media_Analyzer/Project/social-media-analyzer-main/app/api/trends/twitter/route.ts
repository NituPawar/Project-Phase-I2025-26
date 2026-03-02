import { NextResponse } from "next/server"
import { getTwitterTrends } from "@/lib/twitter-service"

export async function GET() {
  try {
    const trends = await getTwitterTrends()
    return NextResponse.json(trends, {
      headers: {
        "Cache-Control": "public, s-maxage=300, stale-while-revalidate=600",
      },
    })
  } catch (error) {
    console.error("Error in Twitter trends API:", error)
    return NextResponse.json({ error: "Failed to fetch Twitter trends" }, { status: 500 })
  }
}
