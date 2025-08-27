## Local Artisans MVP

Monorepo with FastAPI backend and React (Vite) frontend.

### Backend

- Path: `backend/`
- Run:
  - Create virtualenv
  - `pip install -r backend/requirements.txt`
  - Copy `backend/.env.example` to `.env` and adjust
  - `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

Endpoints:
- `GET /api/health`
- `POST /api/analyze-product` (multipart: `payload` JSON string, optional `image` file)

### Frontend

- Path: `frontend/`
- Run:
  - `npm install`
  - Copy `frontend/.env.example` to `.env`
  - `npm run dev`

Environment:
- Frontend uses `VITE_API_URL` (default `http://localhost:8000`)
- Backend uses `FRONTEND_URL` for CORS (default `http://localhost:5173`), `AI_PROVIDER=mock`


