import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAnalysisStore } from '../store/useAnalysisStore'

export default function Dashboard() {
  const nav = useNavigate()
  const start = useAnalysisStore((s) => s.start)

  const [repoUrl, setRepoUrl] = useState('')
  const [token, setToken] = useState('')

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-semibold">New analysis</h1>
      <div className="rounded-lg border bg-white p-4 space-y-3">
        <label className="block text-sm">
          Repo URL
          <input className="mt-1 w-full rounded border p-2" value={repoUrl} onChange={(e) => setRepoUrl(e.target.value)} placeholder="https://github.com/owner/repo" />
        </label>
        <label className="block text-sm">
          GitHub Token
          <input className="mt-1 w-full rounded border p-2" value={token} onChange={(e) => setToken(e.target.value)} placeholder="ghp_..." />
        </label>
        <button
          className="rounded bg-slate-900 px-4 py-2 text-white"
          onClick={async () => {
            const id = await start(repoUrl, token)
            nav(`/analysis/${id}`)
          }}
        >
          Start
        </button>
      </div>
    </div>
  )
}
