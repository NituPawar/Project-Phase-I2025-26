"use client"

import { useEffect, useCallback } from "react"
import useSWR from "swr"
import { updateTrendHistory } from "@/lib/trend-history"

const fetcher = (url: string) => fetch(url).then((res) => res.json())

interface UseTrendsOptions {
  platform?: "twitter" | "reddit" | "all"
  refreshInterval?: number
}

export function useTrends({ platform = "all", refreshInterval = 60000 }: UseTrendsOptions = {}) {
  const { data, error, isLoading, mutate } = useSWR(`/api/trends?platform=${platform}`, fetcher, {
    revalidateOnFocus: false,
    revalidateOnReconnect: true,
    dedupingInterval: 60000,
    focusThrottleInterval: 300000,
    errorRetryCount: 3,
    errorRetryInterval: 5000,
  })

  // Auto-refresh on interval
  useEffect(() => {
    if (refreshInterval <= 0) return

    const interval = setInterval(() => {
      mutate()
    }, refreshInterval)

    return () => clearInterval(interval)
  }, [refreshInterval, mutate])

  const refresh = useCallback(() => {
    mutate()
  }, [mutate])

  const trendsWithGrowth = data ? updateTrendHistory(data) : []

  return {
    trends: trendsWithGrowth,
    isLoading,
    error,
    refresh,
    mutate,
  }
}
