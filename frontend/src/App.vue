<template>
  <div class="container">
    <header class="header">
      <h1>🎨 Vector Asset Management</h1>
      <p>Manage your digital assets with ease</p>
    </header>

    <main class="main-content">
      <div class="status-card" :class="{ healthy: isHealthy, unhealthy: !isHealthy }">
        <h2>Backend Status</h2>
        <p class="status-indicator" :class="{ online: isHealthy, offline: !isHealthy }">
          {{ isHealthy ? '🟢 Online' : '🔴 Offline' }}
        </p>
        <p v-if="statusMessage" class="status-message">{{ statusMessage }}</p>
        <button @click="checkHealth" class="btn btn-primary">Check Status</button>
      </div>

      <div class="assets-card">
        <h2>Assets</h2>
        <div class="assets-list">
          <p v-if="assets.length === 0" class="empty-state">No assets yet. Create one to get started!</p>
          <div v-for="asset in assets" :key="asset.id" class="asset-item">
            <h3>{{ asset.name }}</h3>
            <p>{{ asset.description }}</p>
          </div>
        </div>
        <div class="asset-form">
          <input v-model="newAsset.name" placeholder="Asset name" class="input" />
          <input v-model="newAsset.description" placeholder="Description" class="input" />
          <button @click="createAsset" class="btn btn-success">Create Asset</button>
        </div>
      </div>
    </main>

    <footer class="footer">
      <p>VAM v0.1.0 © 2026 - Running on Docker</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data() {
    return {
      isHealthy: false,
      statusMessage: '',
      assets: [],
      newAsset: {
        name: '',
        description: ''
      }
    }
  },
  mounted() {
    this.checkHealth()
    this.loadAssets()
  },
  methods: {
    async checkHealth() {
      try {
        const response = await axios.get('/api/v1/health')
        this.isHealthy = response.status === 200
        this.statusMessage = `Backend is running - Version: ${response.data.version}`
      } catch (error) {
        this.isHealthy = false
        this.statusMessage = 'Backend is not responding'
      }
    },
    async loadAssets() {
      try {
        const response = await axios.get('/api/v1/assets')
        this.assets = response.data.assets
      } catch (error) {
        console.error('Failed to load assets:', error)
      }
    },
    async createAsset() {
      if (!this.newAsset.name) {
        alert('Please enter an asset name')
        return
      }
      try {
        const response = await axios.post('/api/v1/assets', null, {
          params: {
            name: this.newAsset.name,
            description: this.newAsset.description
          }
        })
        this.assets.push(response.data)
        this.newAsset = { name: '', description: '' }
      } catch (error) {
        console.error('Failed to create asset:', error)
      }
    }
  }
}
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.header {
  text-align: center;
  color: white;
  margin-bottom: 40px;
  padding: 30px 0;
}

.header h1 {
  font-size: 3em;
  margin-bottom: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
}

.header p {
  font-size: 1.2em;
  opacity: 0.9;
}

.main-content {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 30px;
  margin-bottom: 40px;
}

.status-card,
.assets-card {
  background: white;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.status-card:hover,
.assets-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
}

.status-card h2,
.assets-card h2 {
  color: #333;
  margin-bottom: 20px;
  font-size: 1.5em;
}

.status-indicator {
  font-size: 1.5em;
  margin: 20px 0;
  font-weight: bold;
}

.status-indicator.online {
  color: #27ae60;
}

.status-indicator.offline {
  color: #e74c3c;
}

.status-message {
  color: #666;
  margin-bottom: 20px;
  font-size: 0.95em;
}

.assets-list {
  margin-bottom: 20px;
  max-height: 300px;
  overflow-y: auto;
}

.asset-item {
  padding: 15px;
  background: #f8f9fa;
  border-radius: 8px;
  margin-bottom: 10px;
  border-left: 4px solid #667eea;
}

.asset-item h3 {
  color: #333;
  margin-bottom: 5px;
}

.asset-item p {
  color: #666;
  font-size: 0.9em;
}

.empty-state {
  text-align: center;
  color: #999;
  padding: 40px 20px;
  font-style: italic;
}

.asset-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.input {
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 1em;
  transition: border-color 0.3s ease;
}

.input:focus {
  outline: none;
  border-color: #667eea;
}

.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 1em;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: #667eea;
  color: white;
}

.btn-primary:hover {
  background: #5568d3;
  transform: scale(1.05);
}

.btn-success {
  background: #27ae60;
  color: white;
}

.btn-success:hover {
  background: #229954;
  transform: scale(1.05);
}

.footer {
  text-align: center;
  color: white;
  padding: 20px;
  font-size: 0.9em;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .header h1 {
    font-size: 2em;
  }

  .main-content {
    grid-template-columns: 1fr;
  }
}
</style>
