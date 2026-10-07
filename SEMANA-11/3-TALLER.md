[Semana 11](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Taller de laboratorio 11 · Diagnóstico de gobierno digital y tablero de línea base

**SI-886 · Planeamiento Estratégico de TI** · Semana 11 · Sesión 2 en laboratorio · 100 min · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Secuencia del taller

```mermaid
flowchart TD
    PA["<b>Paso A</b><br/>Catálogo de servicios y su<br/>nivel de digitalización<br/><i>15 min</i>"]
    PB["<b>Paso B</b><br/>Diagnóstico de los ocho ejes<br/>con línea base<br/><i>20 min</i>"]
    PC["<b>Paso C</b><br/>Tablero de línea base en<br/>Metabase<br/><i>15 min</i>"]
    PD["<b>Paso D</b><br/>Redactar la Sección 6.1<br/><i>10 min</i>"]
    PE["<b>Paso E</b><br/>Validar y corregir<br/><i>25 min</i>"]
    PF["<b>Paso F</b><br/>Registrar y cerrar<br/><i>15 min</i>"]
    PA --> PB --> PC --> PD --> PE --> PF
    classDef paso fill:#E8F1FB,stroke:#16285C,stroke-width:1px,color:#16285C;
    class PA,PB,PC,PD,PE,PF paso;
```

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S11-TALLER-Grupo<N>.pdf` |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La **5. Resultados y evidencias** se califica contra la tabla de resultados esperados de esta guía, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 11» |
| **Cuándo vence** | 48 horas después de la sesión de laboratorio |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## El reto

| | |
|---|---|
| **Situación** | La organización cree que está digitalizada porque tiene una web. Hay que medir en qué nivel está de verdad cada servicio. |
| **Misión** | Levantar el catálogo de servicios con su nivel de digitalización y evaluar los ocho ejes del gobierno digital con evidencia. |
| **Criterio de éxito** | Cada nivel declarado se sostiene con una prueba de que el servicio funciona así, y no con lo que dice el portal. |

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Levantar el **catálogo de servicios** de la organización con su nivel de digitalización.
- Evaluar los **ocho ejes** del gobierno digital con evidencia.
- Establecer la **línea base** de cada indicador, o declarar explícitamente que no se mide.
- Determinar el **nivel de madurez de gobierno digital** de la organización.
- Aplicar la prueba del **principio de una sola vez** al catálogo de servicios.
- Construir el **tablero de línea base** en Metabase.
- Redactar la **Sección 6.1** del PETI (Plan Estratégico de Tecnologías de Información).

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **RSGD 005-2018-PCM/SEGDI**, Anexo I | https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf |
| **D. S. 029-2021-PCM** y **D. S. 085-2023-PCM** | Componentes del gobierno digital y objetivos de la política |
| **Estándares de Interoperabilidad de la PIDE** | https://www.peru.gob.pe/normas/docs/Estandares_Interoperabilidad_PIDE_SEGDI.pdf |
| **Metabase** (Docker) | https://www.metabase.com/ |
| **PostgreSQL** (Docker) | Base del tablero |
| **Python 3.11+** con `pandas`, `matplotlib` | Cálculo de indicadores |
| Secciones Sección 4.1, Sección 4.3 y Sección 5 del PETI | Insumos del diagnóstico |

### 1.3. Seguridad

1. El catálogo de servicios y sus volúmenes son información **Confidencial** de la organización.
2. El tablero se despliega **en local** (`127.0.0.1`) con datos agregados; no se cargan datos personales de usuarios.
3. Los indicadores de seguridad digital revelan debilidades. Se reportan por nivel, sin detalle técnico explotable.
4. Si se observa el recorrido de un usuario real, se obtiene su **consentimiento** y no se registran sus datos personales.

---

## 2. Procedimiento o Metodología

> **Documento del caso para esta semana.** La organización entrega **Cuestionario de diagnóstico de la organización**, en `CASOS/EMPRESA-<NN>-<slug>/documentos/cuestionario-diagnostico.md`. Es consistente con los datos de `datos/`. Las personas, usuarios y proveedores que menciona existen en los archivos. **No señala sus debilidades**; declara lo que la organización dice hacer.

### Paso A — Catálogo de servicios y su nivel de digitalización

`06_gobierno_digital/GD01_catalogo_servicios.csv`:

| id | Servicio | Usuario destinatario | Volumen anual | **Nivel actual (0–5)** | Canales | Tiempo de atención | Documentos solicitados | **De ellos, ya en poder de la organización** | Sistemas que lo soportan | ¿Trata datos personales? | Nivel objetivo | Justificación del objetivo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S-01 | Registro de pedido | Cliente (bodega) | 74 400 | **1** | Teléfono, vendedor, portal (4 %) | 15 min | 0 | 0 | Portal, ERP | Sí | **4** | Es el servicio de mayor volumen; la visión exige 80 % digital |
| S-02 | Consulta de estado de pedido | Cliente | 22 000 | **0** | Teléfono al vendedor | 5 min | 0 | 0 | Ninguno | No | **4** | Elimina 22 000 llamadas anuales |
| S-03 | Solicitud de línea de crédito | Cliente | 320 | **2** | Formulario en papel | 5 días | 4 | **2** (RUC y ficha ya registrados) | ERP | Sí | **3** | Requiere evaluación humana |
| S-04 | Reclamo o devolución | Cliente | 180 | **1** | Teléfono, correo | 48 h | 2 | 1 | Correo | Sí | **4** | Trazabilidad exigida por el diagnóstico |
| S-05 | Descarga de comprobante | Cliente | 74 400 | **2** | Correo bajo pedido | 24 h | 0 | 0 | ERP | Sí | **4** | Autoservicio inmediato |
| S-06 | Solicitud de vacaciones | Trabajador | 130 | **0** | Papel | 3 días | 1 | **1** | Ninguno | Sí | **4** | Interno, esfuerzo bajo |
| S-07 | Consulta de boleta de pago | Trabajador | 768 | **2** | Impresa | Mensual | 0 | 0 | Planilla | Sí, sensibles | **4** | Reduce carga administrativa |

**El programa está en [`HERRAMIENTAS/SEMANA-11/GD02_analisis_servicios.py`](../HERRAMIENTAS/SEMANA-11/GD02_analisis_servicios.py).** Se copia al repositorio del equipo como `06_gobierno_digital/GD02_analisis_servicios.py` y **se edita con los datos de su organización**. El programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
cp ../HERRAMIENTAS/SEMANA-11/GD02_analisis_servicios.py 06_gobierno_digital/GD02_analisis_servicios.py
python3 06_gobierno_digital/GD02_analisis_servicios.py
```

### Paso B — Diagnóstico de los ocho ejes con línea base

`06_gobierno_digital/GD03_ejes.csv`:

| Eje | Indicador | **Línea base** | Fuente y fecha del dato | Evidencia | Nivel del eje (1–5) | Observación |
|---|---|---|---|---|---|---|
| 1. Gobernanza | ¿Existe comité de TI o de gobierno digital? | **No** | Entrevista y revisión de actas, a la fecha de corte | Sin actas | 1 | — |
| 1. Gobernanza | ¿Existe plan de TI vigente? | **No** | Documental | — | 1 | Este PETI será el primero |
| 2. Servicios | Nivel medio ponderado de digitalización | **1,2 de 5** | `GD02` | Catálogo | 2 | — |
| 2. Servicios | % de transacciones por canal digital | **4 %** | Registro del portal, a la fecha de corte | Reporte | 1 | — |
| 3. Interoperabilidad | N.º de integraciones activas | **1** (ERP↔WMS por archivo plano) | Sección 5.2.3 | Modelo de arquitectura | 1 | — |
| 3. Interoperabilidad | Documentos solicitados que ya poseemos | **3 de 7** | `GD02` | Catálogo | 2 | — |
| 4. Seguridad digital | ¿Existe SGSI (Sistema de Gestión de Seguridad de la Información)? | **No** | Sección 4.1, Sección 4.3 | Matriz de cumplimiento | 1 | Obligación normativa pendiente |
| 4. Seguridad digital | Incidentes registrados en 12 meses | **3** | Registro | — | 1 | **Cifra anormalmente baja.** No se registran |
| 4. Seguridad digital | % de sistemas con restauración probada | **0 %** | Entrevista; sin prueba de restauración en más de dos años | — | 1 | — |
| 5. Datos | Entidades con dueño designado | **0 de 6** | Sección 5.2.2 | Estructura de información | 1 | — |
| 5. Datos | % de decisiones con dato verificable | **No se mide** | — | — | 1 | **Primer proyecto: empezar a medir** |
| 6. Identidad digital | ¿Identidad única de usuario? | **No** | Inventario de accesos | — | 1 | Cuentas por sistema, sin correspondencia |
| 6. Identidad digital | ¿Segundo factor de autenticación? | **No** | — | — | 1 | — |
| 7. Talento | % de personal capacitado en TI en 12 meses | **8 %** | RR. HH., último ejercicio | Registro de capacitación | 2 | — |
| 7. Talento | Perfil cultural dominante | **Jerarquía (42)** | Sección 2.4 | Diagnóstico CVF | — | Condiciona la implantación |
| 8. Infraestructura | Disponibilidad de servicios críticos | **No se mide** | — | — | 1 | **Primer proyecto: instrumentar** |
| 8. Infraestructura | % de equipos dentro de soporte | **66 %** | Inventario | — | 2 | Servidor del ERP fuera de soporte |

**El programa está en [`HERRAMIENTAS/SEMANA-11/GD04_madurez.py`](../HERRAMIENTAS/SEMANA-11/GD04_madurez.py).** Se copia al repositorio del equipo como `06_gobierno_digital/GD04_madurez.py` y **se edita con los datos de su organización**. El programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
cp ../HERRAMIENTAS/SEMANA-11/GD04_madurez.py 06_gobierno_digital/GD04_madurez.py
python3 06_gobierno_digital/GD04_madurez.py
```

### Paso C — Tablero de línea base en Metabase

```bash
docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab \
  -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 postgres:16

docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 \
  -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5432 \
  -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal \
  metabase/metabase
```

```python
# 06_gobierno_digital/GD05_carga_tablero.py
import pandas as pd
from sqlalchemy import create_engine

eng = create_engine("postgresql://peti:peti_lab@127.0.0.1:5433/peti")
pd.read_csv("GD01_catalogo_servicios.csv").to_sql("servicios", eng, if_exists="replace", index=False)
pd.read_csv("GD03_ejes.csv").to_sql("ejes_gd", eng, if_exists="replace", index=False)
pd.read_csv("../04_normativa/NO03_matriz_cumplimiento.csv").to_sql("cumplimiento", eng, if_exists="replace", index=False)
pd.read_csv("../04_normativa/MG03_capacidad.csv").to_sql("capacidad", eng, if_exists="replace", index=False)
print("Datos cargados. Metabase: http://127.0.0.1:3001")
```

**Tableros mínimos a construir en Metabase.**

| Tablero | Visualización | Pregunta que responde |
|---|---|---|
| Nivel de digitalización por servicio | Barras horizontales | ¿Qué servicios están más atrasados? |
| Nivel ponderado por volumen | Número grande | ¿Qué proporción de las atenciones es realmente digital? |
| Madurez por eje | Radar o barras | ¿Dónde está la mayor brecha de gobierno digital? |
| Estado de cumplimiento normativo | Anillo | ¿Cuántas obligaciones se incumplen? |
| Capacidad de procesos actual vs. objetivo | Barras agrupadas | ¿Qué procesos exigen mayor esfuerzo? |
| **Indicadores sin línea base** | Tabla | ¿Qué necesitamos empezar a medir? |

> **Este tablero es el punto de partida de la sección 10 Supervisión.** Los mismos indicadores, con sus metas de sección 6.2, se monitorearán durante la ejecución del plan.

### Paso D — Redactar la Sección 6.1

```markdown
## 6.1 Situación actual del gobierno digital

### 6.1.1 Marco conceptual y alcance
Los seis componentes del gobierno digital aplicados a la organización, con su
equivalencia si es privada.

### 6.1.2 Catálogo de servicios y su nivel de digitalización
Tabla del catálogo · **nivel medio simple y ponderado por volumen**.

### 6.1.3 Aplicación del principio de una sola vez
Documentos solicitados que la organización ya posee y su proporción.

### 6.1.4 Diagnóstico por eje
Los ocho ejes con indicador, línea base, fuente y nivel.

### 6.1.5 Indicadores sin línea base
Listado y proyectos de instrumentación asociados.
**Sin línea base no puede fijarse meta ni demostrarse avance.**

### 6.1.6 Nivel de madurez del gobierno digital
Nivel obtenido, radar y posicionamiento en el modelo de cinco niveles.

### 6.1.7 Síntesis · las brechas de mayor impacto
Servicios de mayor brecha ponderada por volumen y ejes de menor nivel.
**Esta síntesis es el insumo directo de los objetivos (Sección 6.2).**
```

### Paso E — Validar y corregir (25 min)

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Recorrer dos servicios de principio a fin y comprobar que el nivel declarado es el real.
2. Verificar que cada eje evaluado trae la evidencia que sostiene su puntaje.
3. Comprobar que el principio de «una sola vez» se evaluó sobre documentos concretos.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso F — Registrar la evidencia y cerrar (15 min)

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S11: diagnostico de gobierno digital, catalogo de servicios y linea base — seccion 6.1"
git tag -a v0.11 -m "PETI v0.11 — situacion actual del gobierno digital"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Código y archivos de configuración | Rama del taller, fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | `docs/`, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `docs/evidencias/S11/` | URL del archivo |
> | Salida de comandos | `docs/evidencias/S11/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-11` sobre el commit entregado:
>
> ```bash
> git tag -a taller-11 -m "Taller 11 · SI886"
> git push origin taller-11
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-11`
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **El catálogo con niveles** | Cada servicio con su nivel comprobado, no declarado | Catálogo de servicios |
| **Los ocho ejes con evidencia** | Cada puntaje con la prueba que lo sostiene | Tablero de línea base |
| **La línea base del plan** | Las cifras de partida contra las que se medirá el avance | Sección 5.1 |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | Catálogo con **≥ 7 servicios**, cada uno con volumen anual y nivel de digitalización | `GD01_catalogo_servicios.csv` |
| 2 | **Nivel medio ponderado por volumen** calculado y contrastado con el promedio simple | Salida de `GD02_analisis_servicios.py` |
| 3 | Prueba del **principio de una sola vez**. Documentos redundantes contados | Salida del script |
| 4 | Brecha por servicio ponderada por volumen, con los 5 de mayor impacto | Salida del script |
| 5 | Gráfico del catálogo con nivel actual y objetivo | `GD_servicios.png` |
| 6 | Los **ocho ejes** evaluados, con al menos dos indicadores cada uno | `GD03_ejes.csv` |
| 7 | **Línea base declarada** en cada indicador, o «no se mide» explícito | Misma tabla |
| 8 | **Indicadores sin línea base identificados y contados**, con su proyecto de instrumentación | Salida de `GD04_madurez.py` |
| 9 | Nivel de madurez de gobierno digital calculado y posicionado en el modelo | Salida del script |
| 10 | Radar de madurez por eje | `GD_madurez.png` |
| 11 | Tablero en Metabase con **al menos 6 visualizaciones** | Capturas |
| 12 | Sección 6.1 redactada, con la síntesis de brechas de mayor impacto | `6.1_situacion_actual.md` |
| 13 | Etiqueta `v0.11` en Git | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **El catálogo con niveles** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **Los ocho ejes con evidencia** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La línea base del plan** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

| Puntaje | Equivalencia |
|---|---|
| 18 – 20 | Destacado |
| 14 – 17 | Logrado |
| 6 – 13 | En proceso |
| 0 – 5 | Insuficiente |

> **Un resultado declarado sin evidencia enlazada no se califica**, aunque el trabajo se haya hecho. La tabla de la sección 3.1 es la lista de cotejo; esta rúbrica es lo que determina la nota.

## 4. Conclusiones

Mínimo tres. Líneas argumentales esperadas:

1. El nivel de digitalización ponderado por volumen es el indicador que importa. El promedio simple sobrevalora el avance cuando los servicios de mayor volumen son los menos digitalizados, que es el caso más frecuente.
2. Un indicador sin línea base no puede sostener una meta ni demostrar avance; el primer proyecto asociado a esos indicadores no es mejorarlos sino empezar a medirlos.
3. Gobierno digital no es cantidad de sistemas sino capacidad del usuario de completar el servicio sin cambiar de canal; medir sistemas en lugar de servicios produce un diagnóstico que no refleja la experiencia real.

## 5. Referencias Bibliográficas

- Decreto Legislativo 1412, Ley de Gobierno Digital. https://www.gob.pe/institucion/pcm/colecciones/147-normativa-sobre-gobierno-digital
- Decreto Supremo 029-2021-PCM, Reglamento de la Ley de Gobierno Digital. https://www.gob.pe/13326-reglamento-de-la-ley-de-gobierno-digital
- Decreto Supremo 085-2023-PCM, Política Nacional de Transformación Digital al 2030. https://busquedas.elperuano.pe/dispositivo/NL/2200457-5
- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — Lineamientos del PGD (Plan de Gobierno Digital). https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- Estándares de Interoperabilidad de la PIDE. https://www.peru.gob.pe/normas/docs/Estandares_Interoperabilidad_PIDE_SEGDI.pdf
- Presidencia del Consejo de Ministros. *Transformación digital en el Perú*. https://www.gob.pe/transformaciondigital
- OCDE. *Digital Government Policy Framework*. https://www.oecd.org/governance/digital-government/
- Rodríguez Bermúdez, J. R. (2015). *Usos estratégicos de las TIC*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57677
- Metabase. *Metabase Documentation*. https://www.metabase.com/docs/latest/

## 6. Anexos

- `anexo_A_catalogo_servicios.xlsx`
- `anexo_B_diagnostico_ejes.xlsx`
- `anexo_C_madurez_gobierno_digital.png`
- `anexo_D_tablero_metabase.pdf` — capturas de las visualizaciones
- `anexo_E_recorrido_usuario.pdf` — el de la dinámica de aula
- `anexo_F_seccion_6_1.pdf`

---

---

[Semana 11](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
