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

---

## Preguntas finales

Respuesta a cada pregunta basado en el contexto del script de prueba funcional:

## ¿Qué tipo de errores podrías detectar con esta prueba funcional?

### Errores de Funcionalidad

- **Campo de búsqueda no funciona:** Si el input no acepta texto o no procesa la búsqueda
- **Botón de búsqueda roto:** Si el formulario no se envía correctamente
- **Resultados no se cargan:** Si la página no muestra resultados después de la búsqueda
- **Enlaces rotos:** Si los resultados no llevan a páginas válidas

### Errores de Interfaz (UI)

- **Elementos desplazados:** Si el campo de búsqueda no está visible
- **Cambios en selectores:** Como pasó en tu caso con .result vs [data-testid='result']
- **CSS roto:** Si los elementos no se renderizan correctamente
- **Responsive issues:** Si la página no funciona en diferentes resoluciones

### Errores de Rendimiento

- **Carga lenta:** Si los elementos tardan más del timeout esperado
- **JavaScript no ejecuta:** Si componentes dinámicos no cargan
- **Memory leaks:** Si la página consume demasiada memoria

### Errores de Integración

- **APIs fallando:** Si la búsqueda depende de servicios externos
- **Base de datos desconectada:** Si no hay conexión con el backend
- **CDN problemas:** Si recursos externos no cargan

### Errores de Compatibilidad

- **Navegador específico:** Comportamiento diferente entre Chrome/Firefox/Safari
- **Versiones del navegador:** Funciones no soportadas en versiones antiguas
- **Sistema operativo:** Diferencias entre Windows/Linux/macOS

---

## ¿Por qué es importante automatizar pruebas desde la perspectiva del usuario?

### Validación de Experiencia Real

- **Flujo completo:** Simula exactamente lo que hace un usuario real
- **Interacciones complejas:** Clicks, scroll, formularios, navegación
- **Casos edge:** Situaciones que los desarrolladores no consideraron

### Eficiencia y Escalabilidad

```python
# Manual: 1 tester, 1 navegador, 8 horas/día
# Automatizado: N tests, N navegadores, 24/7
def test_multiple_browsers():
    browsers = ['chrome', 'firefox', 'safari', 'edge']
    for browser in browsers:
        run_test_suite(browser)  # Imposible manual
```

### Consistencia

- **Mismos pasos:** Elimina variabilidad humana
- **Mismos datos:** Usa datasets controlados
- **Misma velocidad:** Timing predecible

### Detección Temprana

- En CI/CD pipeline
- Detecta errores de código
- Detecta errores de UX

### ROI (Return on Investment)

- **Costo inicial alto:** Desarrollo de scripts
- **Costo continuo bajo:** Ejecución automática
- **Ahorro a largo plazo:** Menos bugs en producción

### Regresión Prevention

- Cada deploy ejecuta TODAS las pruebas anteriores

### Documentación Viva

- Los tests actúan como documentación ejecutable
- Muestran cómo debería funcionar el sistema
- Se mantienen actualizados automáticamente

---

## ¿Qué limitaciones tiene Selenium y cómo las superarías?

- **Limitación 1:** Rendimiento y Velocidad
- **Solución:** Combinación de herramientas
- **Limitación 2:** Mantenimiento de Selectores
- **Solución:** Page Object Model
- **Limitación 3:** Aplicaciones SPA y JavaScript Pesado
- **Solución:** Esperas inteligentes
- **Limitación 4:** Escalabilidad
- **Solución:** Selenium Grid + Docker
- **Limitación 5:** Código paralelo
- **Solución:** Appium + Device Farm
- **Limitación 6:** Captcha y Sistemas Anti-Bot
- **Solución:** Técnicas de evasión

- Estrategia Integral para Superar Limitaciones

```python
class ModernTestFramework:
    def __init__(self):
        self.api_client = APIClient()
        self.selenium_driver = None
        self.playwright_browser = None
    
    def test_feature_complete(self):
        # 1. API testing (rápido)
        self.api_client.test_search_endpoint()
        
        # 2. Visual testing (componentes)
        self.playwright_browser.screenshot_compare()
        
        # 3. E2E critical path (Selenium)
        self.selenium_driver.test_user_journey()
        
        # 4. Performance testing
        lighthouse_score = self.run_lighthouse_audit()
        
        # 5. Accessibility testing
        axe_results = self.run_axe_core()
        
        return all([api_ok, visual_ok, e2e_ok, perf_ok, a11y_ok])
```

---

## Herramientas Complementarias

- **Playwright:** Más rápido, mejor para SPAs
- **Cypress:** Mejor experiencia de desarrollo
- **Puppeteer:** Control fino de Chrome
- **TestCafe:** Sin WebDriver, más estable
- **Postman/Newman:** API testing
- **k6:** Performance testing

En resumen, Selenium sigue siendo valioso pero debe usarse estratégicamente, combinado con otras herramientas y técnicas modernas para crear una suite de testing robusta y eficiente.

---

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
