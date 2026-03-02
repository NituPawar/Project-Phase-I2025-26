"use client"

import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from "@/components/ui/dialog"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

interface TrendDetailsModalProps {
  trend: any | null
  open: boolean
  onOpenChange: (open: boolean) => void
}

export function TrendDetailsModal({ trend, open, onOpenChange }: TrendDetailsModalProps) {
  if (!trend) return null

  const platform = trend.platform?.toLowerCase() || "unknown"
  const platformColor =
    platform === "twitter"
      ? "bg-blue-500/20 text-blue-300"
      : platform === "reddit"
        ? "bg-orange-500/20 text-orange-300"
        : "bg-gray-500/20 text-gray-300"

  const handleOpen = (url: string) => {
    if (url) {
      window.open(url, "_blank", "noopener,noreferrer")
    } else if (platform === "twitter") {
      const searchUrl = `https://twitter.com/search?q=${encodeURIComponent(trend.name)}`
      window.open(searchUrl, "_blank", "noopener,noreferrer")
    } else if (platform === "reddit") {
      const subredditUrl = `https://reddit.com/${trend.name}`
      window.open(subredditUrl, "_blank", "noopener,noreferrer")
    }
  }

  return (
    <Dialog open={open} onOpenChange={onOpenChange}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            {trend.name || trend.title}
            <Badge className={platformColor}>{platform}</Badge>
          </DialogTitle>
          <DialogDescription>Trend details and engagement metrics</DialogDescription>
        </DialogHeader>

        <div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div>
              <p className="text-sm text-muted-foreground">Volume</p>
              <p className="text-2xl font-bold">{(trend.volume || trend.score || 0).toLocaleString()}</p>
            </div>
            {trend.subscribers && (
              <div>
                <p className="text-sm text-muted-foreground">Subscribers</p>
                <p className="text-2xl font-bold">{(trend.subscribers / 1000000).toFixed(1)}M</p>
              </div>
            )}
          </div>

          <div>
            <p className="text-sm text-muted-foreground mb-2">Full Name</p>
            <p className="text-sm bg-muted/50 rounded p-2 font-mono break-all">{trend.name || trend.title}</p>
          </div>

          <Button onClick={() => handleOpen(trend.url)} className="w-full">
            View on {platform === "twitter" ? "Twitter" : "Reddit"}
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  )
}
