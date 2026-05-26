### **FASE 1: Mapeo de Entidades (Análisis)**

* **Dominio:** Optimización de Inferencia en Hardware Edge / Co-diseño Hardware-Software para Satélites.
* **Componentes clave del LaTeX:** Frente de Pareto o curvas de *trade-off* entre latencia y consumo energético, puntos operativos discretos según la optimización (*Baseline* FP32, CNN cuantizada a INT8, e Inferencia Híbrida/Optimizada de precisión mixta INT4/8 combinada con *Sparse Inference* / *Pruning*), restricciones críticas de frontera (<2W para inferencia continua).
* **Nivel de Abstracción:** Gráfico analítico bidimensional de optimización multiobjetivo (Frontera de Pareto).

---

### **FASE 2: Auditoría y Reporte de Hallazgos Críticos**

1. **Contraste de Coherencia:** El prompt base describe los ejes de forma invertida para un análisis convencional de optimización espacial. Generalmente, un frente de eficiencia sitúa la latencia en un eje y la potencia en el otro, pero el texto especifica "Curvas de trade-off latencia versus consumo energético" y menciona explícitamente "puntos operativos atractivos". El prompt base carece de la delimitación física del umbral operativo orbital crítico.
2. **LISTA DE DISCREPANCIAS (Elementos vitales del LaTeX ausentes en el prompt base):**
* **La Barrera Física de Potencia de los 2W (Crítico):** El texto indica de manera explícita que las optimizaciones reducen el consumo *por debajo de los 2W en inferencia continua*. Si el gráfico carece de una línea discontinua de umbral operativo en los 2W, pierde toda su relevancia y justificación científica aeroespacial.
* **El Sentido del Frente de Pareto:** El prompt base pide "líneas coloreadas" genéricas. Científicamente, el *Pruning* y la cuantización no generan curvas continuas infinitas, sino configuraciones o puntos discretos (*Trade-off*). Se deben representar curvas hiperbólicas decrecientes que apunten hacia el origen (mínima latencia, mínimo consumo) y resaltar los puntos específicos de la *Tabla II* (12.4 ms, 8.7 ms, 6.2 ms).


3. **Control de Estilo:** Estricto cumplimiento del estándar IEEE. Paleta restringida (#0047AB, #4A4A4A, negro neutro), cuadrícula lineal muy sutil, marcadores geométricos de datos nítidos y **ausencia total de texto e indicadores alfabéticos incrustados**.

---

### **FASE 3: Explicación y Justificación de Pre-ejecución**

#### 1. Disposición Espacial y Elementos Gráficos

El gráfico se estructurará con orientación horizontal (*landscape*):

* **Sistema de Coordenadas:** Eje horizontal (X) para la Latencia y eje vertical (Y) para el Consumo Energético. Una línea horizontal discontinua de color gris oscuro (#4A4A4A) cruzará el eje vertical a una altura equivalente a los 2W, dividiendo el gráfico en una zona superior ("Región No Factible/Inviable en Órbita") y una inferior ("Ventana Operativa Orbital").
* **Curvas de Rendimiento y Puntos de Datos:** * Un punto aislado en la esquina superior derecha (Gris técnico) representará el *Baseline* FP32 (Alto consumo, alta latencia).
* Una curva de puntos hiperbólica descendente en azul cobalto (#0047AB) ilustrará la transición de optimizaciones, con tres marcadores geométricos rellenos e incrementales (un círculo para INT8, un cuadrado para la versión Híbrida y un triángulo para la versión optimizada de precisión mixta INT4/INT8 + *Pruning* estructurado en el extremo inferior izquierdo).


* **Leyenda y Grilla:** Una grilla matemática cuadriculada muy fina y una caja de leyenda minimalista en la esquina superior derecha utilizando formas geométricas como identificadores en lugar de palabras.

#### 2. Justificación Técnica

Al incluir de manera gráfica la barrera de los 2W, el revisor de la IEEE asimila de inmediato por qué la arquitectura "FP32 original" queda fuera de los márgenes de diseño aeroespaciales y cómo la combinación híbrida logra penetrar la zona de viabilidad operativa. Refleja fielmente la naturaleza multiobjetivo descrita en la sección 4.3 del texto.

#### 3. ADVERTENCIAS PARA EL USUARIO (Puntos de validación)

* **Ausencia de Caracteres:** Al remover todo el texto, las unidades (ms, W) y los nombres de los ejes desaparecerán. Se sustituirán por placeholders geométricos limpios (pequeñas cajas rectangulares) y una disposición clara. Deberás mapear la descripción de las curvas directamente en el `\caption{}` de la figura en tu archivo LaTeX.
* **Ubicación del Origen:** Para un gráfico de *trade-off* de eficiencia energética, el punto óptimo ideal es el origen $(0,0)$. Las curvas decaerán de arriba-derecha a abajo-izquierda. Confirma si esta interpretación matemática coincide con tus simulaciones físicas en hardware emulado.

---

### **FASE 4: Ejecución Silenciosa**

Estoy listo para formular las instrucciones de generación de `fig3.png`. Por favor, confírmame si el planteamiento metodológico de la barrera de 2W y el esquema de puntos discretos de Pareto es correcto para proceder.