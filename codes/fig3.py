import numpy as np
import matplotlib.pyplot as plt
import os
import json
import ipywidgets as widgets
from IPython.display import display, HTML

# --- 1. GENERACIÓN DE DATOS ANALÍTICOS (Basados en el Contexto Técnico) ---
# Datos estimados para representar las curvas de compromiso (Pareto Front)
latencia_fp32 = [12.4, 13.0, 14.2]
consumo_fp32 = [2.8, 3.1, 3.5]

latencia_int8 = [8.7, 9.2, 10.5]
consumo_int8 = [1.8, 1.9, 2.2]

latencia_mixed = [6.2, 6.8, 7.5]
consumo_mixed = [1.2, 1.3, 1.5]

latencia_sparse = [7.5, 8.0, 9.0]
consumo_sparse = [1.4, 1.6, 1.9]

# --- 2. RECREACIÓN ANALÍTICA (MATPLOTLIB) ---
plt.figure(figsize=(9, 6))
plt.style.use('seaborn-v0_8-whitegrid')

# Dibujar límite de viabilidad (2W)
plt.axhline(2.0, color='red', linestyle='--', alpha=0.6, label='Satellite Limit (2W)')

# Graficar series
plt.plot(latencia_fp32, consumo_fp32, 'o-', color='#4A4A4A', label='FP32 (Baseline)')
plt.plot(latencia_int8, consumo_int8, 's-', color='#0047AB', label='INT8 Quantized')
plt.plot(latencia_mixed, consumo_mixed, 'd-', color='#002D6E', label='Mixed INT4/8')
plt.plot(latencia_sparse, consumo_sparse, '^-', color='#0073CF', label='Sparse Inference')

# Formato académico
plt.title("Trade-off: Inferencia Eficiente en Condiciones Orbitales", fontsize=12)
plt.xlabel("Latencia de Inferencia (ms)")
plt.ylabel("Consumo Energético (W)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.show()

# --- 3. GENERACIÓN DE CÓDIGO TIKZ MODULAR ---
tikz_code = r"""\begin{tikzpicture}
\begin{axis}[
    width=0.95\columnwidth,
    height=7cm,
    grid=both,
    grid style={line width=.1pt, draw=gray!10},
    major grid style={line width=.2pt, draw=gray!30},
    xlabel={Latency (ms)},
    ylabel={Power (W)},
    legend pos=north west,
    legend style={nodes={scale=0.7, transform shape}, draw=none, fill=none},
    axis lines=left,
    enlarge x limits=0.1,
    enlarge y limits=0.1,
    mark size=2pt,
    tick label style={font=\footnotesize}
]

% Límite Operativo Satelital
\addplot[red, dashed, thick, domain=5:15, forget plot] {2.0};
\node[red, anchor=south west] at (axis cs: 10, 2.0) {\tiny Operational Limit (2W)};

% FP32 Baseline
\addplot[color=gray!60, mark=*, thick] coordinates {
    (12.4, 2.8) (13.0, 3.1) (14.2, 3.5)
};
\addlegendentry{FP32 Baseline}

% INT8
\addplot[color=blue!70!black, mark=square*, thick] coordinates {
    (8.7, 1.8) (9.2, 1.9) (10.5, 2.2)
};
\addlegendentry{INT8}

% Mixed INT4/8
\addplot[color=blue!40!black, mark=diamond*, thick] coordinates {
    (6.2, 1.2) (6.8, 1.3) (7.5, 1.5)
};
\addlegendentry{Mixed INT4/8}

% Sparse
\addplot[color=cyan!70!black, mark=triangle*, thick] coordinates {
    (7.5, 1.4) (8.0, 1.6) (9.0, 1.9)
};
\addlegendentry{Sparse}

\end{axis}
\end{tikzpicture}"""

# --- 4. INTERFAZ INTERACTIVA (IPYWIDGETS) ---
filename_input = widgets.Text(value='fig_tradeoff_pareto.tex', description='Archivo:', layout=widgets.Layout(width='300px'))
save_btn = widgets.Button(description='💾 Guardar en Disco', button_style='success')
copy_btn = widgets.Button(description='📋 Copiar TikZ', button_style='info')
output_log = widgets.Output()

def save_to_disk(b):
    with output_log:
        path = "workflow/workflow/outputs/codes/"
        os.makedirs(path, exist_ok=True)
        full_path = os.path.join(path, filename_input.value)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(tikz_code)
        print(f"✅ Guardado exitosamente en: {full_path}")

def copy_to_clipboard(b):
    with output_log:
        # JavaScript para copiar al portapapeles en Colab
        js = f"navigator.clipboard.writeText({json.dumps(tikz_code)}); alert('Código TikZ copiado');"
        display(HTML(f"<script>{js}</script>"))
        print("📋 Código copiado al portapapeles.")

save_btn.on_click(save_to_disk)
copy_btn.on_click(copy_to_clipboard)

display(widgets.HBox([filename_input, save_btn, copy_btn]))
display(output_log)