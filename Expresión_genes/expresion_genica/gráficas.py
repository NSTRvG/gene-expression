import matplotlib.pyplot as plt
import seaborn as sns

def violin_plot(expresion_genes_combined):
    """Genera un Violin Plot separando MW y Oven en cada tiempo"""
    plt.figure(figsize=(14, 10))
    sns.violinplot(x="Tiempo", y="Expresión", hue="Condición", data=expresion_genes_combined, split=True, palette="coolwarm", linewidth=1.5, density_norm="count")
    plt.title("Distribución de la Expresión Génica en Diferentes Tiempos (Separado por MW y Oven)")
    plt.xlabel("Tiempo (horas)")
    plt.ylabel("Expresión Génica")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend(title="Condición")
    plt.show()

def boxplot(expresion_genes_combined):
    """Genera un Boxplot de expresión génica"""
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Tiempo", y="Expresión", data=expresion_genes_combined, hue="Condición", palette="coolwarm")
    plt.title("Boxplot de Expresión Génica en Diferentes Tiempos")
    plt.xlabel("Tiempo (horas)")
    plt.ylabel("Expresión Génica")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend(title="Condición")
    plt.show()

def histogramas(tiempos, labels, colors):
    """Genera histogramas de expresión génica"""
    plt.figure(figsize=(12, 6))
    for tiempo, label, color in zip(tiempos, labels, colors):
        sns.histplot(tiempo.values.flatten(), kde=True, bins=30, color=color, label=label, alpha=0.5)
    plt.legend()
    plt.title("Expresión Génica en Diferentes Tiempos")
    plt.xlabel("Expresión Génica")
    plt.ylabel("Frecuencia")
    plt.show()

def scatter_plot(df_avg_8h, df_avg_14h, df_avg_24h):
    """Genera un Scatter Plot de MW vs. Oven en los tres horarios"""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharex=True, sharey=True)

    sns.scatterplot(x=df_avg_8h["MW_8h"], y=df_avg_8h["Oven_8h"], ax=axes[0], alpha=0.6, edgecolor=None)
    axes[0].set_title("Expresión en MW vs. Oven (8h)")

    sns.scatterplot(x=df_avg_14h["MW_14h"], y=df_avg_14h["Oven_14h"], ax=axes[1], alpha=0.6, edgecolor=None)
    axes[1].set_title("Expresión en MW vs. Oven (14h)")

    sns.scatterplot(x=df_avg_24h["MW_24h"], y=df_avg_24h["Oven_24h"], ax=axes[2], alpha=0.6, edgecolor=None)
    axes[2].set_title("Expresión en MW vs. Oven (24h)")

    plt.tight_layout()
    plt.show()

def volcano_plot(df, padj_column):
    """Genera un Volcano Plot con los datos de expresión génica y permite elegir la columna de p-valor ajustado"""
    # Calcular log2FC y -log10(padj_column)
    df["log2FC"] = np.log2(df.filter(like="MW").mean(axis=1) / df.filter(like="Oven").mean(axis=1))
    df["-log10(padj)"] = -np.log10(df[padj_column])  # Usar la columna de p-valor ajustado proporcionada

    # Graficar Volcano Plot
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="log2FC", y="-log10(padj)", alpha=0.7)

    # Resaltar genes significativamente expresados (padj < 0.05 y |log2FC| > 1)
    significativos = df[(df[padj_column] < 0.05) & (abs(df["log2FC"]) > 1)]
    sns.scatterplot(data=significativos, x="log2FC", y="-log10(padj)", color="red", alpha=0.8, label="Genes Diferenciales")

    plt.axhline(-np.log10(0.05), color="gray", linestyle="--", label="p-adj = 0.05")
    plt.axvline(-1, color="gray", linestyle="--")
    plt.axvline(1, color="gray", linestyle="--")
    plt.title(f"Volcano Plot - Genes Diferencialmente Expresados ({padj_column})")
    plt.xlabel("Log2 Fold Change (MW vs. Oven)")
    plt.ylabel(f"-Log10({padj_column})")
    plt.legend()
    plt.grid(True)
    plt.show()
