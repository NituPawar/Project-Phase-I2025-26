"use client"

import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { TrendItem } from "@/components/trend-item"
import { ScrollArea } from "@/components/ui/scroll-area"

interface TrendsListProps {
  trends: any[]
  onTrendClick?: (trend: any) => void
}

export function TrendsList({ trends, onTrendClick }: TrendsListProps) {
  return (
    <Card className="bg-card/50 backdrop-blur-sm">
      <CardHeader>
        <CardTitle>Top Trends</CardTitle>
        <CardDescription>Most discussed right now</CardDescription>
      </CardHeader>
      <CardContent>
        <ScrollArea className="h-[480px]">
          <div className="space-y-2 pr-4">
            {trends.length > 0 ? (
              trends.map((trend, index) => (
                <div key={`${trend.name}-${index}`} onClick={() => onTrendClick?.(trend)} className="cursor-pointer">
                  <TrendItem trend={trend} rank={index + 1} />
                </div>
              ))
            ) : (
              <p className="text-sm text-muted-foreground py-8 text-center">No trends available</p>
            )}
          </div>
        </ScrollArea>
      </CardContent>
    </Card>
  )
}
