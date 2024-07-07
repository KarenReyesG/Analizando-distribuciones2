import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'heart_failure_data_ETL.csv'
data = pd.read_csv(file_path)

# Definir las categorías
categorias = ['No', 'Sí']  # Cambié las etiquetas a "No" y "Sí"

# Configurar el layout de subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Gráfico de sectores para anémicos
anemia_counts = data['anaemia'].value_counts()
axes[0, 0].pie(anemia_counts, labels=categorias[:len(anemia_counts)], autopct="%1.1f%%")
axes[0, 0].set_title('Anémicos')

# Gráfico de sectores para diabéticos
diabetes_counts = data['diabetes'].value_counts()
axes[0, 1].pie(diabetes_counts, labels=categorias[:len(diabetes_counts)], autopct="%1.1f%%")
axes[0, 1].set_title('Diabéticos')

# Gráfico de sectores para fumadores
smoking_counts = data['smoking'].value_counts()
axes[1, 0].pie(smoking_counts, labels=categorias[:len(smoking_counts)], autopct="%1.1f%%")
axes[1, 0].set_title('Fumadores')

# Gráfico de sectores para muertes
death_counts = data['DEATH_EVENT'].value_counts()
axes[1, 1].pie(death_counts, labels=categorias[:len(death_counts)], autopct="%1.1f%%")
axes[1, 1].set_title('Muertes')

# Ajustar el layout y mostrar el gráfico
fig.suptitle('Distribución de variables categóricas')
plt.tight_layout()
plt.show()