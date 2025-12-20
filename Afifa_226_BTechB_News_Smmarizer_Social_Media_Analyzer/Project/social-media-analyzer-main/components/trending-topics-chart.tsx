"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer, Tooltip, Cell } from "recharts"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { useMemo } from "react"
import { TrendingUp, TrendingDown, Minus } from "lucide-react"

interface TrendingTopicsChartProps {
  trends: any[]
}

export function TrendingTopicsChart({ trends }: TrendingTopicsChartProps) {
  const chartData = useMemo(() => {
    if (!trends || trends.length === 0) return []

    return trends.slice(0, 10).map((trend, index) => ({
      name: (trend.name || trend.title || "").replace(/^[#r/]/, "").substring(0, 12),
      volume: trend.volume || trend.score || 0,
      fullName: trend.name || trend.title,
      growthIndicator: trend.growthIndicator || "stable",
      growthRate: trend.growthRate || 0,
    }))
  }, [trends])

  const getBarColor = (indicator: string) => {
    switch (indicator) {
      case "rising":
        return "#22c55e" // green
      case "falling":
        return "#ef4444" // red
      case "stable":
      default:
        return "#3b82f6" // blue
    }
  }

  return (
    <Card className="bg-card/50 backdrop-blur-sm border border-border">
      <CardHeader className="pb-4">
        <div className="flex items-start justify-between">
          <div>
            <CardTitle>Trending Topics</CardTitle>
            <CardDescription>Top 10 trending topics by mention volume</CardDescription>
          </div>
          <div className="flex flex-col gap-1 text-xs">
            <div className="flex items-center gap-1 text-green-500">
              <TrendingUp className="w-3 h-3" />
              <span>Rising</span>
            </div>
            <div className="flex items-center gap-1 text-red-500">
              <TrendingDown className="w-3 h-3" />
              <span>Falling</span>
            </div>
            <div className="flex items-center gap-1 text-blue-500">
              <Minus className="w-3 h-3" />
              <span>Stable</span>
            </div>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        {chartData.length > 0 ? (
          <div className="w-full h-[350px] bg-white rounded-lg p-4">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={chartData} margin={{ top: 10, right: 20, left: 0, bottom: 50 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#e5e7eb" vertical={true} />
                <XAxis
                  dataKey="name"
                  stroke="#6b7280"
                  angle={-45}
                  textAnchor="end"
                  height={80}
                  fontSize={12}
                  tick={{ fill: "#6b7280" }}
                />
                <YAxis stroke="#6b7280" tick={{ fill: "#6b7280" }} />
                <Tooltip
                  contentStyle={{
                    backgroundColor: "#ffffff",
                    border: "1px solid #e5e7eb",
                    borderRadius: "8px",
                  }}
                  formatter={(value: any) => [value?.toLocaleString?.() || value, "Volume"]}
                  labelFormatter={(label) => `Topic: ${label}`}
                  content={({ active, payload }) => {
                    if (active && payload && payload.length) {
                      const data = payload[0].payload
                      return (
                        <div className="bg-white border border-gray-200 rounded-lg p-3 shadow-lg">
                          <p className="font-semibold text-sm mb-1 text-gray-900">{data.fullName}</p>
                          <p className="text-sm text-gray-700">Volume: {data.volume.toLocaleString()}</p>
                          {data.growthRate !== 0 && (
                            <p className="text-sm flex items-center gap-1 mt-1">
                              {data.growthIndicator === "rising" && (
                                <>
                                  <TrendingUp className="w-3 h-3 text-green-500" />
                                  <span className="text-green-500">+{data.growthRate}%</span>
                                </>
                              )}
                              {data.growthIndicator === "falling" && (
                                <>
                                  <TrendingDown className="w-3 h-3 text-red-500" />
                                  <span className="text-red-500">{data.growthRate}%</span>
                                </>
                              )}
                              {data.growthIndicator === "stable" && (
                                <>
                                  <Minus className="w-3 h-3 text-yellow-500" />
                                  <span className="text-yellow-500">{data.growthRate}%</span>
                                </>
                              )}
                            </p>
                          )}
                        </div>
                      )
                    }
                    return null
                  }}
                />
                <Bar dataKey="volume" radius={[8, 8, 0, 0]} animationDuration={800}>
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={getBarColor(entry.growthIndicator)} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        ) : (
          <div className="flex items-center justify-center h-[350px] text-muted-foreground text-sm">
            No trending data available. Configure API credentials or check back later.
          </div>
        )}
      </CardContent>
    </Card>
  )
}
