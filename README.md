# HelloChusquis-Plugins

¡Bienvenido al repositorio oficial de plugins para HelloChusquis!

Este proyecto tiene como objetivo centralizar y facilitar la gestión de plugins para HelloChusquis, permitiendo a los usuarios extender sus funcionalidades de manera sencilla y a los desarrolladores contribuir con nuevas herramientas.

## ¿Qué es HelloChusquis?

HelloChusquis es un asistente virtual o plataforma que interactúa con el usuario a través de comandos o solicitudes. Los plugins son módulos que extienden las capacidades de HelloChusquis, permitiéndole realizar tareas específicas como cálculos, búsquedas de información, conversiones de moneda, etc.

## Instalación de Plugins

Para instalar un plugin en tu instancia de HelloChusquis, generalmente necesitarás:

1.  **Descargar el archivo del plugin**: Puedes obtener los archivos `.py` directamente desde la carpeta `plugins/` de este repositorio.
2.  **Colocar el plugin en el directorio adecuado**: Copia el archivo `.py` del plugin en la carpeta de plugins de tu instalación de HelloChusquis.
3.  **Actualizar el registro de plugins**: Asegúrate de que tu instancia de HelloChusquis reconozca el nuevo plugin. Esto puede implicar actualizar un archivo de configuración o ejecutar un comando de recarga de plugins.

Consulta la documentación oficial de HelloChusquis para obtener instrucciones detalladas sobre cómo integrar plugins.

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
