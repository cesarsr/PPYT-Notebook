import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _():
    import marimo as mo

    css = """
    /* ============================================================
       Tema "JupyterLab + Video Accesible" para marimo / molab
       Autor: curso Programación con Python I
       Uso:
         A) Stylus → regla para molab.marimo.io → pegar todo este archivo
         B) Celda de apertura del cuaderno (ver celda_inicio.py)
       Nota: usa SOLO la variable pública --marimo-monospace-font y
       selectores de etiqueta estándar (p, pre, h1...) para máxima
       robustez ante actualizaciones de marimo/molab.
       ============================================================ */

    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;600;700&display=swap');

    :root {
      /* Familias tipográficas (variables públicas y estables de marimo) */
      --marimo-text-font: 'Inter', 'Segoe UI', system-ui, sans-serif;
      --marimo-heading-font: 'Inter', 'Segoe UI', system-ui, sans-serif;
      --marimo-monospace-font: 'JetBrains Mono', 'Cascadia Code', 'SF Mono', Consolas, monospace;

      /* Paleta alto contraste (claro / oscuro) */
      --video-fg:        light-dark(#111111, #f2f2f2);
      --video-fg-soft:   light-dark(#333333, #d9d9d9);
      --video-bg-celda:  light-dark(#f7f7f7, #1e1e24);
      --video-borde:     light-dark(#c8c8c8, #3a3a44);
      --video-acento:    light-dark(#2166ac, #6cb2f5);   /* azul JupyterLab */
      --video-exito:     light-dark(#1a7f37, #4ade80);
      --video-advert:    light-dark(#9a6700, #f0b429);
      --video-error:     light-dark(#cf222e, #ff7b72);
    }

    /* ---------- 1. TIPOGRAFÍA GRANDE Y LEGIBLE (video) ---------- */

    body, .paragraph, p, li, td, th {
      font-size: 1.2rem;
      line-height: 1.7;
      color: var(--video-fg);
    }

    strong, b { color: var(--video-fg); font-weight: 700; }

    /* Código proporcional en títulos respecto a la nueva base */
    h1 code, h2 code, h3 code, h4 code, h5 code, h6 code {
       font-size: 0.75em !important; 
       font-weight: inherit !important;
       display: inline-block !important;
    }

    h1 { font-size: 2.2rem; font-weight: 700; margin: 1.1em 0 0.6em; }
    h2 { font-size: 1.75rem; font-weight: 700; margin: 1em 0 0.5em; }
    h3 { font-size: 1.45rem; font-weight: 600; margin: 0.9em 0 0.4em; }
    h4 { font-size: 1.25rem; font-weight: 600; }

    /* Enlaces con contraste y subrayado visible */
    a {
      color: var(--video-acento);
      text-decoration: underline;
      text-underline-offset: 3px;
    }

    /* ---------- 2. CÓDIGO: look JupyterLab ---------- */

    pre, code, kbd, samp {
      font-family: var(--marimo-monospace-font);
      font-size: 0.9rem;  /* Original 1.05rem afecta el tamaño de salida y codigo */
      line-height: 1.6;
      color: var(--video-fg);
    }

    /* Bloques de código con fondo tipo JupyterLab */
    pre {
      background: var(--video-bg-celda);
      border: 1px solid var(--video-borde);
      border-left: 4px solid var(--video-acento);
      border-radius: 6px;
      padding: 0.1em 1.1em; /* original 0.9em 1.1em afecta padding de la salida resultado */
      overflow-x: auto;
    }

    /* Código en línea resaltado */
    code {
      background: var(--video-bg-celda);
      border: 1px solid var(--video-borde);
      border-radius: 4px;
      padding: 0.1em 0.35em;
    }

    pre code { background: transparent; border: none; padding: 0; }

    /* ---------- 3. CELDAS: aire de JupyterLab ---------- */

    /* Tarjeta suave alrededor del contenido de cada celda
       (best-effort: el contenedor interno puede cambiar de nombre) */
    section, article, [data-cell], .marimo-cell {
      border-radius: 3px;
    }

    /* Salidas: algo mas pequenas que el codigo (acompanan, no dominan).
       !important necesario porque los estilos internos de molab ganan
       la especificidad en el area de salida. */
    [data-cell-role='output'], .output, .marimo-output,
    .marimo-output *, [class*='output'], [class*='Output'] {
      font-size: 1.05rem !important;
      font-weight: 500 !important;
      color: var(--video-fg);
    }

    /* Excepcion: la PROSA markdown vive dentro del mismo contenedor de salida
       en marimo. Se restaura al tamaño grande de lectura para video;
       los resultados planos de codigo se quedan en 1.05rem. */
    .marimo-output p, .marimo-output li, .marimo-output .paragraph,
    .output p, .output li, .output .paragraph,
    [data-cell-role='output'] p, [data-cell-role='output'] li,
    [data-cell-role='output'] .paragraph {
      font-size: 1.2rem !important;
      line-height: 1.7 !important;
      font-weight: 400 !important;
    }
    /* Nota: SIN borde lateral en salidas. En marimo, las celdas markdown
       tambien renderizan su contenido como 'output': un borde aqui pegaria
       en todo. La distincion visual de la salida la da el tamano/peso. */
    /* Tablas y texto largo dentro de salidas: ligeramente menor */
    [data-cell-role='output'] table, .output table, .marimo-output table {
      font-size: 0.95rem !important;
    }

    /* ---------- 4. TABLAS legibles ---------- */
    /*
    table {
      border-collapse: collapse;
      font-size: 1.1rem;
      margin: 1em 0;
    }

    th, td {
      border: 1px solid var(--video-borde);
      padding: 0.5em 0.9em;
    }

    th {
      background: var(--video-bg-celda);
      font-weight: 700;
    }

    tr:nth-child(even) td {
      background: color-mix(in srgb, var(--video-bg-celda) 60%, transparent);
    }
    *()
    /* ---------- 5. ADORNOS DE ACCESIBILIDAD ---------- */

    ::selection {
      background: var(--video-acento);
      color: #ffffff;
    }

    /* Citas y avisos llamativos */
    blockquote {
      border-left: 4px solid var(--video-advert);
      background: var(--video-bg-celda);
      margin: 1em 0;
      padding: 0.6em 1em;
      font-size: 1.15rem;
    }

    /* Línea horizontal clara */
    hr {
      border: none;
      border-top: 2px solid var(--video-borde);
      margin: 1.5em 0;
    }

    /* ---------- 6. MODO CLARO "JupyterLab puro" (opcional) ----------
       Si grabas SIEMPRE en tema claro y quieres el fondo grisáceo
       característico de JupyterLab, descomenta el bloque: */

    /*
    html { background: #ececec; }
    body { background: #ffffff; }
    */

    /* ---------- 7. Resumen de cambios para producción ----------
       - Texto base 1.2rem (≈ 19px a zoom 100 %; ≈ 24 px a zoom 125 %)
       - Código 1.05rem mono espaciada con borde azul estilo Jupyter
       - Salidas a 1rem (algo menor que el codigo), peso medio, sin bordes decorativos
       - Contraste AA+: #111 sobre blanco / #f2f2f2 sobre oscuro
       ============================================================ */

    """

    # Inyecta el CSS en el cuaderno (funciona en molab y en marimo local).
    # Alternativa para la pantalla del instructor: extension Stylus con molab-jupyterlab.css
    mo.Html("<style>" + css + "</style>")
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Introducción a los Cuadernos de Python con marimo

    **marimo** es un entorno de computación interactiva de código abierto y reactivo para Python que te permite escribir y ejecutar código, crear visualizaciones e incluir texto enriquecido, ecuaciones y elementos interactivos en un solo lugar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ¿Qué es un cuaderno marimo?

    - Un **cuaderno (notebook)** está compuesto por **celdas** que pueden contener código Python, texto enriquecido (**Markdown**), ecuaciones matemáticas ($\LaTeX$) y salidas visuales (gráficos, tablas e interfaces interactivas).
    - Es ampliamente utilizado para **análisis de datos**, **investigación científica**, **enseñanza** y **creación de prototipos**.
    - A diferencia de los cuadernos tradicionales, los cuadernos de marimo se guardan como archivos puros de Python (`.py`), fáciles de versionar con Git y ejecutar como scripts o aplicaciones web.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## ¿Por qué usar marimo?

    - **Exploración interactiva y reactiva:** Cuando modificas una variable o interactúas con un control visual, todas las celdas que dependen de ella se actualizan automáticamente.
    - Prototipado rápido y experimentación.
    - **Investigación 100% reproducible:** Combina código, explicaciones y resultados sin "estado oculto". El cuaderno siempre refleja exactamente lo que muestra el código en pantalla.
    - **Ejecución versátil:** Funciona en la nube (por ejemplo, en **Molab** sin instalar nada en tu computadora) o de forma local desde tu terminal o editor como VS Code.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Componentes básicos

    - **Celdas de código:** Ejecutan código Python. La última expresión de una celda (o lo que pases a `print()`) se muestra como salida.
    - **Celdas Markdown:** Permiten dar formato al texto, agregar encabezados, listas, imágenes y ecuaciones usando `mo.md(...)` o cambiando la vista de la celda a Markdown.
    - **Salidas (Outputs):** Visibles debajo de la celda de código por defecto (pueden mostrarse encima de la celda de código según tu configuración).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Atajos de teclado útiles

    | Atajo | Acción |
    | :--- | :--- |
    | `Ctrl/Cmd` `Enter` | Ejecutar la celda actual |
    | `Ctrl/Cmd` `Shift` `Enter` | Ejecutar o actualizar celdas pendientes |
    | `Ctrl/Cmd` `Shift` + `P` | Abrir la paleta de comandos |
    | `Ctrl/Cmd` `S` | Guardar el cuaderno |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 1. Ejemplo de Celda de Código

    No te preocupes si aún no conoces todos los detalles de Python; aprenderás paso a paso en los módulos del curso. Aquí asignamos dos variables (`x` e `y`) y mostramos su suma:
    """)
    return


@app.cell
def _():
    # Asignamos valores y mostramos el resultado con Ctrl Enter
    x = 10
    y = 5
    print("x + y =", x + y)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 2. Ejemplo de Celda Markdown

    En marimo, el texto enriquecido se escribe convirtiendo la celda al modo Markdown desde el menú de la celda. Puedes usar `#` para encabezados, `*cursiva*`, `**negrita**` y signos de dólar `$$` para ecuaciones en $\LaTeX$.

    Haz doble clic en la celda de abajo o selecciona **Show code** (la opción con el ícono del ojo) en el menú de la celda de abajo para ver cómo está escrita y edítala si deseas probar:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Este es un encabezado de ejemplo.
    **Línea adicional**

    Puedes escribir texto en *cursiva*, en **negrita** e incluso añadir ecuaciones famosas:

    $$E = mc^2$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 3. El Orden de las Celdas y la Reactividad

    En los cuadernos tradicionales (como Jupyter), el orden manual en que ejecutas las celdas importa muchísimo: ejecutar celdas en desorden o sobrescribir variables en varias celdas suele causar errores (`NameError`) o resultados inconsistentes.

    **En marimo, esto se resuelve gracias a la ejecución reactiva:**

    1. **Actualización automática (Tipo hoja de cálculo):** marimo analiza qué variables define cada celda y cuáles utiliza. Cuando ejecutas una celda donde cambia una variable, marimo actualiza automáticamente todas las demás celdas que dependen de ella.
    2. **El orden visual en la página no rompe tu código:** Puedes colocar una celda con el resultado arriba y la definición abajo; marimo sabe en qué orden lógico ejecutarlas.
    3. **Regla de oro (Variables únicas):** En marimo, **no puedes definir la misma variable global en dos celdas distintas**. Cada variable tiene una única celda de origen para garantizar que siempre sepas cuál es su valor real.

    ### Ejemplo práctico de reactividad

    Observa las dos celdas siguientes (`Celda A` y `Celda B`). Prueba cambiar el valor de `n = 10` a `n = 5` en la **Celda A** y presiona `Ctrl` `Enter`. ¡Verás cómo la **Celda B** se actualiza sola sin que tengas que volver a ejecutarla manualmente!
    """)
    return


@app.cell
def _():
    # Celda A: Definimos la variable 'n'
    n = 5
    return (n,)


@app.cell
def _(n):
    # Celda B: Calculamos el doble de 'n'
    print("El doble de n es:", n * 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Interactividad nativa con controles visuales (`mo.ui`)

    Como marimo es reactivo, también podemos usar controles interactivos como deslizadores (*sliders*). Mueve el control deslizante de abajo y observa cómo la celda siguiente recalcula el resultado en tiempo real:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    factor = mo.ui.slider(start=1, stop=20, value=5, label="Selecciona un número:")
    factor
    return (factor,)


@app.cell(hide_code=True)
def _(factor, mo):
    mo.md(f"""
    El número seleccionado es **{factor.value}** y su cuadrado es **{factor.value ** 2}**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 4. Descargar, Exportar y Guardar el Cuaderno

    ### Guardar el cuaderno
    - Puedes guardar tus cambios haciendo clic en el ícono de **Guardar (disquete)** en la barra del cuaderno o usando el atajo `Ctrl` `S` (Windows/Linux) o `Cmd` `S` (Mac).
    - Si estás trabajando en un cuaderno compartido de solo lectura en la nube (como en **Molab**), puedes crear tu propia copia editable o descargarlo a tu computadora.

    ### Descargar y exportar
    Desde el menú del cuaderno (esquina superior derecha), puedes:
    1. **Descargar el código (`.py`):** Guarda el archivo original de Python en tu equipo.
    2. **Exportar como HTML o PDF:** Ideal para compartir tus resultados o entregar tareas en un formato estático de lectura.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## 5. Información Complementaria (Opcional)

    ### Operaciones con celdas
    Al pasar el cursor sobre una celda o hacer clic en el botón de acciones (`...`) en el borde de la celda, puedes:
    - **Agregar celdas:** Con los botones `+` arriba o abajo de la celda actual.
    - **Mover celdas:** Arrastrándolas o usando las opciones de subir/bajar celda.
    - **Dividir o combinar celdas** y ocultar el código (`Hide code`) para dejar solo el texto o resultado visible.
    - **Deshacer eliminación:** Si borras una celda por accidente con el ícono de papelera, puedes recuperarla desde el botón de deshacer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### El Kernel (Motor de Python) y cómo reiniciarlo
    El **kernel** es el motor computacional (el intérprete de Python) que ejecuta el código de tu cuaderno en segundo plano.
    - A diferencia de otros entornos donde debes reiniciar el kernel constantemente porque las variables quedan "sucias" en memoria, **marimo mantiene la memoria limpia automáticamente** (si borras una celda o una variable, también se elimina de la memoria).
    - Sin embargo, si ejecutas un bucle infinito por error o deseas reiniciar toda la sesión desde cero, puedes ir al menú del cuaderno y seleccionar **Restart kernel** (Reiniciar kernel).

    ---
    ### ¡Felicitaciones por completar este tutorial sobre cuadernos marimo!
    Ya tienes todo listo para explorar, experimentar con código Python y comenzar con los módulos prácticos del curso.
    """)
    return


if __name__ == "__main__":
    app.run()
