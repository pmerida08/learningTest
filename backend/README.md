# Instrucciones para desplegar en Render.com

1. Sube esta carpeta (`backend`) a un repositorio de GitHub.
2. Entra a `https://dashboard.render.com/` y crea un nuevo servicio de Web Service.
3. Conecta tu repositorio y selecciona la carpeta `backend` como raíz.
4. Render detectará el `Procfile` y el `requirements.txt` automáticamente.
5. Elige Python 3.10+ como entorno.
6. El comando de inicio será tomado del `Procfile`.
7. ¡Listo! Render instalará dependencias y levantará tu API.

Tu API estará disponible en una URL pública que Render te dará.
