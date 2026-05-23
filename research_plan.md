```json
{
  "titulo": "IA Orientada al On-board Cloud Masking y Filtrado Inteligente: Arquitecturas de Inferencia Eficiente para Satélites de Próxima Generación",
  "folder_name": "ia_onboard_cloud_masking_filtrado_inteligente",
  "abstract_preliminar": "El procesamiento a bordo de imágenes satelitales enfrenta restricciones severas de potencia, memoria y computación. Este artículo propone arquitecturas de IA para cloud masking y filtrado inteligente en satélites de próxima generación, enfatizando inferencia eficiente mediante modelos ligeros (CNNs reducidas, boosting), técnicas de compresión (pruning, quantization) y optimizaciones hardware-aware. Se evalúan modelos con accuracies >93% y bajos requerimientos de parámetros (<600), demostrando viabilidad en entornos edge espaciales. Se discuten implementaciones en hardware como VPUs y FPGAs, comparando con enfoques ground-based. Los resultados validan reducciones significativas en latencia y consumo energético, habilitando downlink selectivo y análisis en tiempo real para misiones EO. Se abordan desafíos de radiación y generalización multi-sensor.",
  "secciones": [
    {
      "nro": 1,
      "titulo_seccion": "Introducción",
      "objetivos": ["Establecer la motivación y relevancia del cloud masking on-board", "Presentar desafíos de inferencia eficiente en satélites", "Delimitar objetivos y estructura del artículo"],
      "subsecciones": ["1.1 Motivación y Contexto en Observación Terrestre", "1.2 Desafíos Computacionales en Entornos Espaciales", "1.3 Contribuciones Principales"],
      "insumos": ["Figura 1: Diagrama de pipeline on-board", "Tabla 1: Comparación de requisitos satelitales"],
      "llaves_bibtex": ["Ali2026_Lightweight", "Aybar2024_DTACSNet", "PhiSat2_Overview"]
    },
    {
      "nro": 2,
      "titulo_seccion": "Estado del Arte",
      "objetivos": ["Revisar métodos tradicionales de cloud masking", "Analizar avances en IA on-board para EO", "Identificar brechas en eficiencia de inferencia"],
      "subsecciones": ["2.1 Métodos Basados en Umbrales y Física", "2.2 Enfoques de Deep Learning Ground-Based", "2.3 Soluciones On-Board Existentes y Misiones Demo"],
      "insumos": ["Tabla 2: Comparativa de accuracies y complejidad"],
      "llaves_bibtex": ["Ali2026_Lightweight", "Aybar2024_DTACSNet", "KP_Labs2024_PhiSat", "Anzalone2024_Review"]
    },
    {
      "nro": 3,
      "titulo_seccion": "Arquitecturas Propuestas para Cloud Masking",
      "objetivos": ["Describir modelos CNN ligeros y alternativas de boosting", "Presentar integración de filtrado inteligente", "Detallar optimizaciones para multi-espectral/hiperspectral"],
      "subsecciones": ["3.1 Modelos CNN con Reducción de Features", "3.2 Gradient Boosting para On-Board", "3.3 Pipeline de Filtrado Inteligente"],
      "insumos": ["Figura 2: Arquitectura CNN propuesta", "Eq. 1: Función de pérdida", "Tabla 3: Parámetros del modelo"],
      "llaves_bibtex": ["Ali2026_Lightweight", "FastSEnSeI2025"]
    },
    {
      "nro": 4,
      "titulo_seccion": "Técnicas de Inferencia Eficiente",
      "objetivos": ["Examinar pruning, quantization y destilación", "Evaluar trade-offs accuracy vs. eficiencia", "Adaptación a hardware satelital"],
      "subsecciones": ["4.1 Pruning y Sparse Inference", "4.2 Quantization Aware Training", "4.3 Optimizaciones Hardware-Aware (FPGA/VPU)"],
      "insumos": ["Tabla 4: Resultados de compresión", "Figura 3: Curvas de latencia-energía"],
      "llaves_bibtex": ["PruningQuant2025", "Li2025_ModelCompression", "Hawks2021_QAPruning"]
    },
    {
      "nro": 5,
      "titulo_seccion": "Resultados Experimentales",
      "objetivos": ["Presentar métricas de desempeño en datasets públicos y simulados", "Comparar con baselines", "Analizar consumo en entornos emulados"],
      "subsecciones": ["5.1 Evaluación de Accuracy y Robustez", "5.2 Métricas de Eficiencia Computacional", "5.3 Análisis en Hardware Emulado"],
      "insumos": ["Tabla 5: Resultados comparativos", "Figura 4: Ejemplos de máscaras"],
      "llaves_bibtex": ["Ali2026_Lightweight", "Aybar2024_DTACSNet", "TransferLearning2025"]
    },
    {
      "nro": 6,
      "titulo_seccion": "Discusión",
      "objetivos": ["Interpretar hallazgos y limitaciones", "Analizar implicaciones operacionales", "Comparar con estado del arte"],
      "subsecciones": ["6.1 Análisis de Trade-offs", "6.2 Robustez ante Radiación y Variabilidad", "6.3 Impacto en Misiones Futuras"],
      "insumos": [],
      "llaves_bibtex": ["KP_Labs2024_PhiSat", "Aybar2024_DTACSNet"]
    },
    {
      "nro": 7,
      "titulo_seccion": "Conclusiones y Trabajos Futuros",
      "objetivos": ["Sintetizar contribuciones", "Proponer direcciones de investigación", "Discutir escalabilidad"],
      "subsecciones": ["7.1 Resumen de Logros", "7.2 Limitaciones y Desafíos Abiertos", "7.3 Recomendaciones para Implementación"],
      "insumos": [],
      "llaves_bibtex": ["Ali2026_Lightweight", "PhiSat2_Overview"]
    }
  ]
}
```

```bibtex
@article{Ali2026_Lightweight,
  author    = {Ali, Mazen and Pereira, Antonio and Gentile, Fabio and others},
  title     = {Lightweight Cloud Masking Models for On-Board Inference in Hyperspectral Imaging},
  journal   = {Scientific Reports},
  year      = {2026},
  doi       = {10.1038/s41598-026-47153-x},
  url       = {https://www.nature.com/articles/s41598-026-47153-x},
  note      = {[Online]. Available: https://arxiv.org/abs/2507.08052}
}

@article{Aybar2024_DTACSNet,
  author    = {Aybar, C. and Mateo-García, G. and others},
  title     = {Onboard Cloud Detection and Atmospheric Correction With Efficient Deep Learning Models},
  journal   = {IEEE Transactions on Geoscience and Remote Sensing},
  year      = {2024},
  doi       = {10.1109/TGRS.2024.10716772},
  url       = {https://ieeexplore.ieee.org/document/10716772},
  note      = {IGARSS related}
}

@misc{KP_Labs2024_PhiSat,
  author    = {KP Labs},
  title     = {Boosting In-Orbit Cloud Detection with AI},
  year      = {2024},
  url       = {https://www.kplabs.space/news/boosting-in-orbit-cloud-detection-with-ai},
  note      = {Project overview for Φ-sat-2}
}

@article{Anzalone2024_Review,
  author    = {Anzalone, A. and others},
  title     = {An Introduction to Machine and Deep Learning Methods for Cloud Masking in Satellite Imagery},
  journal   = {Applied Sciences},
  volume    = {14},
  number    = {7},
  year      = {2024},
  doi       = {10.3390/app14072887},
  url       = {https://www.mdpi.com/2076-3417/14/7/2887}
}

@misc{FastSEnSeI2025,
  author    = {Authors of Fast-SEnSeI},
  title     = {Fast-SEnSeI: Lightweight Sensor-Independent Cloud Masking for On-board Multispectral Sensors},
  year      = {2025},
  url       = {https://arxiv.org/abs/2509.20991},
  note      = {arXiv preprint}
}

@article{PruningQuant2025,
  author    = {Li, X. and others},
  title     = {Research on Model Compression and Efficient Inference Algorithm for Deep Neural Networks},
  journal   = {IEEE Conference Proceedings},
  year      = {2025},
  url       = {https://ieeexplore.ieee.org/document/11069155/}
}

@article{Li2025_ModelCompression,
  author    = {Li, X.},
  title     = {Research on Model Compression and Efficient Inference Algorithm for Deep Neural Networks},
  journal   = {IEEE},
  year      = {2025},
  url       = {https://ieeexplore.ieee.org/document/11069155}
}

@article{Hawks2021_QAPruning,
  author    = {Hawks, B. and others},
  title     = {Ps and Qs: Quantization-Aware Pruning for Efficient Low Latency Neural Network Inference},
  journal   = {Frontiers in Artificial Intelligence},
  year      = {2021},
  doi       = {10.3389/frai.2021.676564},
  url       = {https://www.frontiersin.org/articles/10.3389/frai.2021.676564/full}
}

@misc{TransferLearning2025,
  author    = {Authors},
  title     = {Transfer Learning for Onboard Cloud Segmentation in Thermal Earth Observation},
  year      = {2025},
  url       = {https://arxiv.org/abs/2511.00357}
}

@misc{PhiSat2_Overview,
  author    = {ESA},
  title     = {Φsat-2 Mission Overview},
  year      = {2025},
  url       = {https://www.esa.int/Applications/Observing_the_Earth/Phsat-2}
}
```

```json
{
  "seccion_nro": 1,
  "titulo_seccion": "Introducción",
  "mapa_uso": {
    "Ali2026_Lightweight": {
      "razon_seleccion": "Proporciona evidencia reciente de modelos lightweight para cloud masking on-board con accuracies >93% y baja complejidad.",
      "guia_redaccion": "Citar en 1.1 y 1.3 para motivar la viabilidad técnica y destacar resultados de inferencia rápida en hardware emulado.",
      "subseccion_destino": "1.1"
    },
    "Aybar2024_DTACSNet": {
      "razon_seleccion": "Ejemplo IEEE de DTACSNet para cloud detection y corrección atmosférica on-board.",
      "guia_redaccion": "Usar en 1.2 para ilustrar arquitecturas eficientes y desafíos de integración multi-tarea.",
      "subseccion_destino": "1.2"
    },
    "PhiSat2_Overview": {
      "razon_seleccion": "Demostrador real de misiones con AI on-board para cloud filtering.",
      "guia_redaccion": "Referenciar en 1.3 para contextualizar contribuciones en misiones de próxima generación.",
      "subseccion_destino": "1.3"
    }
  }
}
```

```json
{
  "seccion_nro": 2,
  "titulo_seccion": "Estado del Arte",
  "mapa_uso": {
    "Ali2026_Lightweight": {
      "razon_seleccion": "Estudio clave sobre modelos boosting y CNN para hyperspectral on-board.",
      "guia_redaccion": "Tabla comparativa en 2.3, citando métricas de eficiencia y limitaciones de ground-based.",
      "subseccion_destino": "2.3"
    },
    "Aybar2024_DTACSNet": {
      "razon_seleccion": "Enfoque CNN eficiente para detección y corrección on-board.",
      "guia_redaccion": "Contrastar en 2.2-2.3 con métodos tradicionales, destacando F2-score.",
      "subseccion_destino": "2.3"
    },
    "KP_Labs2024_PhiSat": {
      "razon_seleccion": "Caso práctico de Φ-sat-2 para cloud detection on-orbit.",
      "guia_redaccion": "Ejemplo en 2.3 de reducción de downlink mediante AI.",
      "subseccion_destino": "2.3"
    },
    "Anzalone2024_Review": {
      "razon_seleccion": "Revisión comprehensiva de DL para cloud masking.",
      "guia_redaccion": "Base para 2.1 y 2.2, categorizando enfoques.",
      "subseccion_destino": "2.2"
    }
  }
}
```

```json
{
  "seccion_nro": 3,
  "titulo_seccion": "Arquitecturas Propuestas para Cloud Masking",
  "mapa_uso": {
    "Ali2026_Lightweight": {
      "razon_seleccion": "Base directa para CNN con feature reduction y modelos alternativos.",
      "guia_redaccion": "Describir arquitectura en 3.1 y 3.2, citando número de parámetros (597) y accuracy.",
      "subseccion_destino": "3.1"
    },
    "FastSEnSeI2025": {
      "razon_seleccion": "Modelo sensor-independiente lightweight para multispectral.",
      "guia_redaccion": "Integrar en 3.3 para pipeline de filtrado multi-sensor.",
      "subseccion_destino": "3.3"
    }
  }
}
```

```json
{
  "seccion_nro": 4,
  "titulo_seccion": "Técnicas de Inferencia Eficiente",
  "mapa_uso": {
    "PruningQuant2025": {
      "razon_seleccion": "Investigación reciente sobre compresión y algoritmos de inferencia eficiente.",
      "guia_redaccion": "Soportar discusión de pruning y quantization en 4.1-4.2 con resultados cuantitativos.",
      "subseccion_destino": "4.2"
    },
    "Li2025_ModelCompression": {
      "razon_seleccion": "Enfoque sistemático en compresión DNN para edge.",
      "guia_redaccion": "Citar en 4.3 para adaptaciones hardware-aware.",
      "subseccion_destino": "4.3"
    },
    "Hawks2021_QAPruning": {
      "razon_seleccion": "Estudio fundacional de quantization-aware pruning.",
      "guia_redaccion": "Usar en 4.1 para justificar combinación de técnicas y trade-offs.",
      "subseccion_destino": "4.1"
    }
  }
}
```

```json
{
  "seccion_nro": 5,
  "titulo_seccion": "Resultados Experimentales",
  "mapa_uso": {
    "Ali2026_Lightweight": {
      "razon_seleccion": "Resultados empíricos detallados de modelos lightweight.",
      "guia_redaccion": "Principal fuente para Tabla 5 y Figura 4, comparando CPU/GPU inference.",
      "subseccion_destino": "5.2"
    },
    "Aybar2024_DTACSNet": {
      "razon_seleccion": "Métricas de F2-score y eficiencia on-board.",
      "guia_redaccion": "Baseline en 5.1 para validación.",
      "subseccion_destino": "5.1"
    },
    "TransferLearning2025": {
      "razon_seleccion": "Ejemplo de transfer learning para thermal/cloud en CubeSats.",
      "guia_redaccion": "Citar en 5.3 para emulación Jetson y escalabilidad.",
      "subseccion_destino": "5.3"
    }
  }
}
```

```json
{
  "seccion_nro": 6,
  "titulo_seccion": "Discusión",
  "mapa_uso": {
    "KP_Labs2024_PhiSat": {
      "razon_seleccion": "Implicaciones operacionales en misiones reales.",
      "guia_redaccion": "Discutir impacto en 6.3 y reducción de datos.",
      "subseccion_destino": "6.3"
    },
    "Aybar2024_DTACSNet": {
      "razon_seleccion": "Limitaciones y fortalezas de modelos eficientes.",
      "guia_redaccion": "Contrastar limitaciones en 6.1-6.2.",
      "subseccion_destino": "6.1"
    }
  }
}
```

```json
{
  "seccion_nro": 7,
  "titulo_seccion": "Conclusiones y Trabajos Futuros",
  "mapa_uso": {
    "Ali2026_Lightweight": {
      "razon_seleccion": "Resumen de potencial para sistemas on-board AI.",
      "guia_redaccion": "Sintetizar logros y sugerir extensiones en 7.2-7.3.",
      "subseccion_destino": "7.1"
    },
    "PhiSat2_Overview": {
      "razon_seleccion": "Contexto de misiones demo para trabajos futuros.",
      "guia_redaccion": "Proponer integración en plataformas como Φ-sat en 7.3.",
      "subseccion_destino": "7.3"
    }
  }
}
```