**TESIS: Desarrollo de un Sistema de Pronóstico del Centelleo Ionosférico sobre el Perú utilizando Machine Learning para la Mitigación de Perturbaciones en Señales Satelitales.**
---

El trabajo de tesis tiene como objetivo principal desarrollar un sistema de pronóstico de irregularidades ionosféricas conocidas como centelleos. Estas irregularidades afectan a las señales satelitales de telecomunicaciones y de navegación, generando perturbaciones que comprometen la precisión y continuidad de sistemas como el GNSS(Global Navigation Satellite Systems). Este sistema garantiza la identificación de perturbaciones que afectan las señales satelitales y realiza pronósticos precisos de sus ocurrencias contribuyendo así a reducir riesgos asociados a estas irregularidades.
En un contexto donde la dependencia de tecnologías basadas en GNSS es esencial para aplicaciones críticas —desde navegación autónoma hasta comunicaciones de alta seguridad—, fenómenos ionosféricos como el centelleo representan un desafío significativo. Estas irregularidades, especialmente frecuentes en latitudes bajas como el Perú, pueden degradar o interrumpir las señales, comprometiendo el funcionamiento de sistemas de posicionamiento y navegación en actividades cotidianas y estratégicas. Ante  esta problemática, el sistema busca implementar un enfoque integral que permita mitigar estos efectos adversos mediante el uso de diferentes tecnologías, instrumentos, bases de datos y algoritmos de aprendizaje automático.
Para alcanzar los objetivos, el sistema integra datos de tres fuentes clave:
El servicio OmniWeb de la NASA, que proporciona parámetros de clima espacial como el índice kp y la velocidad del viento solar.
Los radares y ionosondas del Radio Observatorio de Jicamarca(ROJ) sede del Instituto Geofísico del Perú, que ofrecen información detallada de la ionósfera.
La red instrumentos distribuidos Low Latitude Ionospheric Sensor Network(LISN), que recopila mediciones del contenido total de electrones(TEC) en regiones cŕiticas como la anomalía ecuatorial.
El desarrollo del sistema incluirá modelos predictivos basados en técnicas de machine learning. Entre estos destacan redes neuronales recurrentes (LSTM) para analizar secuencias temporales, y métodos supervisados como Support Vector Machines (SVM) y Random Forest para clasificar los niveles de centelleo representados por el índice S4. Estos modelos integrarán variables geofísicas, datos históricos y mediciones en tiempo real, permitiendo anticipar perturbaciones con hasta varias horas de antelación.
Se tiene en cuenta también la incorporación de análisis detallados sobre burbujas de plasma, utilizando una vasta base de datos histórica del Instituto Geofísico del Perú (IGP), que abarca más de dos décadas de registros ionosféricos. Este enfoque permitirá profundizar en la relación entre estas irregularidades y los fenómenos de centelleo.
En conclusión, este sistema no sólo mitigará los impactos negativos del centelleo en tecnologías basadas en GNSS, sino que también posicionará al Perú como líder regional en el monitoreo y pronóstico ionosférico. Su implementación fortalecerá la capacidad de respuesta frente a estos fenómenos, beneficiando a sectores productivos, actividades socioeconómicas y aplicaciones estratégicas a nivel nacional.

**PLAN DE TRABAJO	Nº 02**
---

NOTA INICIAL: El entorno de ejecucion de los programas es el base de anaconda de la laptop Ubuntu22.04

**I TRIMESTRE**
**Revisión Sistemática de la Literatura y Adquisición de Datos:**
1. Revisión sistemática de la literatura:
* Analizar artículos clave sobre técnicas de predicción del centelleo ionosférico utilizando machine learning.
* Identificar enfoques relevantes como el uso de redes neuronales (LSTM) y Random Forest en el pronóstico del TEC (contenido total de electrones), revisando estudios como "Data‐Driven Forecasting of Low‐Latitude Ionospheric Total Electron Content.
* Profundizar en investigaciones sobre técnicas de radio-ocultación GNSS y correlación del índice S4 con irregularidades ionosféricas como burbujas de plasma y Es layers​.

2. Adquisición de datos históricos:
* Recopilar datos de clima espacial (índices Kp, AE, Dst, f10.7) desde el servicio OmniWeb de la NASA.
* Obtener mediciones ionosféricas (TEC, derivas ExB) proporcionadas por la red de sensores del ROJ y LISN del IGP.
Definir periodos y estaciones críticas para el análisis, priorizando datos de alta calidad y resolución temporal consistente.
3. Preprocesamiento de datos:
* Normalización: Escalar los datos para asegurar uniformidad en las entradas del modelo.
* Eliminación de outliers: Identificar y excluir valores atípicos que puedan afectar la precisión del modelo.
* Agregación temporal: Consolidar los datos en ventanas temporales apropiadas para facilitar el análisis de series temporales (e.g., 30 minutos o 1 hora).

**II TRIMESTRE**
**Desarrollo del Modelo Predictivo:**

1. Selección de características (Feature Selection):
* Implementar Random Forest para identificar las variables geofísicas más influyentes en el centelleo ionosférico.
Priorizar parámetros como el índice f10.7, Kp y TEC previo, según las mejores prácticas documentadas en la literatura​.

2. Desarrollo y entrenamiento de modelos:
* Clasificación: Entrenar modelos supervisados como SVM y Random Forest para clasificar niveles de centelleo basados en el índice S4.
* Regresión: Implementar redes neuronales LSTM para predecir valores continuos de S4, considerando memoria temporal de eventos previos.

3. Validación del modelo:
* Aplicar técnicas de validación cruzada para evaluar la robustez de los modelos.
* Medir el desempeño utilizando métricas como precisión, recall, F1-score y RMSE para modelos de regresión.
* Realizar pruebas con datos de prueba independientes para garantizar generalización.

**III TRIMESTRE**
**Implementación y Validación** 
1. Desarrollo del sistema integrado:
* Implementar los modelos predictivos en una plataforma accesible, con capacidad de visualización y análisis en tiempo real.
* Diseñar una interfaz que permita a los usuarios consultar predicciones y datos históricos de centelleo.

2. Pruebas en ubicaciones estratégicas:

* Realizar validaciones en campo en regiones críticas como Piura y Jicamarca, con alta incidencia de fenómenos ionosféricos.
* Ajustar parámetros de los modelos según el desempeño observado en condiciones reales.

3. Documentación y análisis final:

* Comparar resultados obtenidos con estudios previos para validar la efectividad del sistema.
* Proponer mejoras y extender el sistema a otras regiones del país según necesidades futuras-

