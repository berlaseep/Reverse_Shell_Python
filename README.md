# Reverse Shell Python


### Instalación
Para instalar se necesita un editor como vscode o un alguna distribución de linux. No apto para <a href="https://github.com/termux/termux-app">Termux</a>

### Windows
- VSC: Clona el projecto en VSC y sigue las instrucciones de configuración
- Windows: Abre el archivo: Reverse_Shell.py copia su codigo pegalo en el bloc de notas y guardalo como quieras pero que acabe en .py

  ### Linux

 Clona el repositorio

 ```Git
git clone https://github.com/berlaseep/Reverse_Shell_Python.git
```

### Configuración

Cambia la linea 8 y en la parte de la IP 192.168.0.0 por la tuya si no sabes cual es tu IP puedes ejecutar
```Windows
ipconfig
```

```Linux
hostname -I
```

### Ejecutar

### Linux

En linux has de ponerte a la escucha OBLIGATORIAMENTE por el puerto 443

```Linux
nc -nlvp 443
```

### Windows

En windows debes descargar netcat aqui te dejo un video que explica <a href="https://youtu.be/v0ncgMru8q8?si=fqtccAfWZSImM1Ac">Como instalar netcat en windows</a>
una vez echo esto solo ejecuta el comando

```netcat
nc -nlvp 443
```

Una vez ejecutado este comando tanto en Windows como en Linux haz que la victima ejecute el archivo .py y conseguiras una reverse shell.

### AVISO

No me hago cargo de el uso de este archivo para acciones maliciosas
