"""
Script para restaurar todas las imágenes originales desde la carpeta de backup.
Para restaurar todo:
    python restaurar_fotos.py
Para restaurar un archivo específico:
    python restaurar_fotos.py nombre_archivo.jpg
"""
import os, sys, shutil

backup_dir = '_backup_images_originales'
target_dir = 'static/images'

if not os.path.exists(backup_dir):
    print(f"Error: No se encontró la carpeta de backup '{backup_dir}'.")
    sys.exit(1)

specific_target = sys.argv[1].lower().replace('\\', '/') if len(sys.argv) > 1 else None
specific_name = os.path.basename(specific_target) if specific_target else None

restored = 0
for root, dirs, files in os.walk(backup_dir):
    rel_path = os.path.relpath(root, backup_dir).replace('\\', '/')
    dest_dir = os.path.join(target_dir, rel_path)
    os.makedirs(dest_dir, exist_ok=True)
    for f in files:
        full_rel = os.path.normpath(os.path.join(rel_path, f)).replace('\\', '/')
        if specific_target and (specific_name != f.lower() and specific_target not in full_rel.lower()):
            continue
        src_file = os.path.join(root, f)
        dest_file = os.path.join(dest_dir, f)
        shutil.copy2(src_file, dest_file)
        print(f"Restaurada: {full_rel}")
        restored += 1

print(f"\nProceso finalizado. Total de imágenes restauradas: {restored}")

