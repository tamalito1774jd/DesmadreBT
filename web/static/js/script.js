// API Base URL
const API_BASE = "http://localhost:5000/api";

// Cargar estadísticas
async function loadStats() {
    try {
        const response = await fetch(`${API_BASE}/stats`);
        const data = await response.json();
        
        if (data.success) {
            document.getElementById("total-usuarios").textContent = data.total_usuarios;
            document.getElementById("dinero-total").textContent = `$${data.dinero_total.toLocaleString()}`;
            document.getElementById("nivel-promedio").textContent = data.nivel_promedio;
        }
    } catch (error) {
        console.error("Error cargando estadísticas:", error);
    }
}

// Cargar top dinero
async function loadTopDinero() {
    try {
        const response = await fetch(`${API_BASE}/top_dinero`);
        const data = await response.json();
        
        const container = document.getElementById("top-dinero");
        container.innerHTML = "";
        
        if (data.success && data.data.length > 0) {
            data.data.forEach((item, index) => {
                const div = document.createElement("div");
                div.className = "top-item";
                div.innerHTML = `
                    <div class="top-rank">#${index + 1}</div>
                    <div class="top-info">
                        <div class="top-user">Usuario #${item.user_id}</div>
                        <div class="top-value">💰 $${item.dinero.toLocaleString()}</div>
                    </div>
                `;
                container.appendChild(div);
            });
        } else {
            container.innerHTML = "<p>Sin datos disponibles</p>";
        }
    } catch (error) {
        console.error("Error cargando top dinero:", error);
    }
}

// Cargar top niveles
async function loadTopNiveles() {
    try {
        const response = await fetch(`${API_BASE}/top_niveles`);
        const data = await response.json();
        
        const container = document.getElementById("top-niveles");
        container.innerHTML = "";
        
        if (data.success && data.data.length > 0) {
            data.data.forEach((item, index) => {
                const div = document.createElement("div");
                div.className = "top-item";
                div.innerHTML = `
                    <div class="top-rank">#${index + 1}</div>
                    <div class="top-info">
                        <div class="top-user">Usuario #${item.user_id}</div>
                        <div class="top-value">📈 Nivel ${item.nivel} (${item.xp} XP)</div>
                    </div>
                `;
                container.appendChild(div);
            });
        } else {
            container.innerHTML = "<p>Sin datos disponibles</p>";
        }
    } catch (error) {
        console.error("Error cargando top niveles:", error);
    }
}

// Inicializar dashboard
document.addEventListener("DOMContentLoaded", () => {
    loadStats();
    loadTopDinero();
    loadTopNiveles();
    
    // Recargar datos cada 30 segundos
    setInterval(() => {
        loadStats();
        loadTopDinero();
        loadTopNiveles();
    }, 30000);
});
