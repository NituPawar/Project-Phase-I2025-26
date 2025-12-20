"use client"

import { Button } from "@/components/ui/button"
import { Card, CardContent } from "@/components/ui/card"

interface PlatformSelectorProps {
  platform: "twitter" | "reddit" | "all"
  onPlatformChange: (platform: "twitter" | "reddit" | "all") => void
}

export function PlatformSelector({ platform, onPlatformChange }: PlatformSelectorProps) {
  return (
    <Card className="bg-card/50 backdrop-blur-sm">
      <CardContent className="pt-6">
        <div className="flex flex-wrap gap-2">
          <Button variant={platform === "all" ? "default" : "outline"} onClick={() => onPlatformChange("all")}>
            All Platforms
          </Button>
          <Button variant={platform === "twitter" ? "default" : "outline"} onClick={() => onPlatformChange("twitter")}>
            Twitter/X
          </Button>
          <Button variant={platform === "reddit" ? "default" : "outline"} onClick={() => onPlatformChange("reddit")}>
            Reddit
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}
