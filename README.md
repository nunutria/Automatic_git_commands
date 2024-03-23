# Automatic_git_commands

Automatic_git_commands es básicamente un script hecho en python el cual nos permite realizar contribuciones de manera semiautomática para llenar el cuadro de contribuciones de GitHub, teniendo así un hermoso cuadro lleno de contribuciones, sin la necesidad de tener que crear proyectos y demás.  ¿trampa? Si un poco. “Nunca dejes de crear proyectos 🦦”


![Logo](https://docs.github.com/assets/cb-35216/mw-1440/images/help/profile/contributions-graph.webp)


## Como usar

Descargamos el código.

```bash
  git clone https://github.com/nunutria/Automatic_git_commands.git
```

Instalamos plyer

```bash
pip install plyer
```

### Parte engorrosa pero sencilla.

* Necesitamos crear un repositorio en github, preferible iniciar con una Branch principal 'main' puede ser un repositorio privado.

* Ahora el código main.py lo copiamos en la carpeta del repositorio creado.

* En este punto podrás ejecutar el script main.py

* Al ejecutarse:
  * Creará dos archivos
    	
    * registroGitHub.txt: llevar registro de  Commits y archivo que se subirá al repositorio.
    * Contador.bin: Llevara un registro de la cantidad de veces que se ha ejecutado el script.
  * Luego mostrar dos notificaciones para estar al tanto de la operación.

#### Debes tener en cuenta la opción de mostrar las contribuciones de repositorios privados

![Logo](https://docs.github.com/assets/cb-44440/mw-1440/images/help/profile/activity-overview.webp)

* Podrás chequear si se realizó correctamente la contribución observando los Commits del repositorio.

# Listo

Te dejo un exe para que lo puedas usar comodamente desde windows