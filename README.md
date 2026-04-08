# HelloChusquis-Plugins

¡Bienvenido al repositorio oficial de plugins para HelloChusquis!

Este proyecto tiene como objetivo centralizar y facilitar la gestión de plugins para HelloChusquis, permitiendo a los usuarios extender sus funcionalidades de manera sencilla y a los desarrolladores contribuir con nuevas herramientas.

## ¿Qué es HelloChusquis?

HelloChusquis es un asistente virtual o plataforma que interactúa con el usuario a través de comandos o solicitudes. Los plugins son módulos que extienden las capacidades de HelloChusquis, permitiéndole realizar tareas específicas como cálculos, búsquedas de información, conversiones de moneda, etc.

## Instalación de Plugins

Para instalar un plugin en tu instancia de HelloChusquis, simplemente abre tu terminal y ejecuta el siguiente comando:

```bash
hellochusquis install <nombre_del_plugin>
```

Este comando se encargará automáticamente de descargar el plugin y configurarlo en tu entorno de HelloChusquis. Asegúrate de reemplazar `<nombre_del_plugin>` con el nombre real del plugin que deseas instalar (por ejemplo, `calculator`, `wikipedia`, etc.).

## Creación de Nuevos Plugins

Crear un nuevo plugin para HelloChusquis es un proceso sencillo. Cada plugin debe seguir una estructura específica para ser compatible con la plataforma.

### Estructura del Plugin

Cada archivo `.py` de un plugin debe contener las siguientes variables y función:

```python
PLUGIN_NAME = "nombre_del_plugin"
PLUGIN_DESCRIPTION = "Una breve descripción de lo que hace el plugin."
PLUGIN_SCHEMA = {
    "type": "function",
    "function": {
        "name": "nombre_de_la_funcion_a_llamar",
        "description": PLUGIN_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": {
                # Define aquí los parámetros que tu función `run` espera
                "parametro1": {"type": "string", "description": "Descripción del parametro1"},
                "parametro2": {"type": "number", "description": "Descripción del parametro2"}
            },
            "required": ["parametro1"]
        }
    }
}

def run(...) -> str:
    # Implementa aquí la lógica de tu plugin.
    # La función `run` debe aceptar los parámetros definidos en PLUGIN_SCHEMA.
    # Debe devolver un string con el resultado de la operación.
    pass
```

-   **`PLUGIN_NAME`**: Un identificador único para tu plugin.
-   **`PLUGIN_DESCRIPTION`**: Una descripción concisa de la funcionalidad del plugin.
-   **`PLUGIN_SCHEMA`**: Un diccionario que define la interfaz del plugin, incluyendo el nombre de la función a invocar y los parámetros que acepta, siguiendo el formato de esquema de funciones.
-   **`run(...)`**: La función principal del plugin que ejecuta la lógica. Debe aceptar los parámetros definidos en `PLUGIN_SCHEMA` y devolver un `str`.

### Ejemplo Básico

Consulta los plugins existentes en la carpeta `plugins/` para ver ejemplos prácticos de implementación.

## Plugins Disponibles

Aquí tienes una lista de los plugins actualmente disponibles en este repositorio:

| Plugin      | Descripción                                                              |
| :---------- | :----------------------------------------------------------------------- |
| `calculator`  | Realiza operaciones aritméticas básicas como suma, resta, multiplicación y división. |
| `wikipedia`   | Busca información en Wikipedia y devuelve un resumen.                    |
| `currency`    | Convierte una cantidad de una moneda a otra utilizando tasas de cambio actuales. |
| `news`        | Obtiene las últimas noticias de una categoría o palabra clave específica. |
| `sysinfo`     | Obtiene información básica del sistema operativo y hardware.             |
| `spotify`     | Controla la reproducción de Spotify y busca contenido.                   |
| `translator`  | Traduce texto entre diferentes idiomas, detectando el idioma de origen automáticamente. |
| `filemanager` | Gestiona archivos y directorios en el sistema de archivos (leer, escribir, listar, crear, borrar, renombrar). |
| `git`         | Asistente para operaciones básicas de Git (status, add, commit, push, pull, branch, log). |
| `youtube`     | Busca videos en YouTube, obtiene información y descarga audio o enlaces. |
| `crypto`      | Obtiene precios de criptomonedas en tiempo real.                         |
| `stocks`      | Obtiene precios de acciones y datos de bolsa en tiempo real.             |
| `todo`        | Gestiona una lista de tareas persistente (añadir, listar, completar, eliminar). |
| `shell`       | Ejecuta comandos de shell de forma segura en el sistema.                 |
| `qr`          | Genera códigos QR a partir de texto o URLs.                              |
| `password`    | Genera contraseñas seguras y personalizables.                           |
| `unit`        | Convierte unidades de peso, longitud, temperatura, volumen, etc.         |
| `joke`        | Cuenta chistes aleatorios en español.                                    |
| `ip`          | Obtiene información de la IP pública y geolocalización.                 |
| `calendar`    | Gestiona fechas, horas, recordatorios y eventos.                         |


## Cómo Contribuir

¡Nos encantaría que contribuyeras a este proyecto! Si tienes una idea para un nuevo plugin, una mejora para uno existente o encuentras un error, por favor, sigue estos pasos:

1.  **Haz un Fork del Repositorio**: Crea una copia del repositorio en tu cuenta de GitHub.
2.  **Clona tu Fork**: Clona el repositorio a tu máquina local.
    ```bash
    git clone https://github.com/TU_USUARIO/HelloChusquis-Plugins.git
    ```
3.  **Crea una Nueva Rama**: Crea una rama para tu nueva característica o corrección de error.
    ```bash
    git checkout -b feature/nombre-de-tu-feature
    ```
4.  **Realiza tus Cambios**: Implementa tu plugin o realiza las modificaciones necesarias.
5.  **Añade y Haz Commit de tus Cambios**: Añade los archivos modificados y haz un commit con un mensaje claro.
    ```bash
    git add .
    git commit -m "feat: Añade el plugin de [nombre]"
    ```
6.  **Sube tus Cambios**: Sube tu rama a tu repositorio fork.
    ```bash
    git push origin feature/nombre-de-tu-feature
    ```
7.  **Abre un Pull Request**: Ve a la página de GitHub de tu repositorio fork y abre un Pull Request hacia el repositorio original `aminoy77/HelloChusquis-plugins`. Describe tus cambios detalladamente.

¡Gracias por tu contribución!

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
