# Atlas de vegas de la Puna argentina

Sitio estático (GitHub Pages) con fotos de campo de vegas altoandinas y un chat bibliográfico.
Todo cambio de datos sigue el procedimiento de PROCESO.md:

@PROCESO.md

## Reglas para el asistente

- Después de tocar `data/`, `fotos/`, `miniaturas/` o el README, correr
  `python herramientas/actualizar_readme.py` y `python herramientas/validar_datos.py`.
  No dar un cambio por terminado si el validador tiene errores.
- Si aparece un nombre de vega dudoso (posible duplicado o sin punto de muestreo cercano),
  preguntar antes de inventar uno nuevo.
- Para la bibliografía, seguir `wiki/CLAUDE.md`: las fichas y las síntesis se escriben leyendo
  los textos, nunca con llamadas a APIs.
- Textos, commits y documentación en español.
