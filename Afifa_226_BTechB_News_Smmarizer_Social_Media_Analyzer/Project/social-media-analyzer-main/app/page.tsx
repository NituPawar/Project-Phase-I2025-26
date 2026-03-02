"use client"

import { useState, useMemo } from "react"
import { Card, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { TrendingTopicsChart } from "@/components/trending-topics-chart"
import { PlatformSelector } from "@/components/platform-selector"
import { TrendsList } from "@/components/trends-list"
import { PlatformStats } from "@/components/platform-stats"
import { TrendSearch } from "@/components/trend-search"
import { TrendFilter } from "@/components/trend-filter"
import { TrendDetailsModal } from "@/components/trend-details-modal"
import { PlatformComparisonChart } from "@/components/platform-comparison-chart"
import { useTrends } from "@/hooks/use-trends"

export default function Home() {
  const [platform, setPlatform] = useState<"twitter" | "reddit" | "all">("all")
  const [autoRefresh, setAutoRefresh] = useState(true)
  const [searchQuery, setSearchQuery] = useState("")
  const [minVolume, setMinVolume] = useState(0)
  const [selectedTrend, setSelectedTrend] = useState<any | null>(null)

  const { trends, isLoading, error, refresh } = useTrends({
    platform,
    refreshInterval: autoRefresh ? 60000 : 0,
  })

  const filteredTrends = useMemo(() => {
    return trends.filter((trend) => {
      const volume = trend.volume || trend.score || 0
      const matchesSearch = (trend.name || trend.title || "").toLowerCase().includes(searchQuery.toLowerCase())
      const meetsVolume = volume >= minVolume
      return matchesSearch && meetsVolume
    })
  }, [trends, searchQuery, minVolume])

  return (
    <div className="min-h-screen bg-background">
      <header className="border-b border-border bg-card/50 backdrop-blur-sm sticky top-0 z-50">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
            <div>
              <h1 className="text-3xl font-bold text-foreground">Trend Analyzer</h1>
              <p className="mt-1 text-sm text-muted-foreground">Real-time trending topics from Twitter/X and Reddit</p>
            </div>
            <div className="flex flex-wrap items-center gap-3">
              <label className="flex items-center gap-2 text-sm">
                <input
                  type="checkbox"
                  checked={autoRefresh}
                  onChange={(e) => setAutoRefresh(e.target.checked)}
                  className="rounded"
                />
                <span className="text-foreground">Auto-refresh</span>
              </label>
              <Button onClick={refresh} disabled={isLoading} variant="default">
                {isLoading ? "Updating..." : "Refresh"}
              </Button>
            </div>
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        {error && (
          <Card className="mb-6 bg-destructive/10 border-destructive/30">
            <CardContent className="pt-6">
              <p className="text-sm text-destructive">Error loading trends. Using cached or mock data.</p>
            </CardContent>
          </Card>
        )}

        <PlatformSelector platform={platform} onPlatformChange={setPlatform} />

        <div className="mt-8">
          <PlatformStats trends={filteredTrends} />
        </div>

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          <TrendSearch onSearchChange={setSearchQuery} />
          <TrendFilter minVolume={minVolume} onMinVolumeChange={setMinVolume} />
        </div>

        <div className="mt-8 grid gap-8 lg:grid-cols-3">
          <div className="lg:col-span-2">
            <TrendingTopicsChart trends={filteredTrends} />
          </div>
          <div>
            <TrendsList trends={filteredTrends.slice(0, 15)} onTrendClick={setSelectedTrend} />
          </div>
        </div>

        {platform === "all" && (
          <div className="mt-8">
            <PlatformComparisonChart trends={filteredTrends} />
          </div>
        )}

        {isLoading && filteredTrends.length === 0 && (
          <div className="flex items-center justify-center py-12">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
          </div>
        )}
      </main>

      <TrendDetailsModal
        trend={selectedTrend}
        open={!!selectedTrend}
        onOpenChange={(open) => !open && setSelectedTrend(null)}
      />
    </div>
  )
}
