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

def heatmap(df_avg_8h, df_avg_14h, df_avg_24h, top_genes):
    """Genera un Heatmap con los 20 genes más expresados comparando MW y Oven"""
    df_top_avg_8h = df_avg_8h.loc[top_genes]
    df_top_avg_14h = df_avg_14h.loc[top_genes]
    df_top_avg_24h = df_avg_24h.loc[top_genes]

    fig, axes = plt.subplots(1, 3, figsize=(18, 8))

    sns.heatmap(df_top_avg_8h, annot=True, cmap="coolwarm", linewidths=0.5, ax=axes[0])
    axes[0].set_title("Expresión en 8h (MW vs. Oven)")

    sns.heatmap(df_top_avg_14h, annot=True, cmap="coolwarm", linewidths=0.5, ax=axes[1])
    axes[1].set_title("Expresión en 14h (MW vs. Oven)")

    sns.heatmap(df_top_avg_24h, annot=True, cmap="coolwarm", linewidths=0.5, ax=axes[2])
    axes[2].set_title("Expresión en 24h (MW vs. Oven)")

    plt.tight_layout()
    plt.show()
