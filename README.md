# Toku10 - Full-Stack Monorepo

A modern full-stack application with Vue.js frontend and Python FastAPI backend.

## Project Structure

```
toku10/
├── frontend/              # Vue.js frontend application
│   ├── src/              # Source code
│   ├── public/           # Static assets
│   ├── package.json      # Frontend dependencies
│   └── vite.config.ts    # Vite configuration
├── backend/              # Python FastAPI backend
│   ├── app/              # Application code
│   │   ├── api/          # API routes
│   │   ├── models/       # Database models
│   │   └── services/     # Business logic
│   ├── requirements.txt  # Python dependencies
│   └── .env.example     # Environment variables template
├── shared/               # Shared types and utilities
│   └── types/           # TypeScript types for API contracts
└── package.json         # Root workspace configuration
```

## Quick Start

### Prerequisites

- Node.js (v18+)
- Python (v3.8+)
- npm or yarn

### Installation

1. **Install root dependencies:**

   ```bash
   npm install
   ```

2. **Install all project dependencies:**
   ```bash
   npm run install:all
   ```

### Development

**Start both frontend and backend:**

```bash
npm run dev
```

**Start individually:**

```bash
# Frontend only (http://localhost:5173)
npm run dev:frontend

# Backend only (http://localhost:8000)
npm run dev:backend
```

## Available Scripts

- `npm run dev` - Start both frontend and backend
- `npm run dev:frontend` - Start only frontend
- `npm run dev:backend` - Start only backend
- `npm run build:frontend` - Build frontend for production
- `npm run install:all` - Install all dependencies
- `npm run lint:frontend` - Lint frontend code
- `npm run test:frontend` - Run frontend tests

## API Documentation

When the backend is running, visit:

- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## Technology Stack

### Frontend

- Vue.js 3 with TypeScript
- Vite for build tooling
- Tailwind CSS for styling
- Pinia for state management
- Vue Router for routing

### Backend

- FastAPI (Python web framework)
- Pydantic for data validation
- Uvicorn ASGI server
- CORS enabled for frontend integration

## Development Workflow

1. **Frontend development**: Work in `frontend/` directory
2. **Backend development**: Work in `backend/` directory
3. **Shared types**: Define API contracts in `shared/types/`
4. **Environment variables**: Copy `backend/env.example` to `backend/.env`

## Deployment

Each part can be deployed independently:

- **Frontend**: Build and deploy to any static hosting (Vercel, Netlify, etc.)
- **Backend**: Deploy to any Python hosting (Railway, Heroku, AWS, etc.)

## Contributing

1. Create feature branches from `main`
2. Make changes in the appropriate directory (`frontend/` or `backend/`)
3. Test your changes with `npm run dev`
4. Submit a pull request
