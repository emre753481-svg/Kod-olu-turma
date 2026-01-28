# GitAnalyzer Pro - Bootstrap Repo (Generator)

Bu repo ilk aşamada sadece generator içerir. GitHub Actions çalışınca `gitanalyzer-pro/` fullstack projesini otomatik üretir ve bu repoya commit/push eder.

## Çalıştırma
1) Repo Settings → Actions → Workflow permissions: Read and write (önerilir)
2) Actions sekmesi → "Generate Full Project" workflow → Run workflow
3) Workflow bitince repo içinde `backend/`, `frontend/`, `docker-compose.yml` vb. oluşur.
4) Railway: Deploy from GitHub repo ile deploy et (backend ve frontend için ayrı servis önerilir).
