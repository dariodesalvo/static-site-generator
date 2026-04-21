# Static Site Generator

Un generador de sitios estaticos escrito en Python que convierte archivos Markdown a HTML.

## Caracteristicas

- Convierte Markdown a HTML
- Soporta sintaxis comun de Markdown:
  - Encabezados (`#`, `##`, etc.)
  - Texto en **negrita** y *cursiva*
  - Listas ordenadas y desordenadas
  - Bloques de codigo
  - Citas (blockquotes)
  - Links e imagenes
- Sistema de plantillas HTML
- Generacion recursiva de paginas
- Soporte para basepath configurable (ideal para GitHub Pages)
- Copia automatica de archivos estaticos (CSS, imagenes)

## Estructura del proyecto

```
├── src/                    # Codigo principal
│   ├── main.py            # Punto de entrada
│   ├── htmlnode.py        # Clases para nodos HTML
│   └── textnode.py        # Nodos de texto y conversion
├── helpers/               # Funciones auxiliares
│   ├── helper.py          # Procesamiento de markdown
│   └── markdown_html.py   # Conversion MD a HTML
├── content/               # Archivos markdown fuente
├── static/                # Archivos estaticos (CSS, imagenes)
├── docs/                  # Salida HTML generada
├── template.html          # Plantilla HTML base
├── build.sh              # Script para build de produccion
└── main.sh               # Script para desarrollo local
```

## Uso

### Desarrollo local

```bash
./main.sh
```

Esto genera el sitio y levanta un servidor en `http://localhost:8888`.

### Build para produccion (GitHub Pages)

```bash
./build.sh
```

Genera el sitio en `docs/` con las rutas configuradas para GitHub Pages.

### Tests

```bash
./test.sh
```

## Como funciona

1. Lee archivos `.md` del directorio `content/`
2. Parsea el Markdown y lo convierte a nodos HTML
3. Aplica la plantilla de `template.html`
4. Ajusta las rutas segun el basepath configurado
5. Genera los archivos HTML en `docs/`

## Configuracion de basepath

Para desplegar en GitHub Pages, edita `build.sh` y ajusta el basepath:

```bash
python3 src/main.py "/tu-repositorio/"
```

---

Este proyecto fue desarrollado como parte del curso [Build a Static Site Generator](https://www.boot.dev/courses/build-static-site-generator-python) de [Boot.dev](https://www.boot.dev).
