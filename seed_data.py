import os
import django

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from catalog.models import Categoria, Producto
from portfolio.models import ProyectoObra

def seed():
    print("Iniciando carga de datos de prueba desde PDF Corporativo...")

    # 1. Crear Categorías
    cat_epoxi, _ = Categoria.objects.get_or_create(
        slug="epoxi",
        defaults={
            "nombre": "Epoxi",
            "descripcion": "Sistemas epoxídicos de alta resistencia química y física para pisos, tanques y estructuras.",
            "orden": 1
        }
    )
    
    cat_pu, _ = Categoria.objects.get_or_create(
        slug="poliuretanicos",
        defaults={
            "nombre": "Poliuretánicos",
            "descripcion": "Recubrimientos elásticos de alta resistencia mecánica y excelente retención de color a la intemperie.",
            "orden": 2
        }
    )
    
    cat_membranas, _ = Categoria.objects.get_or_create(
        slug="membranas",
        defaults={
            "nombre": "Membranas e Impermeabilizantes",
            "descripcion": "Impermeabilizantes líquidos avanzados para techos, cubiertas y estructuras hidráulicas.",
            "orden": 3
        }
    )

    cat_anticorrosivos, _ = Categoria.objects.get_or_create(
        slug="anticorrosivos-e-ignifugos",
        defaults={
            "nombre": "Anticorrosivos e Ignífugos",
            "descripcion": "Sistemas de protección pasiva para estructuras metálicas, plantas y tanques.",
            "orden": 4
        }
    )

    print("Categorías creadas correctamente.")

    # 2. Crear Productos
    Producto.objects.get_or_create(
        slug="pintura-epoxi-alto-transito",
        defaults={
            "categoria": cat_epoxi,
            "nombre": "Pintura Epoxi de Alto Tránsito",
            "imagen_principal": "servicios/pisos_epoxy.jpg",
            "descripcion_breve": "Pintura epoxi bicomponente de alta resistencia para pisos industriales y comerciales.",
            "presentacion": "Balde 20 Litros (Componente A + B)",
            "orden": 1,
            "descripcion_detallada": "Pintura formulada a base de resinas epoxídicas curadas con poliamidas. Ofrece una película de gran dureza, excelente resistencia a la abrasión y ataque químico moderado. Ideal para garages, laboratorios, talleres mecánicos y depósitos.",
            "rendimiento_m2": "4 a 6 m² por litro por mano",
            "tiempo_secado": "Al tacto: 4hs | Repintado: 12-24hs | Tránsito Liviano: 48hs | Tránsito Pesado/Curado Total: 7 días",
            "tipo_superficie": "Hormigón firme, seco, libre de aceites, grasas y lechada de cemento. Se recomienda desbaste mecánico.",
            "resistencia_quimica": "Excelente resistencia a derrames de grasas, hidrocarburos, aceites, agua salada y soluciones de limpieza industriales.",
            "destacado_home": True,
            "mostrar_en_aplicadores": True,
            "mostrar_en_industria": True,
            "activo": True
        }
    )

    Producto.objects.get_or_create(
        slug="membrana-poliuretano-liquida",
        defaults={
            "categoria": cat_membranas,
            "nombre": "Membrana de Poliuretano Líquida",
            "imagen_principal": "servicios/aplicacion_recubrimientos.jpg",
            "descripcion_breve": "Membrana líquida impermeable de alta elasticidad para cubiertas transitables.",
            "presentacion": "Balde 25 Kilos (Listo para usar)",
            "orden": 2,
            "descripcion_detallada": "Recubrimiento impermeable elástico monocomponente a base de poliuretano en emulsión acuosa. Una vez seco forma una membrana continua y elástica sin soldaduras ni juntas, ideal para cubiertas, balcones y terrazas transitables.",
            "rendimiento_m2": "1.5 a 2.0 kg por m² (aplicado en 3 o 4 manos con malla de refuerzo)",
            "tiempo_secado": "Secado al tacto: 6hs | Entre manos: 12 a 24hs según condiciones climáticas",
            "tipo_superficie": "Losa de hormigón, carpetas cementicias bien niveladas, baldosas no esmaltadas o chapa galvanizada.",
            "resistencia_quimica": "Resistencia a la radiación UV del sol sin degradarse y al estancamiento temporario de agua de lluvia.",
            "destacado_home": True,
            "mostrar_en_aplicadores": True,
            "mostrar_en_industria": True,
            "activo": True
        }
    )

    Producto.objects.get_or_create(
        slug="poliuretano-alifatico-resistencia",
        defaults={
            "categoria": cat_pu,
            "nombre": "Poliuretano Alifático de Alta Resistencia",
            "imagen_principal": "portfolio/hero_industrial.jpg",
            "descripcion_breve": "Esmalte poliuretánico alifático para protección anticorrosiva y retención de brillo en exteriores.",
            "presentacion": "Kit 4 Litros",
            "orden": 3,
            "descripcion_detallada": "Esmalte poliuretánico de dos componentes de alto brillo y extraordinaria resistencia a la intemperie extrema. Ideal para proteger estructuras metálicas de barcos, puentes, silos y maquinaria industrial expuesta.",
            "rendimiento_m2": "8 a 10 m² por litro por mano (espesor seco recomendado de 50 micrones)",
            "tiempo_secado": "Libre de polvo: 2hs | Al tacto: 4hs | Repintado: 8 a 24hs",
            "tipo_superficie": "Superficies de acero tratadas previamente con una base imprimación o fondo epoxi anticorrosivo adecuado.",
            "resistencia_quimica": "Excelente retención de brillo y color bajo el sol directo. Alta resistencia a vapores químicos, humedad y rociado de agua salina.",
            "destacado_home": True,
            "mostrar_en_aplicadores": True,
            "mostrar_en_industria": True,
            "activo": True
        }
    )

    Producto.objects.get_or_create(
        slug="recubrimiento-epoxi-tanques-prfv",
        defaults={
            "categoria": cat_epoxi,
            "nombre": "Sistema Epoxi / PRFV para Tanques y Estructuras",
            "imagen_principal": "portfolio/tanque_industrial.jpg",
            "descripcion_breve": "Esquema anticorrosivo e inerte de alta resistencia química para recipientes y plantas de proceso.",
            "presentacion": "Tambor 200 Litros / Juego A+B",
            "orden": 4,
            "descripcion_detallada": "Sistema epoxídico con refuerzo de fibra de vidrio (PRFV/ERFV) formulado para revestir interior de tanques de combustible, plantas químicas y piletas de tratamiento.",
            "rendimiento_m2": "Según especificación de pliego (300 a 500 micrones)",
            "tiempo_secado": "Curado químico completo: 7 días a 20°C",
            "tipo_superficie": "Granallado o arenado al grado casi blanco (SSPC-SP10 / Sa 2.5).",
            "resistencia_quimica": "Inerte a solventes, ácidos diluidos, álcalis y agua tratada.",
            "destacado_home": False,
            "mostrar_en_aplicadores": False,
            "mostrar_en_industria": True,
            "activo": True
        }
    )

    print("Productos creados correctamente.")

    # 3. Crear Proyectos de Referencia (Portfolio)
    ProyectoObra.objects.get_or_create(
        titulo="Recubrimiento & Mantenimiento de Planta Industrial",
        defaults={
            "cliente_ubicacion": "Planta Industrial, Córdoba",
            "categoria_trabajo": "Alpinismo Industrial & Recubrimientos Epoxi",
            "imagen_despues": "portfolio/hero_industrial.jpg",
            "descripcion_corta": "Protección anticorrosiva de estructuras metálicas en altura mediante técnicas de alpinismo industrial y aplicación de esmalte poliuretánico alifático.",
            "publicado": True,
            "orden": 1
        }
    )

    ProyectoObra.objects.get_or_create(
        titulo="Revestimiento de Tanques en Espacios Confinados",
        defaults={
            "cliente_ubicacion": "Planta Química / Procesadora",
            "categoria_trabajo": "Sistemas PRFV & Epoxídicos en Altura",
            "imagen_despues": "portfolio/tanque_industrial.jpg",
            "descripcion_corta": "Tratamiento anticorrosivo e impermeabilización interna de tanques mediante resinas epoxi y PRFV en ambientes de atmosfera controlada.",
            "publicado": True,
            "orden": 2
        }
    )

    ProyectoObra.objects.get_or_create(
        titulo="Piso Epoxi Autonivelante & Demarcación Vial",
        defaults={
            "cliente_ubicacion": "Nave Logística y Centro de Distribución",
            "categoria_trabajo": "Pisos Epoxi Autonivelantes & Señalización",
            "imagen_despues": "portfolio/piso_autonivelante.jpg",
            "descripcion_corta": "Rehabilitación de solado industrial de 2500m² con sistema epoxi de alta resistencia al tránsito de autoelevadores y demarcaciones reflectivas.",
            "publicado": True,
            "orden": 3
        }
    )

    print("Proyectos de portfolio creados correctamente.")
    print("¡Carga de datos finalizada con éxito!")

if __name__ == "__main__":
    seed()
