export interface TrendSnapshot {
  name: string
  volume: number
  timestamp: number
}

// Store last 10 snapshots per trend (in-memory, could be localStorage in production)
const trendHistory = new Map<string, TrendSnapshot[]>()

/**
 * Adds current trends to history and calculates growth rates
 */
export function updateTrendHistory(trends: any[]): any[] {
  const now = Date.now()

  return trends.map((trend) => {
    const trendName = trend.name || trend.title
    const currentVolume = trend.volume || trend.score || 0

    // Get or initialize history for this trend
    let history = trendHistory.get(trendName) || []

    // Add current snapshot
    history.push({
      name: trendName,
      volume: currentVolume,
      timestamp: now,
    })

    // Keep only last 10 snapshots (last ~10 minutes if refreshing every 60s)
    if (history.length > 10) {
      history = history.slice(-10)
    }

    trendHistory.set(trendName, history)

    // Calculate growth rate
    const growthRate = calculateGrowthRate(history)

    return {
      ...trend,
      growthRate,
      growthIndicator: getGrowthIndicator(growthRate),
    }
  })
}

/**
 * Calculates growth rate comparing latest to previous snapshot
 * Returns percentage change
 */
function calculateGrowthRate(history: TrendSnapshot[]): number {
  if (history.length < 2) return 0

  const current = history[history.length - 1]
  const previous = history[history.length - 2]

  if (previous.volume === 0) return current.volume > 0 ? 100 : 0

  const change = ((current.volume - previous.volume) / previous.volume) * 100
  return Math.round(change * 10) / 10 // Round to 1 decimal
}

/**
 * Returns growth indicator: "rising", "falling", or "stable"
 */
function getGrowthIndicator(growthRate: number): "rising" | "falling" | "stable" {
  if (growthRate > 5) return "rising"
  if (growthRate < -5) return "falling"
  return "stable"
}

/**
 * Clears all trend history (useful for testing or reset)
 */
export function clearTrendHistory(): void {
  trendHistory.clear()
}
