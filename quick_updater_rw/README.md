# Quick Updater RW

Modulo para Odoo 17 Community que agrega un acceso rapido en la barra superior para buscar y actualizar modulos instalados.

Esta version esta adaptada para usarse junto con `responsive_web`, evitando que los estilos de ese modulo conviertan el dropdown del actualizador en un menu de pantalla completa.

## Que hace

- Agrega un widget en el systray de Odoo.
- Permite buscar modulos instalados por nombre.
- Actualiza un modulo desde el mismo widget.
- Permite guardar modulos favoritos en el navegador.
- Muestra errores de actualizacion en un panel legible y copiable.
- Guarda un historial basico de las actualizaciones realizadas desde el widget.

## Requisitos

- Odoo 17 Community Edition.
- Modulo `responsive_web` instalado.
- Acceso de administrador en Odoo.

## Instalacion

1. Copia la carpeta `quick_updater_rw` dentro de tu ruta de addons.
2. Reinicia el servidor de Odoo.
3. Actualiza la lista de aplicaciones.
4. Busca `Quick Updater RW` e instala el modulo.

## Uso

1. Entra a Odoo con un usuario administrador.
2. Abre el widget desde la barra superior.
3. Busca el modulo que quieres actualizar.
4. Presiona `Actualizar`.

Si falla la actualizacion, el widget mostrara el detalle del error y un boton para copiarlo.

## Notas

- Esta variante depende de `responsive_web`.
- El widget solo se muestra a usuarios administradores.
- Solo permite actualizar modulos ya instalados.
- Si usas esta version, no necesitas instalar tambien `quick_module_updater_dz`.

## Licencia

LGPL-3
