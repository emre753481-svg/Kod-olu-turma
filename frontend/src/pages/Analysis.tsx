import { useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { useAnalysisStore } from '../store/useAnalysisStore'

export default function Analysis() {
  const { id } = useParams()
  const poll = useAnalysisStore((s) => s.poll)
  const fetchResults = useAnalysisStore((s) => s.fetchResults)
  const status = useAnalysisStore((s) => s.status)
  const progress = useAnalysisStore((s) => s.progress)
  const message = useAnalysisStore((s) => s.message)
  const results = useAnalysisStore((s) => s.results)

  useEffect(() => {
    if (!id) return
    const t = setInterval(async () => {
      await poll(id)
    }, 1000)
    return () => clearInterval(t)
  }, [id, poll])

  useEffect(() => {
    if (!id) return
    if (status === 'completed') fetchResults(id)
  }, [id, status, fetchResults])

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-semibold">Analysis</h1>
      <div className="rounded border bg-white p-4">
        <div>Status: {status ?? '...'}</div>
        <div>Progress: {progress ?? 0}%</div>
        <div className="text-sm text-slate-600">{message}</div>
      </div>

      {results && (
        <pre className="rounded border bg-white p-4 overflow-auto text-xs">
{JSON.stringify(results, null, 2)}
        </pre>
      )}
    </div>
  )
}
