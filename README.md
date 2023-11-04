<div align="center">

  <h3 align="center">Django - Proyecto Chat Grupo WebSocket</h3>
  
  [![Django][Django]][Django-url]
  [![Javascript][Javascript.com]][Javascript-url]
  [![Bootstrap][Bootstrap.com]][Bootstrap-url]
  [![HTML5][HTML5.com]][HTML5-url]
  [![CSS3][CSS3.com]][CSS3-url]

  <a href="#"><strong>Ver Demo »</strong></a>

</div>

## Descripción del Proyecto

Este proyecto de Django se ha diseñado para ofrecer una solución de autenticación segura y eficiente que utiliza direcciones de correo electrónico tanto para el registro de nuevos usuarios como para el inicio de sesión. Su principal enfoque es la seguridad de los datos y la experiencia del usuario.

### Requisitos Previos
* **Python**

  Asegúrate de tener Python instalado en tu sistema de preferencia > Python 3.x

  Para verificar qué versión de Python tienes instalada en tu sistema, puedes abrir una terminal y ejecutar el siguiente comando:

  ```sh
  python --version
  ```

  Otra forma de verificar las versiones de Python instaladas en tu sistema es ejecutar:

  ```sh
  python3 --version
  ```

  Si no tienes Python instalado o deseas instalar una versión específica, puedes descargarlo desde el sitio web oficial de Python (https://www.python.org/downloads/) o utilizar un gestor de paquetes como Anaconda o Miniconda para administrar múltiples versiones de Python y entornos virtuales en tu sistema.

* **Git**(opcional)

  Si deseas clonar el repositorio desde GitHub, necesitarás Git. Puedes descargarlo desde el sitio web de Git e instalarlo

  Para verificar si tiene instalado git, puedes abrir una terminal y ejecutar el siguiente comando:
  ```sh
  git
  ```

### Instalación

Sigue estos pasos para instalar y configurar.

1. **Clonar el Repositorio** (opcional):

   Si tienes Git instalado y deseas clonar el repositorio, ejecuta el siguiente comando en tu terminal:
   ```sh
   git clone https://github.com/HenryCCoillo/django-login-registro.git   
   ```
   Si prefieres descargar manualmente el código fuente, puedes hacerlo desde el repositorio de GitHub.

2. **Crear un Entorno Virtual** (opcional pero recomendado):

   Es una buena práctica crear un entorno virtual para tu proyecto para aislar las dependencias. En tu terminal, navega hasta el directorio de tu proyecto (donde se encuentra `requirements.txt`) y ejecuta:
   ```sh
   python -m venv env
   ```

    Luego, activa el entorno virtual:
    
    * En Windows:
      ```sh
      env\Scripts\activate
      ```

    * En macOS y Linux:
      ```sh
      source env/Scripts/activate
      ```
3. **Instalar Dependencias**:

   Asegúrate de estar en el directorio raíz de tu proyecto y utiliza pip para instalar las dependencias del proyecto desde `requirements.txt`:
   ```sh
   pip install -r requirements.txt
   ```
4. **Configurar Variables de Entorno**:

   La aplicación utiliza variables de entorno, crear un archivo `.env` en el directorio raíz del proyecto y definir las variables allí:

   ```sh
   SECRET_KEY=mysecretkey
   DEBUG=True
   ```
5. **Migraciones y Base de Datos**:

   Realiza las migraciones necesarias para configurar la base de datos. Ejecuta los siguientes comandos en tu terminal:
   ```sh
   python manage.py makemigrations chat
   python manage.py migrate
   ```
   
6. **Iniciar la Aplicación**:
  
   Finalmente, puedes iniciar la aplicación con el siguiente comando:
   ```sh
   python manage.py runserver
   ```
   La aplicación estará disponible en **http://127.0.0.1:8000/**. Puedes acceder a ella desde tu navegador web.
   

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- https://simpleicons.org/ -->
[Django]: https://img.shields.io/badge/django-0C4B33?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Bootstrap-url]: https://getbootstrap.com
[Javascript.com]: https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white
[Javascript-url]: https://developer.mozilla.org/es/docs/Web/JavaScript
[HTML5.com]: https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/es/docs/Web/HTML
[CSS3.com]: https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://developer.mozilla.org/es/docs/Web/CSS
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white