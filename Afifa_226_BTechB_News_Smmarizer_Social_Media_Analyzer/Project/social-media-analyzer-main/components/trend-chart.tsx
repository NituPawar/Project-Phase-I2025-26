import { LineChart, Line, ResponsiveContainer } from "recharts"

interface TrendChartProps {
  trend: any
}

export function TrendChart({ trend }: TrendChartProps) {
  // Mock sparkline data - in production, this would be historical data
  const data = [
    { value: Math.random() * trend.volume * 0.7 },
    { value: Math.random() * trend.volume * 0.8 },
    { value: Math.random() * trend.volume * 0.9 },
    { value: trend.volume * 0.85 },
    { value: trend.volume },
  ]

  return (
    <ResponsiveContainer width="100%" height={40}>
      <LineChart data={data}>
        <Line type="monotone" dataKey="value" stroke="#3b82f6" dot={false} strokeWidth={2} />
      </LineChart>
    </ResponsiveContainer>
  )
}
