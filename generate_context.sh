#!/bin/bash

# Script mejorado para generar CONTEXT.md
# Uso: ./generate_context.sh

{
echo "# Contexto Automatizado - $(date)"

echo -e "\n## 🌐 Stack Tecnológico"
echo "- **Backend**: $(python -c "import django; print(django.get_version())" 2>/dev/null || echo "Django no encontrado") + PostgreSQL"
echo "- **Frontend**: $(node -v 2>/dev/null || echo "Node no encontrado") + $(npm list vite version 2>/dev/null | head -n 1 | awk '{print $NF}' || echo "Vite no encontrado")"

echo -e "\n## 📂 Estructura de Archivos"
echo '```tree'
tree -L 3 -I 'node_modules|venv|__pycache__|.git|dist|build' 2>/dev/null || echo "No se pudo generar la estructura"
echo '```'

echo -e "\n## ⚙️ Configuraciones Clave"
echo '```python'
echo "# Django - settings.py"
[ -f "backend/config/settings/base.py" ] && {
  grep -A 5 "AUTH_USER_MODEL" backend/config/settings/base.py 2>/dev/null || echo "# AUTH_USER_MODEL no configurado"
  grep -A 10 "DATABASES" backend/config/settings/base.py 2>/dev/null || echo "# DATABASES no configurado"
  grep -A 5 "CORS_" backend/config/settings/base.py 2>/dev/null || echo "# CORS no configurado"
} || echo "# Archivo settings.py no encontrado"
echo '```'

echo -e "\n## 🛠️ Estado Actual"
echo "### ✅ Funcionando"
git log -1 --pretty=%B 2>/dev/null | sed 's/^/- /' || echo "- No hay commits registrados"

echo -e "\n### 🚧 Pendientes"
git grep -l "TODO" 2>/dev/null | xargs -I {} sh -c 'echo "- {}: $(grep -m 1 TODO {} | tr -d "\n")"' 2>/dev/null || echo "- No hay TODOs registrados"

echo -e "\n## 🔍 Últimos Cambios"
echo '```bash'
git log -3 --oneline 2>/dev/null || echo "No hay historial de git"
echo '```'

echo -e "\n## 🚀 Comandos Clave"
echo '```bash'
echo "# Backend"
echo "python manage.py runserver"
echo ""
echo "# Frontend"
echo "cd frontend && npm run dev"
echo '```'
} > CONTEXT.md

echo "Archivo CONTEXT.md generado con éxito!"
