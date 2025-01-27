DirectoryWarp
======

Este es un proyecto rápido creado para facilitar trabajar en múltiples directorios diferentes de Linux. En esencia es un cd con aliases para guardar directorios.


Instalación
======
Paso 1: Copiar el script a un directorio path
------
Movemos el archivo a un directorio path, ejemplo:
```
sudo cp DirectoryWarp.py /usr/local/bin/dw
```
Paso 2: Añadir alias a la shell
------
Abrimos el archivo, en mi caso zshell:
```
vim ~/.zshrc
```
Y pegamos este bloque de código al final:
```
# DirectoryWarp
function dw() {
    target=$(python3 /usr/local/bin/dw "$@")
    if [ -d "$target" ]; then
        cd "$target"
    else
        echo "$target"
    fi
}
# DirectoryWarp
```
Una vez hecho esto recargamos la shell para que tenga la nueva configuración:
```
source ~/.zshrc
```

Y ya se puede usar

Uso
======

⋅⋅* Guardar directorio
```
dw set mydir
```

⋅⋅* Ir al directorio
```
dw mydir
```

⋅⋅* Listar directorio
```
dw ls
```

⋅⋅* Borrar un warp específico
```
dw rm warp_a_borrar
```

⋅⋅* Borrar todos los warps
```
dw clear
```
Nota: dw clear no tiene confirmación, usar con cuidado

Notas
======
Es necesario tener Python3 instalado
