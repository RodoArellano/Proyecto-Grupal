https://www.netmentor.es/entrada/crear-diagramas-github

## Verificacion URL remota

```
git remote -v
```

## Chequeo de status del working directory

```
git status
```

## Agregar cambios locales al stage

```
git add .
```

## Creacion de commit

```
git commit -m 'Mensaje'
```

## Formato de commit

```
<tipo-de-commit>[scope]: <descripcion>
```
Ejemplo:
```
docs: add git_command file
```

#Tipos de commit

feat: Una nueva característica/funcionalidad
fix: Arregla un bug
perf: Cambios que mejoran el rendimiento
docs: Cambios en la documentación.
refactor: Refactorización del código como cambios de nombre de variables o funciones.
style: Cambios de formato, tabulaciones, espacios o puntos y coma, etc; no afectan al usuario.
test: Añade tests o refactoriza uno existente.

## Cambio de nombre de rama de Master a Main si no se crea como main

```
git branch -m master main
```

## Primer Push

```
git push --set-upstream origin main
```

En caso de que aparezca algo como lo siguiente
```
origin  git@github.com:RoNovau/Proyecto-Grupal (fetch)
origin  git@github.com:RoNovau/Proyecto-Grupal (push)
```
quiere decir que hay que hacer un fetch (buscar y traer cambios)
```
git fetch origin main
```
```
git push origin main
```

## Luego del primer push solo basta con utilizar el push de la siguiente forma

```
git push
```


## Creacion de una nueva rama

```
git branch nombre_rama
```

##Posicionarse sobre cierta rama

```
git checkout nombre_rama
```

## Chequeo de ramas

```
git branch
```

## Eliminamos la rama X en local

```
git branch -d nombre_rama
```

## Para saber los branch en remoto

```
git branch -a
```

## Para eliminar el branch en remoto

```
git push origin -d branch_X
```

## Pushear cambios a la nueva rama (luego de pushear se vera reflejado en local y en remoto)

```
git add .
git commit -m 'mensaje'
git push --set-upstream origin nombre_rama
```

## Para actualizar tu repositorio local al commit más nuevo

```
git pull
```

# Traigo los cambios de main para colocarlos en mi rama asi la mantenngo actualizada

- Busco cambios

```
git fetch
```

Traigo cambios

```
git pull origin main
```

## Pull Request para trabajo colaborativo

![image](https://github.com/RoNovau/Proyecto-Grupal/assets/110843380/949e1057-fc23-4dbb-8783-7b387fe4893d)

## Revisar un pull request

![image](https://github.com/RoNovau/Proyecto-Grupal/assets/110843380/dcf96714-b3dc-4c8c-b77e-f2ecc2386be3)

## Mergear una vez aceptado

![image](https://github.com/RoNovau/Proyecto-Grupal/assets/110843380/671785e4-8a53-4902-81d3-cfa3dce426ed)
