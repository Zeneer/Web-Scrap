# Instala ggplot2 si no lo tienes instalado
# install.packages("ggplot2")

# Carga la librería ggplot2
library(ggplot2)

# Generar un porcentaje aleatorio para el nivel de bullying
porcentaje_bullying <- runif(1, 0, 100)

# Crear un marco de datos para el nivel de bullying
datos_bullying <- data.frame(Nivel = "Bullying", Porcentaje = porcentaje_bullying)

# Crear un gráfico de barras cartesiano con un color verde
grafico_bullying_cartesiano <- ggplot(datos_bullying, aes(x = Nivel, y = Porcentaje, fill = Nivel)) +
  geom_bar(stat = "identity", width = 0.5, color = "black", fill = "darkgreen") +
  labs(title = "Nivel de Bullying") +
  theme_minimal() +
  theme(legend.position = "none")

# Mostrar el gráfico cartesiano de bullying
print(grafico_bullying_cartesiano)

# Guardar el gráfico cartesiano de bullying como una imagen JPG
ggsave("grafico_bullying_cartesiano_verde.jpg", grafico_bullying_cartesiano, width = 6, height = 6, dpi = 300)
