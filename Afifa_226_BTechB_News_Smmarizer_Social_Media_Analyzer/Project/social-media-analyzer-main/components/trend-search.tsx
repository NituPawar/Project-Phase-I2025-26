"use client"

import { Input } from "@/components/ui/input"
import { Card, CardContent } from "@/components/ui/card"
import { useState, useCallback } from "react"

interface TrendSearchProps {
  onSearchChange: (query: string) => void
}

export function TrendSearch({ onSearchChange }: TrendSearchProps) {
  const [query, setQuery] = useState("")

  const handleChange = useCallback(
    (value: string) => {
      setQuery(value)
      onSearchChange(value)
    },
    [onSearchChange],
  )

  return (
    <Card className="bg-card/50 backdrop-blur-sm">
      <CardContent className="pt-6">
        <Input
          placeholder="Search trends..."
          value={query}
          onChange={(e) => handleChange(e.target.value)}
          className="bg-input/50"
        />
      </CardContent>
    </Card>
  )
}
