# VAM - Vector Asset Management Setup Guide

## Prerequisites

- Docker and Docker Compose installed
- Git
- Port 80 and 8000 available on your system

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/saurabhtim2198-cyber/vam.git
cd vam
```

### 2. Start the Application

```bash
docker-compose up --build
```

This command will:
- Build the backend Docker image
- Build the frontend Docker image
- Start both services
- Create the Docker network

### 3. Access the Application

- **Frontend**: http://localhost
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (Swagger UI)

## Project Structure

```
vam/
├── backend/
│   ├── Dockerfile
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── .dockerignore
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf           # Nginx configuration
│   ├── package.json         # Node dependencies
│   ├── vite.config.js       # Vite build configuration
│   ├── index.html           # HTML entry point
│   ├── src/
│   │   ├── main.js          # Vue app entry
│   │   └── App.vue          # Root Vue component
│   └── .dockerignore
├── docker-compose.yml       # Docker Compose configuration
├── .env.example             # Environment variables template
├── README.md                # Project documentation
└── SETUP.md                 # This file
```

## Backend

**Framework**: FastAPI (Python)

**Features**:
- RESTful API
- CORS enabled
- Health checks
- Automatic API documentation (Swagger UI)

**Endpoints**:
- `GET /` - Health check
- `GET /api/v1/health` - API health status
- `GET /api/v1/assets` - List all assets
- `POST /api/v1/assets` - Create a new asset
- `GET /api/v1/assets/{asset_id}` - Get asset details

## Frontend

**Framework**: Vue.js 3 with Vite

**Features**:
- Modern SPA (Single Page Application)
- Real-time backend communication
- Responsive design
- Asset management interface

## Docker Services

### Backend Service
- **Container Name**: goc_backend
- **Port**: 8000
- **Health Check**: Every 10 seconds
- **Restart Policy**: Always

### Frontend Service
- **Container Name**: goc_frontend
- **Port**: 80
- **Depends On**: Backend service (healthy)
- **Restart Policy**: Always

## Development

### Running Locally (Without Docker)

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Useful Commands

```bash
# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop services
docker-compose down

# Remove volumes
docker-compose down -v

# Rebuild services
docker-compose up --build

# Access backend shell
docker-compose exec backend bash

# Access frontend shell
docker-compose exec frontend sh
```

## Environment Variables

Copy `.env.example` to `.env` and configure as needed:

```bash
cp .env.example .env
```

## Troubleshooting

### Backend not responding
- Check if port 8000 is already in use
- View backend logs: `docker-compose logs backend`
- Ensure health check is passing

### Frontend not loading
- Check if port 80 is already in use
- View frontend logs: `docker-compose logs frontend`
- Clear browser cache and refresh

### Containers not starting
- Ensure Docker daemon is running
- Check available disk space
- Review docker-compose logs: `docker-compose logs`

## API Documentation

Once the backend is running, view interactive API documentation at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Contributing

1. Create a feature branch
2. Make your changes
3. Test locally
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues and questions, please open an issue on GitHub.
