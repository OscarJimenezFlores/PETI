[Semana 01](README.md) · **Teoría** · [Dinámica de aula](2-DINAMICA.md) · [Taller de laboratorio](3-TALLER.md)

# Teoría · Inducción y Lineamientos Generales del Curso

**SI-886 · Planeamiento Estratégico de TI** · Semana 01 · Sesión 1 en aula · 2 h, con la dinámica incluida

---

## Qué se trabaja en esta sesión

- El encargo del semestre.
- Qué es un PETI y qué no es.
- De dónde viene y hacia dónde va el planeamiento.
- La organización objeto de estudio.

## Mapa de la sesión

```mermaid
flowchart TD
    OR["Organización real<br/>elegida por el equipo"]
    PETI["Plan Estratégico de TI"]
    Q1["No es un catálogo de compras"]
    Q2["No es un plan operativo anual"]
    Q3["Es la decisión de qué capacidades<br/>de TI necesita el negocio"]
    S["17 secciones, una por semana"]
    REP["Repositorio con control de versiones"]
    OR --> PETI
    PETI --> Q1
    PETI --> Q2
    PETI --> Q3
    Q3 --> S --> REP
    class PETI nucleo
    class OR,Q3,S concepto
    class Q1,Q2 alerta
    class REP producto
    classDef nucleo fill:#16285C,stroke:#16285C,stroke-width:1px,color:#FFFFFF;
    classDef concepto fill:#E8F1FB,stroke:#16285C,stroke-width:1px,color:#16285C;
    classDef producto fill:#E9F6F2,stroke:#0F766E,stroke-width:1px,color:#0F4C46;
    classDef alerta fill:#FDF2E2,stroke:#B45309,stroke-width:1px,color:#7C3E00;
```

---

## El encargo del semestre (20 min)

**El curso no es una asignatura sobre planeamiento: es un encargo de consultoría.** Al terminar el semestre cada equipo entrega a una organización real un **Plan Estratégico de Tecnologías de Información completo**, con su portafolio de proyectos priorizado y su hoja de ruta.

| Unidad | Semanas | Producto acumulado |
|---|---|---|
| I | 1–6 | **Identidad estratégica y diagnóstico base**: misión, visión, valores, cultura, análisis interno y externo |
| II | 7–12 | **Diagnóstico estratégico completo**: FODA cruzado, marco normativo, marcos de gestión, arquitectura empresarial, objetivos de gobierno digital |
| III | 13–17 | **Plan ejecutable**: portafolio priorizado, riesgos, hoja de ruta, implementación y supervisión |

**Regla estructural del curso:** cada laboratorio produce **una sección del documento final**. No hay trabajo que se descarte. En la Semana 17 el PETI está terminado porque se construyó semana a semana, no porque se escribió al final.

## Qué es un PETI y qué no es (30 min)

**Definición operativa.** El Plan Estratégico de Tecnologías de Información es el instrumento que traduce la estrategia de una organización en **decisiones sobre tecnología, información, personas y procesos**, con un horizonte de tres a cinco años, un portafolio de inversiones priorizado y una forma de medir si funcionó.

| **Un PETI ES** | **Un PETI NO ES** |
|---|---|
| Un instrumento de **decisión de inversión** | Un catálogo de tecnologías de moda |
| Derivado de la estrategia del negocio | Un documento redactado por TI para TI |
| Un portafolio **priorizado** con criterios explícitos | Una lista de deseos del área de sistemas |
| Un compromiso con recursos, plazos y responsables | Una declaración de intenciones |
| Un documento **vivo**, revisado anualmente | Un archivo que se abre cuando lo pide el auditor |
| Medible: cada objetivo tiene indicador y meta | Una narrativa sin cifras |
| Explícito sobre **lo que no se hará** | Un documento que promete todo |

**La prueba de fuego de un PETI.** Si al leerlo un gerente que no es de TI **no puede responder «¿qué gana la empresa con esto y cuándo?»**, el documento fracasó, con independencia de su extensión y de su calidad técnica.

**Los cinco defectos que matan un PETI**, observados sistemáticamente en la práctica:

| Defecto | Cómo se reconoce | Consecuencia |
|---|---|---|
| **Desconexión estratégica** | Los objetivos de TI no se pueden rastrear a ningún objetivo del negocio | El plan compite por presupuesto sin argumento |
| **Diagnóstico decorativo** | El FODA tiene frases genéricas aplicables a cualquier empresa | Las estrategias no responden a la realidad de la organización |
| **Portafolio sin priorización real** | Todos los proyectos son «alta prioridad» | Se ejecuta lo que se pueda, no lo que importa |
| **Ausencia de línea base** | Se declaran metas sin saber el valor actual | Es imposible demostrar avance |
| **Sin dueño ni gobernanza** | Nadie es responsable del plan después de su aprobación | El plan muere el día siguiente a su presentación |

## De dónde viene y hacia dónde va el planeamiento (30 min)

Un PETI no nace de la nada ni termina en sí mismo. Se inserta en una cadena:

```
      ESTRATEGIA DEL NEGOCIO
    (visión, objetivos, modelo de negocio)
                │
                ▼
        DIAGNÓSTICO ESTRATÉGICO
     (interno + externo + arquitectura actual)
                │
                ▼
         OBJETIVOS DE TI
    (derivados, medibles, con línea base)
                │
                ▼
      ARQUITECTURA OBJETIVO
      (negocio, datos, aplicaciones, tecnología)
                │
                ▼
       ANÁLISIS DE BRECHAS
                │
                ▼
    PORTAFOLIO DE PROYECTOS
   (priorizado, con caso de negocio)
                │
                ▼
          HOJA DE RUTA
      (secuencia, dependencias, presupuesto)
                │
                ▼
   EJECUCIÓN · SUPERVISIÓN · AJUSTE
```

**Lo que ocurre cuando se saltan pasos.** La mayoría de los planes fallidos empiezan en «portafolio de proyectos»: alguien decide comprar un ERP, y el plan se escribe hacia atrás para justificarlo. **El síntoma es reconocible:** el diagnóstico de esos planes siempre concluye exactamente lo que hace falta para justificar la compra ya decidida.

**El horizonte y la revisión.** En el sector público peruano, el **Plan de Gobierno Digital** se aprueba por un periodo **mínimo de tres años** y debe **actualizarse y evaluarse anualmente**, conforme a los Lineamientos aprobados por la Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI. En el sector privado la práctica es equivalente: horizonte de tres a cinco años con revisión anual. **Un plan que no se revisa no es estratégico: es histórico.**

## La organización objeto de estudio (25 min)

**Requisitos de la organización.** Cada equipo (4 a 5 integrantes) propone esta misma semana una organización real que cumpla:

| Requisito | Por qué |
|---|---|
| Al menos 15 personas y un responsable de TI o de sistemas identificable | Sin estructura mínima no hay nada que planificar |
| Un contacto dispuesto a conceder **al menos tres entrevistas** durante el semestre | El diagnóstico requiere acceso a la gerencia, no solo a TI |
| Documentación básica accesible: organigrama, plan institucional o de negocio, presupuesto aproximado | Sin evidencia, el diagnóstico es especulación |
| Puede ser **empresa privada, entidad pública, ONG, cooperativa o institución educativa** | La metodología es la misma; cambia el marco normativo |

**Ventaja de elegir una entidad pública.** El marco normativo peruano es explícito y auditable —Ley de Gobierno Digital, Lineamientos del PGD, Política Nacional de Transformación Digital—, lo que da al equipo un criterio objetivo. **Ventaja de elegir una empresa privada:** mayor libertad metodológica y acceso más directo a la gerencia.

**Ética del encargo.** Antes de solicitar cualquier documento se entrega la **carta de presentación institucional de la UPT** y se firma el **acuerdo de confidencialidad**. El PETI que se produce **es propiedad intelectual compartida** con la organización: se le entrega al cierre del semestre, y esa es la principal razón por la que las organizaciones aceptan participar.

**Caso simulado de respaldo.** Si el acceso no se concreta, el equipo trabaja con la organización ficticia documentada en `ANEXO-CASO-SIMULADO.md`, con todos sus documentos, cifras y personajes. La metodología y la exigencia son idénticas.

## Prueba de entrada y encuadre (15 min)

**Prueba de entrada diagnóstica** (15 preguntas, sin nota) sobre: diferencia entre eficacia y eficiencia, lectura de un organigrama, noción de FODA, qué es un indicador, qué es una arquitectura de aplicaciones, lectura de un presupuesto simple y noción de valor presente. El resultado agregado define los refuerzos de las semanas 2 a 5.

**Regla de trabajo del curso:** todo producto se versiona en Git y se redacta en Markdown. La razón no es tecnológica: es que **un PETI real pasa por decenas de versiones y la trazabilidad de los cambios es parte de su calidad**.

---

---

[Semana 01](README.md) · **Teoría** · [Dinámica de aula](2-DINAMICA.md) · [Taller de laboratorio](3-TALLER.md)

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
