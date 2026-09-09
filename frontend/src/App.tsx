import { useEffect, useState } from 'react'
import { Button } from '@/components/ui/button'

const API_BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000'

type Health = {
  status: string
}

export default function App() {
  const [health, setHealth] = useState<Health | null>(null)
  const [error, setError] = useState<string | null>(null)

  async function loadHealth() {
    setError(null)
    try {
      const response = await fetch(`${API_BASE}/health`)
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`)
      }
      setHealth((await response.json()) as Health)
    } catch (cause) {
      setHealth(null)
      setError(cause instanceof Error ? cause.message : 'request failed')
    }
  }

  useEffect(() => {
    void loadHealth()
  }, [])

  return (
    <main className="mx-auto max-w-lg p-8">
      <h1 className="text-2xl font-medium tracking-tight">Aegis</h1>
      <p className="mt-2 text-sm text-muted-foreground">
        Core UI talking to the API health endpoint.
      </p>
      <div className="mt-6 rounded-lg border p-4 text-sm">
        {error ? (
          <p className="text-destructive">API unreachable: {error}</p>
        ) : health ? (
          <p>API status: {health.status}</p>
        ) : (
          <p className="text-muted-foreground">Checking API…</p>
        )}
      </div>
      <Button className="mt-4" type="button" onClick={() => void loadHealth()}>
        Recheck
      </Button>
    </main>
  )
}
