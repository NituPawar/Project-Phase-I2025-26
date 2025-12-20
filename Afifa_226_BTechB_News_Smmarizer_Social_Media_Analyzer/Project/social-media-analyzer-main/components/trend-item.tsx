import { Badge } from "@/components/ui/badge"
import { TrendingUp, TrendingDown, Minus } from "lucide-react"

interface TrendItemProps {
  trend: any
  rank: number
}

export function TrendItem({ trend, rank }: TrendItemProps) {
  const platform = trend.platform?.toLowerCase() || "unknown"
  const platformColor =
    platform === "twitter"
      ? "bg-blue-500/20 text-blue-300"
      : platform === "reddit"
        ? "bg-orange-500/20 text-orange-300"
        : "bg-gray-500/20 text-gray-300"

  const volume = trend.volume || trend.score || 0
  const isLarge = volume > 20000

  const growthRate = trend.growthRate || 0
  const growthIndicator = trend.growthIndicator || "stable"

  return (
    <div
      className={`flex items-start gap-3 rounded-lg border transition-all hover:bg-muted/50 p-3 ${isLarge ? "border-primary/50 bg-primary/5" : "border-border/50"}`}
    >
      <div className="min-w-fit">
        <span className={`text-xs font-bold ${isLarge ? "text-primary" : "text-muted-foreground"}`}>#{rank}</span>
      </div>
      <div className="flex-1 min-w-0">
        <div className="flex items-center gap-2">
          <p className="font-semibold text-foreground truncate text-sm">{trend.name || trend.title}</p>
          {growthIndicator === "rising" && (
            <div className="flex items-center gap-1 text-green-500 text-xs font-medium">
              <TrendingUp className="w-3 h-3" />
              <span>+{growthRate}%</span>
            </div>
          )}
          {growthIndicator === "falling" && (
            <div className="flex items-center gap-1 text-red-500 text-xs font-medium">
              <TrendingDown className="w-3 h-3" />
              <span>{growthRate}%</span>
            </div>
          )}
          {growthIndicator === "stable" && growthRate !== 0 && (
            <div className="flex items-center gap-1 text-yellow-500 text-xs font-medium">
              <Minus className="w-3 h-3" />
              <span>{growthRate}%</span>
            </div>
          )}
        </div>
        <p className="text-xs text-muted-foreground mt-1">
          {volume.toLocaleString()} {platform === "twitter" ? "mentions" : "engagement"}
        </p>
      </div>
      <Badge className={platformColor}>{platform}</Badge>
    </div>
  )
}
