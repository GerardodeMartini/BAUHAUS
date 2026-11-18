# 🎨 Bauhaus — Plataforma Web Corporativa & Catálogo Técnico Industrial

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)](https://gunicorn.org)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Hetzner](https://img.shields.io/badge/Hetzner_Cloud-D50C2D?style=for-the-badge&logo=hetzner&logoColor=white)](https://hetzner.com)
[![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)](https://cloudflare.com)

Plataforma web institucional, catálogo de soluciones técnicas y portal de ingeniería en recubrimientos desarrollado para **Bauhaus Pinturería Técnica Industrial** (Córdoba, Argentina).

🌐 **Sitio en Producción:** [https://bauhaus.ar](https://bauhaus.ar)  
📍 **Sede Comercial & Centro Técnico:** Av. Recta Martinolli 8197, Argüello, Córdoba, Argentina.

---

## 📋 Índice de Contenidos

1. [Visión General del Proyecto](#-1-visión-general-del-proyecto)
2. [Identidad Visual y Sistema de Diseño (UI/UX)](#-2-identidad-visual-y-sistema-de-diseño-uiux)
3. [Recorrido Detallado por Vistas y Funcionalidades](#-3-recorrido-detallado-por-vistas-y-funcionalidades)
   - [Layout Base, Navegación y Footer Inteligente](#31-layout-base-navegación-y-footer-inteligente-templatesbasehtml)
   - [Portada Institucional (Home)](#32-portada-institucional--home-templateshomehtml)
   - [Módulo de Productos y Soluciones](#33-módulo-de-productos-y-soluciones-templatesproductoshtml)
   - [Módulo División Industria y Obras](#34-módulo-división-industria-y-obras-templatesindustriahtml)
   - [Sistema de Prelanzamiento y Control de Acceso](#35-sistema-de-prelanzamiento-y-control-de-acceso-coremiddlewarepy)
4. [Arquitectura Backend y Modelos de Datos (Django)](#-4-arquitectura-backend-y-modelos-de-datos-django)
5. [Estructura del Proyecto](#-5-estructura-del-proyecto)
6. [Stack Tecnológico e Infraestructura Cloud](#-6-stack-tecnológico-e-infraestructura-cloud)
7. [Instalación y Ejecución en Entorno Local](#-7-instalación-y-ejecución-en-entorno-local)
8. [Variables de Entorno (`.env`)](#-8-variables-de-entorno-env)
9. [Despliegue en Producción con Docker](#-9-despliegue-en-producción-con-docker)
10. [Créditos y Licencia](#-10-créditos-y-licencia)

---

## 🎯 1. Visión General del Proyecto

**Bauhaus Pinturería Técnica Industrial** se especializa en recubrimientos de alta exigencia para pisos industriales, protección anticorrosiva, impermeabilización estructural, repintado automotriz y obras de arquitectura.

La plataforma fue diseñada y construida a medida para resolver tres objetivos comerciales clave:
1. **Posicionamiento Técnico Diferencial:** Transmitir solidez ingenieril y respaldo en obra, diferenciándose de una pinturería minorista tradicional mediante casos de estudio reales, fichas de aplicación y validación de grandes empresas.
2. **Segmentación Clara de Audiencias:**
   - **Hogar, Obra y Aplicadores (`/productos/`):** Catálogo organizado por líneas de producto, marcas líderes, propuestas de valor agregado y novedades del centro técnico.
   - **División Industria (`/industria/`):** Soluciones críticas de ingeniería (epóxicos, poliuretanos, altas temperaturas, barreras químicas), servicio de aplicación en planta y portfolio documentado de obras de gran escala.
3. **Conversión Directa y Sin Fricción:** Integración de flujos de consulta contextualizados que conectan al cliente o jefe de planta directamente con los asesores técnicos vía **WhatsApp** (con mensajes pre-armados según el producto o rubro seleccionado) y formularios corporativos/licitaciones.

---

## 🎨 2. Identidad Visual y Sistema de Diseño (UI/UX)

El frontend implementa fielmente el **Brand Book oficial de Bauhaus**, combinando estética industrial moderna con geometría inspirada en la escuela Bauhaus:

### Paleta Cromática Oficial
| Color | Hex | Uso en la Plataforma |
| :--- | :--- | :--- |
| **Azul Profundo Bauhaus** | `#000c1b` | Textos principales, contenedores técnicos del blog, fondos de contraste y botones de acción. |
| **Azul Técnico** | `#4081c1` / `#007ab4` | Bloques de títulos en portadas, sección de respaldo técnico en Industria, botones de consulta y acentos interactivos. |
| **Amarillo Bauhaus** | `#e7b924` | Indicadores de navegación activa, bloque de *Valor Agregado*, marcos internos de fotografías y destacados. |
| **Rojo Bauhaus** | `#E52424` / `#b11617` | Separador geométrico curvo del footer y marcos internos en bloques de formulario y galería de obras. |
| **Gris Claro Neutro** | `#f6f7f9` | Fondos de secciones intercaladas, tarjetas de marcas y footer institucional. |

### Tipografía y Detalles Geométricos
* **Tipografía Corporativa:** `Rethink Sans` (Google Fonts) en pesos `400`, `500`, `600`, `700` y `800`.
* **Remates Curvos en Cuarto de Círculo (SVG):** Los bloques de encabezado en los banners principales y el separador rojo del footer terminan en un cuarto de círculo vectorial (`viewBox="0 0 80 60"`) que aporta la firma visual de la marca.
* **Contenedores de Marca (`marco-marca`):** Tarjetas con esquina inferior derecha curva (`border-radius: 0 0 75px 0`), borde sutil y efecto de elevación en `hover`.
* **Sello Giratorio en Footer:** El isotipo `B` tricolor permanece fijo en el centro mientras el anillo tipográfico *"Pinturería Técnica Industrial"* gira de forma continua y suave (`animate-spin-slow`, 22s por revolución).
* **Diseño Mobile-First Simétrico:** En dispositivos móviles se preserva la proporción de bloques `50% / 50%` (2 columnas con alturas igualadas mediante `items-stretch` y `h-full`) para mantener la armonía editorial de la versión de escritorio sin alargar excesivamente las páginas.

---

## 🖥️ 3. Recorrido Detallado por Vistas y Funcionalidades

### 3.1. Layout Base, Navegación y Footer Inteligente (`templates/base.html`)
* **Barra de Navegación Sticky:** Cabecera fija con logotipo oficial, enlaces a `Home`, `Productos`, `Industria` y `Contacto` con subrayado dinámico `#e7b924` en la página activa, y menú desplegable táctil para móviles.
* **Botón Flotante de WhatsApp:** Acceso permanente en la esquina inferior derecha para asistencia técnica inmediata.
* **Footer Corporativo en 4 Columnas:**
  1. **Sello Bauhaus Animado:** Logo central fijo + anillo de texto giratorio.
  2. **Navegación Rápida:** Enlaces directos a todas las secciones.
  3. **Contacto y Redes:** Dirección física, enlaces directos a WhatsApp de los asesores técnicos (*Sebastián* y *Juan*), correo electrónico (`bauhaustecnico@gmail.com`) e íconos vectoriales a Facebook, Instagram y LinkedIn.
  4. **Mapa de Ubicación Optimizado:** `<iframe>` conectado directamente al endpoint `www.google.com/maps/embed` de la ficha verificada **BAUHAUS Pintura Epoxi** (evitando redirecciones `301` con bloqueo `X-Frame-Options: SAMEORIGIN` en navegadores móviles).
* **Separador Rojo Dinámico:** Script de alineación (`alignFooterSeparator`) que calcula en tiempo real la coordenada `right` de la columna del mapa para que el remate curvo rojo del footer termine exactamente alineado con el borde derecho del mapa en cualquier resolución de pantalla.

---

### 3.2. Portada Institucional — Home (`templates/home.html`)
1. **Hero Carrusel Full-Viewport (`calc(100dvh - 96px)` en PC / `calc(100dvh - 80px)` en móvil):**
   - Slider automático de 3 fotografías industriales de alta resolución con transición suave de opacidad cada 5 segundos.
   - Controles manuales mediante flechas laterales e indicadores inferiores (*dots*).
   - Bloque de título con extensión de color azul `#4081c1` hasta el borde izquierdo de la pantalla, remate curvo SVG y botones de acción hacia *Ver Productos* y *Contacto*.
2. **Sección "Quiénes Somos":**
   - Presentación de la trayectoria de Bauhaus (desde 2018 en Córdoba) con layout simétrico de 2 columnas: fotografía del local comercial con marco interno amarillo `#e7b924` y reseña institucional.
3. **Carrusel Infinito de Distribuidores Oficiales (Movimiento LTR):**
   - Marquee continuo sin cortes con los logotipos oficiales de **Casablanca, Hempel, Revesta, Sherwin Williams, Sika, Sinteplast y Tecnopol**.
   - Escalado individualmente calibrado por marca para desktop, tablet y móvil.
4. **Blog de Soluciones Técnicas:**
   - Slider interactivo de artículos técnicos (ej. *"Pintura epoxi para pisos: por qué fallan muchos trabajos"* y guías de preparación de sustratos) dentro de una tarjeta `#000c1b` con fotografía enmarcada y paginación por dots.
5. **Carrusel Infinito "Empresas que Confían en Nosotros" (Movimiento RTL):**
   - Banda continua con clientes corporativos e institucionales: **Aguas Cordobesas, Caminos de las Sierras, Grupo Edisur, Cervecería y Maltería Quilmes, Kolektor, Hospital Privado, Sanatorio Allende, Universidad Siglo 21, Renault y Tarjeta Naranja**.
6. **Formulario de Contacto Directo:**
   - Bloque 50% fotografía con marco rojo `#b11617` y 50% formulario (*Nombre, Email, Mensaje*) que estructura la consulta y redirige a WhatsApp listo para enviar.
7. **Banner Panorámico de Cierre:**
   - Imagen industrial de ancho completo con filtro azul corporativo y la frase institucional:  
     *"Bauhaus. Cada superficie tiene una función, cada función una protección."*

---

### 3.3. Módulo de Productos y Soluciones (`templates/productos.html`)
1. **Hero de Productos:** Portada a pantalla completa enfocada en soluciones integrales de recubrimiento.
2. **Grilla de Línea de Productos (4 Verticales):**
   - **Línea Industrial:** Epóxicos, poliuretanos, anticorrosivos y recubrimientos para pisos de alto desempeño.
   - **Hogar y Obra:** Látex interior/exterior, impermeabilizantes para techos y muros, esmaltes y protectores de madera.
   - **Línea Automotriz:** Sistemas de repintado, primers, aparejos, barnices y productos de pulido y terminación.
   - **Accesorios e Insumos:** Rodillos aptos para epoxi, pinceles, lijas técnicas, cintas de enmascarar, diluyentes y elementos de seguridad.
   - Cada tarjeta incluye botón **"Consultar"** que abre WhatsApp con el mensaje pre-configurado para esa línea específica.
3. **Carrusel de Marcas Comercializadas:** Banda continua con las 7 marcas oficiales.
4. **Bloque "Nuestro Valor Agregado":**
   - Sección destacada sobre fondo Amarillo Bauhaus (`#e7b924`) que explica el acompañamiento técnico antes, durante y después de la compra.
5. **Sección "Conocé Más de Nosotros" — Feed Nativo de Instagram (`@bauhauspinturerias`):**
   - Tarjetas diseñadas con la interfaz nativa de Instagram (avatar con aro degradado, usuario, fotografía cuadrada, botones interactivos de *Me gusta*, *Comentar*, *Compartir* y *Guardar*, contador de likes, descripción y link directo al post real).
   - **Doble Comportamiento Responsivo:**
     - **En PC y Tablet (`>= 640px`):** Grilla estática de 4 columnas mostrando los 4 posteos en simultáneo.
     - **En Celulares (`< 640px`):** Carrusel deslizante continuo (*Track Slider*) acelerado por hardware (`transform: translateX`) con transición fluida `cubic-bezier`, rotación automática cada 4.5s, soporte para deslizar con el dedo (*touch swipe*), pausa automática al interactuar y controles inferiores con flechas y puntos indicadores.
6. **Formulario de Asesoramiento y Banner Panorámico Final:**
   - Con la leyenda: *"Bauhaus. Preparar bien, elegir mejor, proteger por más tiempo."*

---

### 3.4. Módulo División Industria y Obras (`templates/industria.html`)
1. **Hero División Industria:** Portada técnica orientada a plantas industriales, ingenieros, jefes de mantenimiento y contratistas de obra pública/privada.
2. **Pinturas Técnicas para la Industria (4 Especialidades):**
   - **Pisos Industriales:** Sistemas epóxicos, poliuretánicos y autonivelantes resistentes a tránsito pesado de autoelevadores, abrasión e impacto.
   - **Protección Anticorrosiva:** Esquemas de alto espesor para estructuras metálicas, tanques, cañerías y ambientes agresivos.
   - **Altas Temperaturas y Resistencia Química:** Recubrimientos especiales para hornos, calderas, chimeneas y zonas de derrame ácido o alcalino.
   - **Impermeabilización Estructural:** Soluciones técnicas para cubiertas industriales, terrazas, cisternas y juntas de dilatación.
3. **Bloque "Del Producto a la Aplicación" (Respaldo Técnico Integral):**
   - Sección sobre fondo Azul Técnico (`#4081c1`) que presenta el servicio de relevamiento en planta, especificación del esquema técnico, provisión de materiales y **servicio de aplicación con mano de obra especializada**.
4. **Galería Interactiva "Experiencia en Obra" (Casos de Éxito con Visor Modal):**
   - 4 tarjetas de proyectos emblemáticos ejecutados por Bauhaus:
     1. **Aguas Cordobesas (Planta Potabilizadora Suquía):** Rehabilitación y esquema anticorrosivo de instalaciones críticas.
     2. **Caminos de las Sierras (Estaciones de Peaje):** Recubrimientos de alta resistencia mecánica e impermeabilización.
     3. **Cervecería y Maltería Quilmes:** Intervención técnica en pisos y áreas operativas de planta.
     4. **Grupo Edisur:** Protección de infraestructura vial, estructuras metálicas y obras civiles.
   - Al hacer click en **"Ver trabajo"** en cualquiera de las tarjetas, se despliega un **Modal Interactivo** con carrusel fotográfico de la obra (imágenes del proceso y resultado final), navegación por teclado/táctil y descripción técnica detallada de la intervención.
5. **Carrusel de Clientes Industriales, Formulario y Banner de Cierre:**
   - Con la frase: *"Bauhaus. Soluciones técnicas pensadas para durar en ambientes exigentes."*

---

### 3.5. Sistema de Prelanzamiento y Control de Acceso (`core/middleware.py`)
El proyecto incluye un módulo de control perimetral (`ModoProximamenteMiddleware`) activable por configuración para etapas de mantenimiento o prelanzamiento:
* **Landing "Próximamente" (`templates/proximamente.html`):** Vista de transición con canales directos de WhatsApp, ubicación y redes.
* **Desbloqueo de Vista Previa (`templates/acceso_preview.html`):** Permite a administradores o clientes autorizados navegar el sitio completo ingresando una contraseña en `/acceso/` o mediante enlace rápido (`?clave=...`).
* **Seguridad Integrada:** Comparación criptográfica en tiempo constante (`secrets.compare_digest`), límite de 5 intentos fallidos con bloqueo temporal de 15 minutos contra fuerza bruta, sesión persistente por cookie firmada (`set_signed_cookie`) y cabeceras `X-Robots-Tag: noindex, nofollow`.

---

## 🗄️ 4. Arquitectura Backend y Modelos de Datos (Django)

El backend está modularizado en **4 aplicaciones principales**:

### 1. `core` (Núcleo y Configuración)
* `settings.py`: Gestión de variables de entorno con `python-dotenv`, conexión de base de datos adaptable (`dj-database-url`), servidor de estáticos comprimidos con **WhiteNoise** (`CompressedManifestStaticFilesStorage`), motor de sesiones basadas en cookies firmadas y endurecimiento automático de seguridad cuando `DEBUG=False` (`SECURE_HSTS_SECONDS`, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `X_FRAME_OPTIONS = 'DENY'`).
* `middleware.py`: Lógica del modo de acceso restringido y protección de rutas.

### 2. `catalog` (Catálogo Técnico y Vistas Públicas)
* **Modelo `Categoria`:** Nombre, slug autogenerado, descripción, imagen y orden de visualización.
* **Modelo `Producto`:**
  - *Datos comerciales:* Categoría, nombre, slug, imagen principal, descripción breve, presentación (ej. Balde 20L, Tambor 200L) y orden.
  - *Especificaciones de ingeniería:* Descripción técnica detallada, rendimiento por $\text{m}^2$, tiempo de secado, preparación/tipo de superficie, resistencia química/mecánica y **archivo PDF descargable de la Ficha Técnica** (`upload_to="fichas_tecnicas/"`).
  - *Flags de segmentación:* `destacado_home`, `mostrar_en_aplicadores`, `mostrar_en_industria`, `activo`.

### 3. `portfolio` (Casos de Éxito y Obras)
* **Modelo `ProyectoObra`:** Título del proyecto, cliente/ubicación, categoría de trabajo, fotografía del *Antes* (opcional), fotografía del *Después / Resultado*, descripción del caso, estado de publicación y orden.

### 4. `contacts` (Gestión de Consultas Corporativas y Licitaciones)
* **Modelo `LicitacionContacto`:** Razón social / empresa, CUIT, correo electrónico, teléfono, tipo de cliente (`Aplicador / Profesional` o `Empresa / Industria`), mensaje/requerimiento, **archivo adjunto de pliego técnico** (`upload_to="licitaciones/adjuntos/"`) y fecha de registro.
* **Integración de Correo Transaccional:** Configurado con `django-anymail[resend]` para envío de notificaciones por email a través de la API de **Resend** (con fallback automático a consola en desarrollo local).

---

## 📂 5. Estructura del Proyecto

```text
pintureria-BAUHAUS/
├── catalog/                    # App principal: Vistas públicas, catálogo de categorías y productos
│   ├── migrations/
│   ├── admin.py                # Panel administrativo de productos y categorías
│   ├── models.py               # Modelos Categoria y Producto (con soporte de fichas PDF)
│   ├── urls.py                 # Rutas públicas (/, /productos/, /industria/, /acceso/)
│   └── views.py                # Controladores de vistas y autenticación de preview
├── contacts/                   # App de contacto corporativo y recepción de licitaciones
│   ├── migrations/
│   ├── admin.py
│   ├── forms.py                # Formulario validado LicitacionContactoForm
│   ├── models.py               # Modelo LicitacionContacto con adjuntos
│   ├── urls.py
│   └── views.py
├── portfolio/                  # App de casos de éxito y obras ejecutadas
│   ├── migrations/
│   ├── admin.py
│   └── models.py               # Modelo ProyectoObra (Antes / Después)
├── core/                       # Configuración central del proyecto Django
│   ├── asgi.py
│   ├── middleware.py           # Middleware de control de acceso y prelanzamiento
│   ├── settings.py             # Configuración general, seguridad, WhiteNoise y Anymail
│   ├── urls.py                 # Enrutador raíz
│   └── wsgi.py                 # Punto de entrada WSGI para Gunicorn
├── templates/                  # Plantillas HTML5 + Tailwind CSS + JS modular
│   ├── base.html               # Layout maestro: Navbar, WhatsApp flotante y Footer con Maps
│   ├── home.html               # Portada institucional con Hero slider, Marcas, Blog y Clientes
│   ├── productos.html          # Catálogo de líneas, Valor Agregado y Feed interactivo de Instagram
│   ├── industria.html          # Soluciones industriales, Respaldo técnico y Galería modal de obras
│   ├── proximamente.html       # Landing de prelanzamiento / mantenimiento
│   └── acceso_preview.html     # Pantalla de desbloqueo con contraseña
├── static/                     # Activos estáticos (Imágenes optimizadas, fuentes y vectores)
│   ├── fonts/                  # Tipografía local de respaldo
│   └── images/
│       ├── marcas/             # Logos oficiales (Casablanca, Hempel, Revesta, Sika, Sinteplast, etc.)
│       ├── empresas/           # Logos de clientes corporativos (Aguas Cordobesas, Quilmes, Edisur, etc.)
│       ├── instagram/          # Capturas y avatar del feed oficial de @bauhauspinturerias
│       └── obras/              # Fotografías de alta resolución de las intervenciones industriales
├── media/                      # Archivos subidos dinámicamente (Fichas técnicas PDF, pliegos)
├── Dockerfile                  # Construcción multi-stage optimizada para producción (Python 3.11-slim)
├── requirements.txt            # Dependencias del proyecto Python/Django
├── .env.example                # Plantilla de variables de entorno
└── manage.py                   # CLI de administración de Django
```

---

## 🛠️ 6. Stack Tecnológico e Infraestructura Cloud

* **Lenguaje & Backend:** Python 3.11+, Django 5.x
* **Frontend & UI:** HTML5 Semántico, Tailwind CSS, JavaScript Vanilla (ES6+), SVG Vectorial
* **Base de Datos:** SQLite3 (Desarrollo local) / PostgreSQL (Producción vía `dj-database-url` y `psycopg2-binary`)
* **Procesamiento de Imágenes:** Pillow 10+
* **Servidor WSGI:** Gunicorn 21+
* **Archivos Estáticos:** WhiteNoise 6+ (compresión Brotli/Gzip y cache-busting por hash)
* **Emails Transaccionales:** Resend API (`django-anymail[resend]`)
* **Contenedorización:** Docker (Multi-stage build sobre `python:3.11-slim`)
* **Servidor Cloud (VPS):** Hetzner Cloud
* **Seguridad Perimetral, CDN & SSL:** Cloudflare (DNS autoritativo, SSL/TLS Full Strict, HSTS, mitigación DDoS)
* **Dominio Oficial:** `bauhaus.ar` (NIC Argentina)

---

## ⚙️ 7. Instalación y Ejecución en Entorno Local

### Prerrequisitos
* **Python 3.11** o superior.
* **Git**.

### Paso a paso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/GerardodeMartini/BAUHAUS.git
   cd BAUHAUS
   ```

2. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows (PowerShell):
   .venv\Scripts\Activate.ps1
   # En Linux / macOS:
   source .venv/bin/activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar las variables de entorno locales:**
   ```bash
   cp .env.example .env
   ```

5. **Ejecutar las migraciones de base de datos:**
   ```bash
   python manage.py migrate
   ```

6. **Iniciar el servidor de desarrollo:**
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```

7. **Abrir en el navegador:**
   - Portada Principal (Home): `http://127.0.0.1:8000/`
   - Productos y Soluciones: `http://127.0.0.1:8000/productos/`
   - División Industria: `http://127.0.0.1:8000/industria/`
   - Panel de Administración: `http://127.0.0.1:8000/admin/`

---

## 🔐 8. Variables de Entorno (`.env`)

| Variable | Descripción | Ejemplo en Producción |
| :--- | :--- | :--- |
| `SECRET_KEY` | Clave criptográfica de Django para firmar sesiones y tokens CSRF. | `clave-larga-aleatoria-segura` |
| `DEBUG` | Modo de depuración (`True` en local, `False` obligatorio en producción). | `False` |
| `MODO_PROXIMAMENTE` | Activa (`True`) o desactiva (`False`) la pantalla de prelanzamiento. | `False` |
| `ALLOWED_HOSTS` | Dominios e IPs autorizados separados por comas. | `bauhaus.ar,www.bauhaus.ar` |
| `CSRF_TRUSTED_ORIGINS` | Orígenes confiables con esquema `https://` para envíos POST. | `https://bauhaus.ar,https://www.bauhaus.ar` |
| `DATABASE_URL` | URI de conexión a PostgreSQL (si se deja vacío utiliza `db.sqlite3`). | `postgres://user:pass@db:5432/bauhaus` |
| `RESEND_API_KEY` | API Key de Resend para envío de correos de formularios. | `re_xxxxxxxxx` |
| `EMAIL_SENDER` | Dirección remitente verificada en Resend. | `notificaciones@bauhaus.ar` |
| `EMAIL_RECEIVER` | Casilla donde Bauhaus recibe las consultas y pliegos. | `bauhaustecnico@gmail.com` |

---

## 🐳 9. Despliegue en Producción con Docker

El proyecto cuenta con un `Dockerfile` multi-stage que compila las dependencias nativas (`libpq-dev`, `build-essential`) en una etapa intermedia y genera una imagen final liviana que recolecta los archivos estáticos (`collectstatic`), aplica las migraciones (`migrate --noinput`) y levanta **Gunicorn** en el puerto `8000`:

```bash
# 1. Construir la imagen de producción
docker build -t bauhaus-web .

# 2. Ejecutar el contenedor con el archivo .env de producción
docker run -d \
  --name bauhaus-app \
  --env-file .env \
  -p 8000:8000 \
  --restart unless-stopped \
  bauhaus-web
```

---

## 📄 10. Créditos y Licencia

* **Diseño, Desarrollo Full-Stack & Despliegue Cloud:** [Gerardo De Martini (Gdmar)](https://gdemar.com.ar/)
* **Cliente & Propiedad Intelectual de Marca:** **Bauhaus Pinturería Técnica Industrial** © 2026 — Córdoba, Argentina. Todos los derechos reservados.
