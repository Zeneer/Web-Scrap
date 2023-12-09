# Generar un porcentaje aleatorio para la deserción
porcentaje_desercion <- runif(1, 0, 100)

# Definir el motivo de la deserción
motivo_desercion <- c("Falta de interés", "Problemas personales", "Falta de apoyo")

# Crear un marco de datos para la deserción
datos_desercion <- data.frame(Motivo = motivo_desercion, Porcentaje = porcentaje_desercion)

# Crear un gráfico de barras cartesiano con un color rojo
grafico_desercion_cartesiano <- ggplot(datos_desercion, aes(x = Motivo, y = Porcentaje, fill = Motivo)) +
  geom_bar(stat = "identity", width = 0.5, color = "black", alpha = 0.7) +
  labs(title = "Nivel de Deserción con Motivos") +
  theme_minimal() +
  theme(legend.position = "none")

# Mostrar el gráfico cartesiano de deserción
print(grafico_desercion_cartesiano)

# Guardar el gráfico cartesiano de deserción como una imagen JPG
ggsave("grafico_desercion_cartesiano_motivos.jpg", grafico_desercion_cartesiano, width = 8, height = 6, dpi = 300)
