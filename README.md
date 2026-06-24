# NetfloxPyDesk

Proyecto integrador de desarrollo de software utilizando **Python 3**, **Qt Designer** y la librería gráfica **PyQt6**, basado en la estructura modular `uixcore`.

---

## Sprint 1 y 2: Estructura Base y Ajustes Iniciales

En estas primeras etapas se migró y depuró la estructura del template base para adaptarla a los requerimientos específicos de la aplicación:

* **Personalización de la interfaz:** Se reconfiguró el título de la ventana principal a `"NetfloxPyDesk"` y se estableció un tamaño predeterminado de `1024x720` píxeles.
* **Menú Dinámico:** Se incorporó con éxito la nueva sección de **"Movies" (Películas)** en la barra de navegación lateral, vinculada a un contenedor limpio y preparado para las futuras funcionalidades del sistema.
* **Entorno Virtual:** Se configuró un entorno virtual limpio (`env`) resolviendo los conflictos de dependencias con `PyQt6`.

---

##  Requisitos e Instalación

Para ejecutar este proyecto de forma local, asegúrate de tener Python instalado y sigue estos pasos en tu terminal de PowerShell:

```sh
# 1. Clonar el repositorio o ingresar a la carpeta del proyecto
cd netfloxpydesk

# 2. Activar el entorno virtual local
.\env\Scripts\Activate.ps1

# 3. Instalar la librería gráfica requerida
python -m pip install PyQt6
