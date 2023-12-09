# Instala ggplot2 si no lo tienes instalado
# install.packages("ggplot2")

# Carga la librería ggplot2
library(ggplot2)

# Datos
motivos <- c("Falta de dinero", "Perdida de interés en los estudios")
porcentajes <- c(50, 30)

# Crear un marco de datos
datos <- data.frame(Motivo = motivos, Porcentaje = porcentajes)

# Crear un gráfico de barras
grafico <- ggplot(datos, aes(x = Motivo, y = Porcentaje, fill = Motivo)) +
  geom_bar(stat = "identity", width = 0.5, color = "black") +
  labs(title = "Motivos de Deserción") +
  theme_minimal() +
  theme(legend.position = "none")

# Mostrar el gráfico
print(grafico)

# Guardar el gráfico como una imagen JPG
ggsave("grafico_desercion_total.jpg", grafico, width = 6, height = 6, dpi = 300)
