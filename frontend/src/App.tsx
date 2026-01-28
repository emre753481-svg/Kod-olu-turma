import { Routes, Route, Link } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Analysis from './pages/Analysis'

export default function App() {
  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <header className="border-b bg-white">
        <div className="mx-auto flex max-w-5xl items-center justify-between p-4">
          <Link to="/" className="font-semibold">GitAnalyzer Pro</Link>
          <nav className="flex gap-4 text-sm">
            <Link to="/">Dashboard</Link>
          </nav>
        </div>
      </header>
      <main className="mx-auto max-w-5xl p-4">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/analysis/:id" element={<Analysis />} />
        </Routes>
      </main>
    </div>
  )
}
