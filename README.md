# 🎨 Bauhaus — Plataforma Web & Catálogo Técnico Industrial

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)](https://cloudflare.com)
[![Coolify](https://img.shields.io/badge/Coolify-6B21A8?style=for-the-badge&logo=traefik&logoColor=white)](https://coolify.io)

Plataforma digital corporativa y catálogo técnico de recubrimientos para **Bauhaus Pinturería Técnica Industrial** (Córdoba, Argentina). Diseñada para conectar el sector de aplicación profesional, obras de arquitectura e industrias de gran escala con soluciones especializadas en recubrimientos epóxicos, poliuretánicos y protección anticorrosiva.

---

## 📌 1. Resumen Ejecutivo (Portfolio Case Study)

* **Cliente:** Bauhaus Recubrimientos Técnicos / Pinturería Industrial.
* **Ubicación:** Recta Martinolli 8197, Argüello, Córdoba, Argentina.
* **Dominio Oficial:** `https://bauhaus.ar`
* **Tipo de Proyecto:** Desarrollo Web Full-Stack, Catálogo de Productos y Despliegue Cloud Automatizado.
* **Rol:** Lead Full-Stack Developer & DevOps Architect.

### 🎯 Desafíos Comerciales y Técnicos
1. **Diferenciación de nicho:** Posicionar a Bauhaus más allá de una pinturería convencional, destacando su liderazgo técnico en líneas de alta exigencia (Casablanca, Hempel, Sinteplast).
2. **Segmentación de audiencias:** Crear flujos de navegación diferenciados para:
   * **Aplicadores & Contratistas:** Fichas técnicas, rendimiento por m², asistencia de cálculo y asesoramiento de obra.
   * **Industrias & Grandes Obras:** Tratamientos de pisos de alto tránsito, barreras químicas, control de corrosión y portfolio de clientes corporativos (Aguas Cordobesas, Caminos de las Sierras, Cervecería Quilmes, Grupo Edisur).
3. **Prelanzamiento Seguro (Modo Próximamente Blindado):** Permitir la delegación DNS anticipada del dominio `.ar` y la validación de certificados SSL sin exponer secciones en desarrollo, canalizando el 100% de las visitas hacia canales comerciales directos (WhatsApp y Redes).
4. **Infraestructura Cloud Robusta y Autónoma:** Despliegue en VPS propio con Coolify y Traefik, orquestado bajo Docker y protegido perimetralmente con Cloudflare.

---

## 🚀 2. Características y Módulos Desarrollados

### 🏢 Portada Institucional (Home)
* Hero interactivo con paleta cromática oficial del Brand Book corporativo (`#000c1b` Navy, `#e7b924` Amarillo Bauhaus, `#007ab4` Azul Técnico).
* Selector dinámico por perfiles de usuario (Aplicador Profesional vs. Industria / Empresa).
* Mosaico de marcas oficiales y validación de clientes con logos vectorizados en alta fidelidad.

### 🛠️ Módulo Especializado: Aplicadores Profesionales
* Calculadora / Asistente orientativo de recubrimientos y preparación de sustratos.
* Presentación de sistemas epóxicos autonivelantes, microcementos y poliuretanos.
* Vía rápida de presupuestación directa por WhatsApp con mensaje pre-armado contextual.

### 🏭 Módulo Especializado: Industria & Obras
* Galerías temáticas de soluciones técnicas: Pisos industriales, Protección anticorrosiva, Resistencia química e Impermeabilización estructural.
* Casos de éxito y validación corporativa.
* Formulario de asesoramiento técnico en planta.

### 🔒 Modo "Próximamente" con Blindaje Perimetral
* **Middleware Inteligente (`core/middleware.py`):**
  * En entorno productivo (`bauhaus.ar`), intercepta todas las rutas públicas y sirve la landing de prelanzamiento en milisegundos.
  * Rutas exentas seguras: Panel de administración (`/admin/`) y recursos estáticos (`/static/`, `/media/`) accesibles para el administrador.
  * Interruptor instantáneo por variable de entorno (`MODO_PROXIMAMENTE=True/False`) para lanzamiento oficial en menos de 30 segundos sin recompilar código.

---

## ⏱️ 3. Desglose y Estimación de Tiempos de Proyecto (WBS)

Esta matriz detalla las horas efectivas y fases de trabajo invertidas para la planificación, desarrollo y despliegue del proyecto:

| Fase | Tareas y Entregables Clave | Horas Est. |
| :--- | :--- | :---: |
| **Fase 1: Discovery & Branding** | • Relevamiento de requisitos comerciales y catálogo de marcas.<br>• Extracción, vectorización y optimización de activos del Brand Book corporativo.<br>• Arquitectura de información y wireframes de flujos (Aplicadores vs. Industria). | **18 hs** |
| **Fase 2: Frontend & UI Design** | • Maquetación responsiva Tailwind CSS para Mobile (iOS/Android) y Desktop.<br>• Implementación de carrusel corporativo, banners y mosaicos de obras.<br>• Landing interactiva de prelanzamiento optimizada para conversión directa a WhatsApp.<br>• Adaptación tipográfica oficial (`Rethink Sans`). | **32 hs** |
| **Fase 3: Backend & Lógica Django** | • Configuración modular de Django (Apps: `catalog`, `contacts`, `core`).<br>• Desarrollo de modelos de datos, vistas y gestión de formularios de contacto.<br>• Creación del Middleware `ModoProximamenteMiddleware` con segregación de entornos.<br>• Configuración de seguridad (HSTS, CSRF Trusted Origins, Secure SSL Redirect). | **28 hs** |
| **Fase 4: DevOps & Contenedorización** | • Creación del `Dockerfile` multi-stage optimizado (Python 3.11-slim, Gunicorn).<br>• Pipeline de recolección de estáticos con WhiteNoise (Brotli/Gzip compression).<br>• Configuración de volúmenes persistentes para almacenamiento de fichas técnicas en `/media/`. | **16 hs** |
| **Fase 5: Infraestructura Cloud & DNS** | • Aprovisionamiento de VPS y despliegue continuo con Coolify & Traefik.<br>• Configuración de zona DNS en Cloudflare (Registros A, CNAME, reglas de redirección 301 www &rarr; raíz).<br>• Criptografía SSL/TLS modo Full/Strict perimetral y mitigación DDoS.<br>• Delegación autoritativa en NIC Argentina (`nic.ar`) con clave fiscal Nivel 3. | **14 hs** |
| **Fase 6: QA, Testing & Documentación** | • Pruebas cruzadas de responsividad (Safari iOS, Chrome, Edge).<br>• Validación de performance y SEO semántico.<br>• Elaboración del Manual de Despliegue en Producción en PDF corporativo.<br>• Documentación técnica y entrega de repositorio. | **12 hs** |
| **TOTAL ESTIMADO** | **Proyecto Integral Llave en Mano** | **120 hs** |

> **Cronograma sugerido de ejecución:** 3 a 4 semanas a ritmo de dedicación semi-exclusiva (30-40 hs semanales) o 6 semanas en modalidad part-time.

---

## 🛠️ 4. Stack Tecnológico

* **Lenguaje:** Python 3.11+
* **Framework Web:** Django 5.x
* **Frontend:** HTML5 Semántico, JavaScript ES6+, Tailwind CSS
* **Servidor de Aplicación (WSGI):** Gunicorn
* **Servidor de Archivos Estáticos:** WhiteNoise
* **Contenedores & Orquestación:** Docker (Multi-stage build), Coolify (PaaS Self-Hosted)
* **Reverse Proxy de VPS:** Traefik
* **Seguridad, CDN & DNS:** Cloudflare (WAF, SSL Full Strict, DDoS Mitigation)
* **Entidad Registrante:** NIC Argentina (`nic.ar`)

---

## ⚙️ 5. Ejecución en Entorno Local (Desarrollo)

### Prerrequisitos
* Python 3.11+ instalado.
* Git.

### Instalación
```bash
# 1. Clonar el repositorio
git clone https://github.com/GerardodeMartini/BAUHAUS.git
cd BAUHAUS

# 2. Crear y activar el entorno virtual
python -m venv .venv
source .venv/bin/activate      # En Linux/Mac
.venv\Scripts\activate         # En Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear archivo de variables de entorno
cp .env.example .env

# 5. Ejecutar migraciones iniciales
python manage.py migrate

# 6. Levantar el servidor de desarrollo
python manage.py runserver
```

Acceder a `http://127.0.0.1:8000/`. En entorno local, la navegación por `/inicio/`, `/aplicadores/` e `/industria/` está habilitada para testing activo.

---

## 🐳 6. Despliegue con Docker

```bash
# Construir la imagen localmente
docker build -t bauhaus-web .

# Correr el contenedor mapeando el puerto 8000
docker run -d -p 8000:8000 --name bauhaus-app bauhaus-web
```

---

## 📄 7. Licencia & Créditos

* **Desarrollo y Arquitectura:** Gerardo De Martini
* **Propiedad Intelectual y Marca:** Bauhaus Pinturería Técnica Industrial © 2026. Todos los derechos reservados.
