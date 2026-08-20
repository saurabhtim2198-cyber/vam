# VAM - Vector Asset Management

🎨 A full-stack containerized application for managing digital assets with a modern Python backend and Vue.js frontend.

## Features

✨ **Full-Stack Application**
- Python FastAPI backend with REST API
- Vue.js 3 frontend with modern UI
- Docker & Docker Compose for containerization
- Health checks and service dependencies
- CORS enabled for cross-origin requests
- Nginx reverse proxy for static files

🚀 **Developer Experience**
- Auto-reload during development
- API documentation with Swagger UI
- Component-based frontend architecture
- Production-ready Docker setup

🛡️ **Reliability**
- Health checks on backend service
- Automatic service restart
- Proper logging and error handling
- Service dependency management

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/saurabhtim2198-cyber/vam.git
cd vam

# Start services
docker-compose up --build
```

### Access Application

- **Frontend**: http://localhost
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## Technology Stack

### Backend
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Language**: Python 3.11
- **Dependencies**: See `backend/requirements.txt`

### Frontend
- **Framework**: Vue.js 3
- **Build Tool**: Vite
- **HTTP Client**: Axios
- **Runtime**: Node.js 18
- **Server**: Nginx

### Infrastructure
- **Containerization**: Docker
- **Orchestration**: Docker Compose
- **Networking**: Custom Docker network (`goc_network`)

## Project Structure

```
vam/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── .dockerignore
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   ├── src/
│   │   ├── main.js
│   │   └── App.vue
│   └── .dockerignore
├── docker-compose.yml
├── .env.example
├── README.md
├── SETUP.md
└── LICENSE
```

## API Endpoints

### Health & Status
- `GET /` - Basic health check
- `GET /api/v1/health` - Detailed health status

### Assets Management
- `GET /api/v1/assets` - List all assets
- `POST /api/v1/assets` - Create new asset
- `GET /api/v1/assets/{asset_id}` - Get asset details

## Development Guide

See [SETUP.md](./SETUP.md) for detailed development instructions including:
- Local development without Docker
- Useful Docker commands
- Troubleshooting guide
- Environment configuration

## Docker Services

| Service | Port | Health Check | Dependencies |
|---------|------|--------------|---------------|
| Backend | 8000 | Every 10s | None |
| Frontend | 80 | N/A | Backend (healthy) |

## Environment Variables

Copy and customize `.env.example`:

```bash
cp .env.example .env
```

See `.env.example` for available configuration options.

## Common Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Rebuild and start
docker-compose up --build

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f backend

# Execute command in container
docker-compose exec backend bash
```

## API Documentation

Interactive API documentation is available at:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Troubleshooting

**Backend not responding?**
- Check port 8000 availability
- View logs: `docker-compose logs backend`
- Verify health check passing

**Frontend not loading?**
- Check port 80 availability
- Clear browser cache
- View logs: `docker-compose logs frontend`

**Services won't start?**
- Ensure Docker daemon is running
- Check disk space
- Review: `docker-compose logs`

## Performance Tips

- Frontend assets are cached by Nginx
- Backend uses async/await for concurrency
- Health checks use minimal resources
- Services auto-restart on failure

## Security Considerations

- CORS is enabled for all origins (configure in production)
- No authentication implemented (add as needed)
- Health check endpoint is public
- Consider adding API rate limiting

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## License

MIT License - See [LICENSE](./LICENSE) file for details

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- See [SETUP.md](./SETUP.md) for troubleshooting

## Author

**saurabhtim2198-cyber**
- GitHub: [@saurabhtim2198-cyber](https://github.com/saurabhtim2198-cyber)

---

**Made with ❤️ using FastAPI + Vue.js + Docker**
