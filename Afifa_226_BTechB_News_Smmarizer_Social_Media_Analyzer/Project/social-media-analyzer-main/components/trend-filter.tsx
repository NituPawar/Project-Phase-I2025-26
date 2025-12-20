"use client"

import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"

interface TrendFilterProps {
  minVolume: number
  onMinVolumeChange: (volume: number) => void
}

export function TrendFilter({ minVolume, onMinVolumeChange }: TrendFilterProps) {
  const volumeLevels = [0, 5000, 10000, 20000, 50000]

  return (
    <Card className="bg-card/50 backdrop-blur-sm">
      <CardContent className="pt-6">
        <div className="space-y-3">
          <p className="text-sm font-semibold text-foreground">Min Mentions</p>
          <div className="flex flex-wrap gap-2">
            {volumeLevels.map((level) => (
              <Button
                key={level}
                variant={minVolume === level ? "default" : "outline"}
                size="sm"
                onClick={() => onMinVolumeChange(level)}
              >
                {level === 0 ? "All" : `${(level / 1000).toFixed(0)}K+`}
              </Button>
            ))}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
