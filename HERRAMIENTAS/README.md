# Programas del curso

**SI-886 · Planeamiento Estratégico de TI**

Aquí viven los programas que los talleres usan. Están fuera de las guías por una razón. **Transcribir código no es un resultado de aprendizaje del curso.** El resultado es la decisión que el programa calcula y la justificación de las cifras que se le dan.

## Cómo se usan

Cada taller indica qué programa copiar y con qué nombre. La forma es siempre la misma.

```bash
cp ../HERRAMIENTAS/SEMANA-<NN>/<programa>.py <carpeta_del_equipo>/<programa>.py
python3 <carpeta_del_equipo>/<programa>.py
```

**El programa se edita.** Los datos que trae son los de la organización de ejemplo. El equipo los reemplaza por los de la suya, y **cada cifra que introduce debe poder justificarse contra una sección del diagnóstico**. Un peso, una calificación o una estimación sin ese respaldo convierte el cálculo en una opinión con decimales.

## Qué hay aquí

| Semana | Programa | Qué calcula |
|---|---|---|
| 02 | `VS02_extraccion_bcrp.py` · `VS03_extraccion_bm.py` · `VS04_graficos.py` | Series de vigilancia estratégica y sus gráficos |
| 04 | `MV01_diagnostico_declaraciones.py` | Diagnóstico de la misión y la visión de una empresa, con su veredicto |
| 05 | `CU02_perfil_cultura.py` | Perfil de cultura organizacional |
| 06 | `AI02_analisis_cadena.py` · `AI06_capacidades.py` | Cadena de valor y evaluación de capacidades |
| 07 | `PE02_matrices.py` | Matrices EFI y EFE |
| 08 | `NO04_analisis_cumplimiento.py` | Análisis de cumplimiento normativo |
| 09 | `MG02_priorizacion_cobit.py` · `MG04_analisis_capacidad.py` | Factores de diseño de COBIT y brechas de capacidad |
| 10 | `AR03_brechas.py` | Brechas de arquitectura y paquetes de trabajo |
| 11 | `GD02_analisis_servicios.py` · `GD04_madurez.py` | Servicios digitales y su madurez |
| 12 | `OB04_valida_indicadores.py` · `OB05_trazabilidad.py` | Validación de indicadores y trazabilidad |
| 13 | `PF01_consolidacion.py` · `PF02_tco.py` · `PF04_alternativas.py` · `PF05_balance.py` · `PF06_dependencias.py` | Portafolio, costo total, alternativas, balance y dependencias |
| 14 | `PR01_no_negociables.py` · `PR03_priorizacion.py` · `PR04_hoja_ruta.py` · `PR06_presupuesto.py` | Priorización, hoja de ruta y presupuesto |
| 15 | `RG03_evaluacion.py` | Evaluación de riesgos del plan |
| 16 | `AP01_coherencia.py` | Verificación de los siete puntos de coherencia del plan |

> **Requisitos.** Python 3.11 o superior, con `pandas` y `matplotlib`. Se instalan en la Semana 01.
