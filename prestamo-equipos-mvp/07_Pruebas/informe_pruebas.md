# Informe de Pruebas

**Fecha de ejecución:** *[27/06/08]*
**Responsable:** *[Developer: Santiago Jimenez]*

---

## 1. Estrategia de pruebas

Se combinaron dos enfoques:

- **Pruebas automatizadas** con el módulo `unittest` de la librería estándar,
  centradas en la lógica de negocio (equipos, estudiantes, préstamos y
  devoluciones), incluyendo casos válidos y de error.
- **Pruebas manuales** por consola, ejecutando el menú completo para verificar
  la interacción con el usuario y el formato de salida.

Las pruebas automatizadas usan una **carpeta de datos temporal**, por lo que no
alteran los archivos JSON reales del proyecto.

---

## 2. Ejecución de las pruebas automatizadas

Comando ejecutado desde `09_Codigo/`:

```bash
python -m unittest discover -s tests -v
```

### Resultado

![image-20260827234212245](/home/camper/.config/Typora/typora-user-images/image-20260827234212245.png)

**Total:** 10 pruebas · **Exitosas:** 10 · **Fallidas:** 0

## 3. Resumen de resultados

| Tipo de prueba | Casos | Exitosos | Fallidos |
|----------------|:-----:|:--------:|:--------:|
| Automatizadas | 10 | 10 | 0 |
| Manuales por consola     | 10 | 10 | 0 |

**Conclusión:** todas las historias de usuario cumplen sus criterios de
aceptación. No se detectaron defectos abiertos al cierre del Sprint.

Ver el detalle de cada caso en [`casos_prueba.md`](casos_prueba.md).
