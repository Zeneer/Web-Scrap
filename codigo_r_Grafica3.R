# Instala ggplot2 si no lo tienes instalado
# install.packages("ggplot2")

# Carga la librería ggplot2
library(ggplot2)

# Generar un porcentaje aleatorio para el nivel de egreso
porcentaje_egreso <- runif(1, 0, 100)

# Crear un marco de datos para el nivel de egreso
datos_egreso <- data.frame(Nivel = "Egreso", Porcentaje = porcentaje_egreso)

# Crear un gráfico de barras cartesiano con un color rojo más fuerte
grafico_egreso_cartesiano <- ggplot(datos_egreso, aes(x = Nivel, y = Porcentaje, fill = Nivel)) +
  geom_bar(stat = "identity", width = 0.5, color = "black", fill = "darkred") +
  labs(title = "Nivel de Egreso de la Universidad") +
  theme_minimal() +
  theme(legend.position = "none")

# Mostrar el gráfico cartesiano de egreso
print(grafico_egreso_cartesiano)

# Guardar el gráfico cartesiano de egreso como una imagen JPG
ggsave("grafico_egreso_cartesiano_rojo.jpg", grafico_egreso_cartesiano, width = 6, height = 6, dpi = 300)
