```markdown
**Title**: IA Orientada al On-board Cloud Masking y Filtrado Inteligente: Arquitecturas de Inferencia Eficiente para Satélites de Próxima Generación

**Description**: El proyecto propone arquitecturas de inteligencia artificial optimizadas para la detección de nubes (cloud masking) y filtrado inteligente directamente a bordo de satélites de observación terrestre de próxima generación. Se desarrollan modelos híbridos basados en CNNs ligeras con reducción de features y gradient boosting, combinados con técnicas avanzadas de compresión (pruning y quantization aware training) y optimizaciones hardware-aware para FPGA y VPU. Los modelos alcanzan accuracies superiores al 93% con menos de 1.500 parámetros, habilitando inferencia eficiente en entornos con restricciones severas de potencia, memoria y radiación, y permitiendo downlink selectivo de datos útiles.

**General Objective**: Desarrollar y validar arquitecturas de inferencia eficiente basadas en IA para cloud masking y filtrado inteligente on-board en satélites de observación terrestre.

**Specific Objectives**: 
- Diseñar modelos CNN ligeros y enfoques híbridos CNN-Gradient Boosting con reducción extrema de complejidad computacional.
- Implementar técnicas de pruning, cuantización y optimizaciones hardware-aware para cumplir restricciones espaciales.
- Evaluar el desempeño en métricas de precisión, robustez y eficiencia en datasets multi-espectrales y hardware emulado.
- Analizar trade-offs entre accuracy, latencia, consumo energético y resiliencia ante radiación.
- Proponer un pipeline completo de filtrado inteligente y recomendaciones para su integración en misiones futuras.

**Justification**: El creciente volumen de datos generados por sensores satelitales de alta resolución supera la capacidad de downlink disponible, lo que genera ineficiencias operativas y limita la respuesta en tiempo real ante eventos críticos. El procesamiento on-board de cloud masking permite filtrar información inútil (escenas nubladas) antes de la transmisión, reduciendo drásticamente el ancho de banda requerido, el consumo energético y los costos de operación. Esta capacidad es esencial para misiones de próxima generación, constelaciones de CubeSats y aplicaciones de monitorización climática, agrícola y de desastres, contribuyendo a una observación terrestre más autónoma, sostenible y eficiente.

**Methodology**: Se emplea un enfoque experimental de diseño y evaluación iterativa. Se desarrollan arquitecturas híbridas CNN-Boosting con optimizaciones de model compression (pruning estructurado y quantization aware training). La validación se realiza mediante datasets públicos multi-espectrales, simulaciones de degradación orbital y pruebas en hardware emulado (Jetson Orin NX representando restricciones de VPU/FPGA). Se utilizan métricas estándar (Accuracy, F2-Score) junto con mediciones de FLOPs, latencia, consumo energético y robustez ante fault injection.

**Scope**: Desarrollo y validación en entorno emulado de arquitecturas on-board para cloud masking multi-espectral con énfasis en eficiencia extrema (menos de 2W y latencia <10 ms).

**Activities**: 
1. Revisión del estado del arte y definición de requisitos. 
2. Diseño de arquitecturas CNN ligeras y modelos híbridos. 
3. Implementación de técnicas de inferencia eficiente (pruning, cuantización y optimizaciones hardware-aware). 
4. Experimentación y evaluación comparativa en datasets y hardware emulado. 
5. Análisis de resultados, discusión de trade-offs y elaboración de recomendaciones.

**Resources**: 
- Datasets públicos multi-espectrales (Sentinel, Landsat y simulados). 
- Plataformas de hardware emulado (NVIDIA Jetson Orin NX). 
- Frameworks de deep learning (PyTorch/TensorFlow) con soporte para quantization y pruning. 
- Herramientas de simulación de entorno espacial y fault injection.

**Limitations**: 
- Validación limitada a entornos emulados (no se incluyen pruebas en órbita real). 
- Dependencia de la calidad y representatividad de los datasets de entrenamiento. 
- Sensibilidad a eventos de radiación extrema y variabilidad hiperespectral no completamente modelada. 
- Restricciones de certificación para misiones de alto valor.
```