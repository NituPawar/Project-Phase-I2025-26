"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer, Tooltip, Legend } from "recharts"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { useMemo } from "react"

interface PlatformComparisonChartProps {
  trends: any[]
}

export function PlatformComparisonChart({ trends }: PlatformComparisonChartProps) {
  const comparisonData = useMemo(() => {
    console.log("[v0] Comparison chart received trends:", trends.length)

    const normalizeName = (name: string) => {
      return name
        .toLowerCase()
        .replace(/^[#r/]+/, "")
        .replace(/\s+/g, "")
        .trim()
    }

    const trendMap = new Map<string, { twitter: number; reddit: number; displayName: string }>()

    trends.forEach((trend) => {
      const originalName = trend.name || trend.title || ""
      const normalizedName = normalizeName(originalName)
      const volume = trend.volume || trend.score || 0
      const platform = trend.platform

      if (!trendMap.has(normalizedName)) {
        const displayName = originalName.replace(/^[#r/]+/, "").trim()
        trendMap.set(normalizedName, { twitter: 0, reddit: 0, displayName })
      }

      const existing = trendMap.get(normalizedName)!
      if (platform === "twitter") {
        existing.twitter += volume
      } else if (platform === "reddit") {
        existing.reddit += volume
      }
    })

    console.log("[v0] Grouped topics:", trendMap.size)

    const result = Array.from(trendMap.values())
      .map((item) => ({
        ...item,
        total: item.twitter + item.reddit,
      }))
      .sort((a, b) => b.total - a.total)
      .slice(0, 10)
      .map((item) => ({
        name: item.displayName.substring(0, 15),
        fullName: item.displayName,
        Twitter: item.twitter,
        Reddit: item.reddit,
      }))

    console.log("[v0] Final comparison data:", result)
    return result
  }, [trends])

  const getTopPlatform = () => {
    const twitterTotal = comparisonData.reduce((sum, item) => sum + item.Twitter, 0)
    const redditTotal = comparisonData.reduce((sum, item) => sum + item.Reddit, 0)

    if (twitterTotal > redditTotal) {
      return { platform: "Twitter/X", percentage: ((twitterTotal / (twitterTotal + redditTotal)) * 100).toFixed(1) }
    } else if (redditTotal > twitterTotal) {
      return { platform: "Reddit", percentage: ((redditTotal / (twitterTotal + redditTotal)) * 100).toFixed(1) }
    }
    return { platform: "Both", percentage: "50.0" }
  }

  const topPlatform = getTopPlatform()

  return (
    <Card className="bg-card/50 backdrop-blur-sm border border-border">
      <CardHeader className="pb-4">
        <div className="flex items-start justify-between">
          <div>
            <CardTitle>Platform Comparison</CardTitle>
            <CardDescription>Side-by-side trend volume comparison (Twitter/X vs Reddit)</CardDescription>
          </div>
          {topPlatform && (
            <div className="text-right">
              <p className="text-xs text-muted-foreground">Leading Platform</p>
              <p className="text-sm font-semibold text-foreground">{topPlatform.platform}</p>
              <p className="text-xs text-muted-foreground">{topPlatform.percentage}% of volume</p>
            </div>
          )}
        </div>
      </CardHeader>
      <CardContent>
        {comparisonData.length > 0 ? (
          <div className="w-full h-[400px] bg-white rounded-lg p-4">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={comparisonData} margin={{ top: 10, right: 20, left: 0, bottom: 60 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" />
                <XAxis
                  dataKey="name"
                  stroke="#6b7280"
                  angle={-45}
                  textAnchor="end"
                  height={80}
                  fontSize={11}
                  tick={{ fill: "#374151" }}
                />
                <YAxis stroke="#6b7280" tick={{ fill: "#374151" }} />

                <Tooltip
                  contentStyle={{
                    backgroundColor: "#ffffff",
                    border: "1px solid #e5e7eb",
                    borderRadius: "8px",
                  }}
                  formatter={(value: any) => [value?.toLocaleString?.() || value, ""]}
                  labelFormatter={(label) => `Topic: ${label}`}
                  content={({ active, payload }) => {
                    if (active && payload && payload.length) {
                      const data = payload[0].payload
                      const total = data.Twitter + data.Reddit
                      const twitterPercent = total > 0 ? ((data.Twitter / total) * 100).toFixed(1) : "0.0"
                      const redditPercent = total > 0 ? ((data.Reddit / total) * 100).toFixed(1) : "0.0"

                      return (
                        <div className="bg-white border border-gray-200 rounded-lg p-3 shadow-lg">
                          <p className="font-semibold text-sm mb-2 text-gray-900">{data.fullName}</p>
                          <div className="space-y-1">
                            <div className="flex items-center justify-between gap-4">
                              <span className="text-xs font-medium text-blue-600">Twitter/X:</span>
                              <span className="text-xs text-gray-900">
                                {data.Twitter.toLocaleString()} ({twitterPercent}%)
                              </span>
                            </div>
                            <div className="flex items-center justify-between gap-4">
                              <span className="text-xs font-medium text-green-600">Reddit:</span>
                              <span className="text-xs text-gray-900">
                                {data.Reddit.toLocaleString()} ({redditPercent}%)
                              </span>
                            </div>
                            <div className="border-t pt-1 mt-1 flex items-center justify-between gap-4">
                              <span className="text-xs font-semibold text-gray-900">Total:</span>
                              <span className="text-xs font-semibold text-gray-900">{total.toLocaleString()}</span>
                            </div>
                          </div>
                        </div>
                      )
                    }
                    return null
                  }}
                />
                <Legend
                  wrapperStyle={{ paddingTop: "20px" }}
                  iconType="rect"
                  formatter={(value) => <span style={{ color: "#374151", fontSize: "12px" }}>{value}</span>}
                />
                <Bar dataKey="Twitter" fill="#3b82f6" radius={[4, 4, 0, 0]} />
                <Bar dataKey="Reddit" fill="#22c55e" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="flex items-center justify-center h-[400px] text-muted-foreground text-sm">
            No comparison data available. Try selecting "All" platforms to see the comparison.
          </div>
        )}
      </CardContent>
    </Card>
  )
}
