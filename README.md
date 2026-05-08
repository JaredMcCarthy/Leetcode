# Leetcode
Soluciones a problemas de **LeetCode** en **Python**, con un sitio en **MkDocs Material** para navegar por problema, dificultad y tags.

## Sitio
- Puedes ver el sitio aquí: **https://jaredmccarthy.github.io/Leetcode/**

## Qué contiene este repo
- **Soluciones en Python** organizadas por número y nombre del problema.
- **Documentación** en `docs/` (MkDocs).
- Una sección **Problemas** que se genera automáticamente con:
  - Dificultad (**Easy / Medium / Hard**)
  - Tags (Array, Hash Table, etc.)
  - Código de la solución
  - Navegación **Anterior / Siguiente**

## Cómo actualizar / agregar nuevos problemas
1. Agrega una carpeta nueva con el formato:
   - `Soluciones/Soluciones/<numero>. <Nombre del problema>/`
   - Dentro debe haber un solo archivo `.py` (por ejemplo `Leetcode_<numero>.py`)

2. En la raíz del repo (donde está `mkdocs.yml`), corre:
```bash
python3 scripts/generate_problems_md.py --solutions-dir "Soluciones/Soluciones"
```
3. Sube cambios a GitHub:
```
git add .
git commit -m "agregar problema <numero>"
git push
```
## Contribuciones
Este es un proyecto personal, si quieres usarlo, siéntete libre de hacer fork y adaptarlo a tu gusto.
