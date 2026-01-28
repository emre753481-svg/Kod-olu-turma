import { create } from 'zustand'
import { api } from '../services/api'

type Status = 'queued' | 'running' | 'completed' | 'failed'

interface State {
  analysisId?: string
  status?: Status
  progress?: number
  message?: string
  results?: any
  start: (repoUrl: string, githubToken: string) => Promise<string>
  poll: (id: string) => Promise<void>
  fetchResults: (id: string) => Promise<void>
}

export const useAnalysisStore = create<State>((set) => ({
  async start(repoUrl, githubToken) {
    const res = await api.post('/api/analyze', { repo_url: repoUrl, github_token: githubToken })
    const id = res.data.analysis_id as string
    set({ analysisId: id })
    return id
  },
  async poll(id) {
    const res = await api.get(`/api/analysis/${id}/status`)
    set({ status: res.data.status, progress: res.data.progress, message: res.data.message })
  },
  async fetchResults(id) {
    const res = await api.get(`/api/analysis/${id}/results`)
    set({ results: res.data.results })
  },
}))
