# GitAnalyzer Pro

Enterprise-level GitHub repository analyzer that generates documentation with AI (OpenAI/Anthropic) and exports results as PDF/Markdown/JSON.

## Local (Docker)
1) Copy envs:
- `cp backend/.env.example backend/.env`
- `cp frontend/.env.example frontend/.env`

2) Start:
- `docker compose up --build`

Backend: http://localhost:8000/docs  
Frontend: http://localhost:5173

## Railway
- Create 2 services from the same GitHub repo:
  - Backend: root directory `backend`
  - Frontend: root directory `frontend`
- Set backend variables: `GITHUB_TOKEN`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `PLANTUML_BASE_URL`
- Set frontend variable: `VITE_API_BASE_URL` (backend public URL)
