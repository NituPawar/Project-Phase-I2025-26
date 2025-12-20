import { Card, CardContent } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

interface PlatformStatsProps {
  trends: any[]
}

export function PlatformStats({ trends }: PlatformStatsProps) {
  const twitterCount = trends.filter((t) => t.platform === "twitter").length
  const redditCount = trends.filter((t) => t.platform === "reddit").length
  const totalVolume = trends.reduce((sum, t) => sum + (t.volume || t.score || 0), 0)

  const twitterVolume = trends.filter((t) => t.platform === "twitter").reduce((sum, t) => sum + (t.volume || 0), 0)

  const redditVolume = trends.filter((t) => t.platform === "reddit").reduce((sum, t) => sum + (t.score || 0), 0)

  return (
    <div className="grid gap-4 md:grid-cols-3">
      <Card className="bg-card/50 backdrop-blur-sm">
        <CardContent className="pt-6">
          <div className="space-y-2">
            <p className="text-sm text-muted-foreground">Total Trends</p>
            <p className="text-3xl font-bold">{trends.length}</p>
            <p className="text-xs text-muted-foreground">Across all platforms</p>
          </div>
        </CardContent>
      </Card>

      <Card className="bg-card/50 backdrop-blur-sm">
        <CardContent className="pt-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <p className="text-sm text-muted-foreground">Twitter/X</p>
              <Badge className="bg-blue-500/20 text-blue-300">{twitterCount}</Badge>
            </div>
            <p className="text-2xl font-bold">{twitterVolume.toLocaleString()}</p>
            <p className="text-xs text-muted-foreground">Total mentions</p>
          </div>
        </CardContent>
      </Card>

      <Card className="bg-card/50 backdrop-blur-sm">
        <CardContent className="pt-6">
          <div className="space-y-2">
            <div className="flex items-center gap-2">
              <p className="text-sm text-muted-foreground">Reddit</p>
              <Badge className="bg-orange-500/20 text-orange-300">{redditCount}</Badge>
            </div>
            <p className="text-2xl font-bold">{redditVolume.toLocaleString()}</p>
            <p className="text-xs text-muted-foreground">Total engagement</p>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
