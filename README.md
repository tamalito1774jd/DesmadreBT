# DesmadreBOT 🤖

Un bot de Discord completo y moderno con múltiples funcionalidades.

## ✨ Características Principales

- 💰 **Sistema de Economía** - Dinero, trabajos, transacciones
- 📈 **Sistema de Niveles** - XP y rankeo de usuarios  
- 🔨 **Moderación Avanzada** - Kick, ban, warn, mute, purge
- 🎵 **Reproductor de Música** - Música de YouTube en voz
- 🚔 **Anti-Spam** - Protección automática
- 🎭 **Auto-Roles** - Asignación automática de roles
- 🌐 **Dashboard Web** - Panel de control en tiempo real
- ⚡ **Slash Commands** - Comandos modernos de Discord

## 📦 Requisitos

- Python 3.10+
- discord.py 2.3.2
- Flask 3.0.0
- yt-dlp 2023.12.30

## 🚀 Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/tamalito1774jd/DesmadreBT.git
   cd DesmadreBT
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configura las variables de entorno**
   - Copia `.env.example` a `.env`
   - Agrega tu token de Discord
   - Configura otras opciones si es necesario

4. **Ejecuta el bot**
   ```bash
   python bot/main.py
   ```

5. **Inicia el Dashboard (opcional)**
   ```bash
   python web/app.py
   ```

## 🎮 Comandos

### Economía
- `!dinero` - Ver dinero
- `!trabajo` - Trabajar y ganar dinero
- `!enviar @usuario cantidad` - Enviar dinero
- `!robar @usuario` - Intentar robar dinero
- `!top_dinero` - Top 10 usuarios por dinero

### Niveles
- `!nivel` - Ver tu nivel
- `!top_niveles` - Top 10 usuarios por nivel

### Moderación
- `!kick @usuario razón` - Expulsar usuario
- `!ban @usuario razón` - Banear usuario
- `!warn @usuario razón` - Advertir usuario
- `!mute @usuario segundos` - Silenciar usuario
- `!unmute @usuario` - Dessilenciar usuario
- `!purge cantidad` - Limpiar mensajes
- `!warnings @usuario` - Ver advertencias

### Música
- `!conectar` - Conectar a canal de voz
- `!desconectar` - Desconectar
- `!tocar canción` - Reproducir canción
- `!parar` - Detener música
- `!reanudar` - Reanudar música

### Auto-Roles
- `!agregarautorrol @rol` - Agregar auto-rol
- `!quitarautorrol @rol` - Quitar auto-rol
- `!listarautorroles` - Ver auto-roles

## 🌐 Dashboard Web

Accede a `http://localhost:5000` para ver el dashboard con estadísticas en tiempo real.

## 📁 Estructura del Proyecto

```
DesmadreBT/
├── bot/
│   ├── config.py           # Configuración
│   ├── main.py             # Archivo principal
│   ├── cogs/
│   │   ├── economia.py
│   │   ├── niveles.py
│   │   ├── moderacion.py
│   │   ├── musica.py
│   │   ├── antispam.py
│   │   └── autoroles.py
│   └── utils/
│       ├── database.py
│       └── embeds.py
├── web/
│   ├── app.py              # API Flask
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── css/style.css
│       └── js/script.js
├── .env                    # Variables de entorno
├── requirements.txt        # Dependencias
└── README.md
```

## ⚙️ Configuración

Edita el archivo `.env`:

```env
DISCORD_TOKEN=tu_token
PREFIX=!
ACTIVITY_STATUS=💰 Economía | 📈 Niveles
DASHBOARD_PORT=5000
```

## 📝 Licencia

Este proyecto está bajo la licencia MIT.

## 👨‍💻 Autor

Hecho por **Tamalito** con ❤️

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request.

---

**¿Necesitas ayuda?** Contacta al desarrollador o abre un issue en GitHub.
