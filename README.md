# Selenium Test

## Descripción

Suite completa de pruebas funcionales automatizadas usando Selenium WebDriver. Incluye pruebas robustas para aplicaciones web con manejo inteligente de selectores dinámicos, esperas explícitas y estrategias de recuperación ante fallos.

### Características Principales

- **Pruebas de búsqueda automatizadas** en múltiples sitios web
- **Selectores robustos** con múltiples estrategias de fallback
- **Esperas inteligentes** para contenido dinámico
- **Soporte multi-navegador** (Chrome, Firefox, Brave, Edge)
- **Reportes detallados** con capturas de pantalla
- **Debug automático** cuando las pruebas fallan
- **Reintentos automáticos** para mayor estabilidad

## Tabla de Contenidos

- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso Básico](#uso-básico)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Pruebas Disponibles](#pruebas-disponibles)
- [Troubleshooting](#troubleshooting)
- [Contribuir](#contribuir)

## Instalación

### Prerrequisitos

- Python 3.8 o superior
- Google Chrome o Chromium instalado
- Git (para clonar el repositorio)

### Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/Leftama/selenium-test-funcional.git
cd selenium-test-funcional

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/macOS:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Verificar Instalación

```bash
python test-busqueda.py
```

## Configuración

### Archivo requirements.txt

```txt
selenium==4.15.2
webdriver-manager==4.0.1
pytest==7.4.3
pytest-html==4.1.1
allure-pytest==2.13.2
python-dotenv==1.0.0
requests==2.31.0
beautifulsoup4==4.12.2
```

### Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Configuración del navegador
BROWSER=chrome
HEADLESS=false
IMPLICIT_WAIT=10
EXPLICIT_WAIT=15

# URLs de prueba
DUCKDUCKGO_URL=https://duckduckgo.com/
GOOGLE_URL=https://www.google.com

# Configuración de reportes
SCREENSHOTS_ENABLED=true
REPORTS_DIR=reports/
DEBUG_MODE=true

# Configuración de navegadores alternativos
BRAVE_PATH=/usr/bin/brave-browser
FIREFOX_PATH=/usr/bin/firefox
```

## Uso Básico

### Ejecutar Todas las Pruebas

```bash
# Ejecutar con pytest
pytest tests/ -v --html=reports/report.html --self-contained-html

# Ejecutar prueba específica
python test-busqueda.py

# Modo headless
HEADLESS=true python test-busqueda.py
```

### Ejecutar con Diferentes Navegadores

```bash
# Chrome (por defecto)
python test-busqueda.py

# Brave
BROWSER=brave python test-busqueda.py

# Firefox
BROWSER=firefox python test-busqueda.py

# Modo headless
python test-busqueda.py --headless
```

## Estructura del Proyecto

```bash
../selenium-test-funcional/
├── evidencia
│   ├── evidencia-00.png
│   └── evidencia-01.png
├── README.md
├── test-busqueda.py
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg
```

## Pruebas Disponibles

### Prueba de Búsqueda (test-busqueda.py)

```python
# Funcionalidades probadas:
✅ Carga de página de búsqueda
✅ Localización del campo de búsqueda
✅ Ingreso de términos de búsqueda
✅ Envío del formulario de búsqueda
✅ Validación de resultados
✅ Extracción de títulos de resultados
```

**Detecta errores como:**

- Campo de búsqueda no disponible
- Búsqueda no funcional
- Resultados no se cargan
- Cambios en la estructura HTML
- Problemas de rendimiento

### Ejecución con Parámetros

```bash
# Buscar término específico
python test-busqueda.py --query "python selenium"

# Verificar número mínimo de resultados
python test-busqueda.py --min-results 5

# Ejecutar en sitio específico
python test-busqueda.py --site duckduckgo
python test-busqueda.py --site google
```

## Troubleshooting

### Problemas Comunes y Soluciones

#### 1. ChromeDriver no compatible

```bash
# Error: SessionNotCreatedException
# Solución: Actualizar ChromeDriver
pip install --upgrade webdriver-manager
```

#### 2. Elementos no encontrados

```python
# Error: NoSuchElementException
# Solución: Usar esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "element-id")))
```

#### 3. Timeouts frecuentes

```python
# Configurar timeouts apropiados
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
driver.set_script_timeout(30)
```

#### 4. Problemas de memoria

```bash
# Configurar límites de memoria para Docker
docker run --memory=2g --shm-size=2g selenium-tests
```

### Debug Mode

Habilita el modo debug agregando `DEBUG=true` a tu archivo `.env`:

```bash
DEBUG=true python test-busqueda.py
```

Esto generará:

- Capturas de pantalla en cada paso
- Logs detallados en `reports/debug.log`
- HTML de la página en caso de error
- Métricas de rendimiento

### Logs Detallados

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('reports/test.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

## Métricas de Rendimiento

```python
import time
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class PerformanceListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        self.start_time = time.time()
    
    def after_navigate_to(self, url, driver):
        load_time = time.time() - self.start_time
        print(f"Page loaded in {load_time:.2f} seconds")

# Usar con el driver
driver = EventFiringWebDriver(webdriver.Chrome(), PerformanceListener())
```

## Contribuir

### Cómo Contribuir

1. **Fork** el proyecto
2. **Crea** una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. **Commit** tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. **Push** a la rama (`git push origin feature/nueva-funcionalidad`)
5. **Crea** un Pull Request

### Guías de Contribución

- Asegúrate de que todas las pruebas pasen
- Agrega tests para nuevas funcionalidades
- Actualiza la documentación si es necesario
- Sigue las convenciones de código (PEP 8)
- Usa nombres descriptivos para commits

## Autores

- **Cristián Araya** - *Desarrollo inicial* - [Leftama](https://github.com/Leftama)

## Agradecimientos

- Selenium WebDriver Team
- Comunidad de Python Testing
- Contribuidores del proyecto

---

⭐ **¡Si este proyecto te ha sido útil, considera darle una estrella!** ⭐
