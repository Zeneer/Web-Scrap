# Generar un porcentaje aleatorio para el nivel de egreso
porcentaje_egreso <- runif(1, 0, 100)

# Crear un marco de datos para el nivel de egreso
datos_egreso <- data.frame(Nivel = "Egreso", Porcentaje = porcentaje_egreso)

# Crear un gráfico de barras cartesiano con un color azul
grafico_egreso_cartesiano <- ggplot(datos_egreso, aes(x = Nivel, y = Porcentaje, fill = Nivel)) +
  geom_bar(stat = "identity", width = 0.5, color = "black", fill = "steelblue") +
  labs(title = "Nivel de Egreso de la Universidad") +
  theme_minimal() +
  theme(legend.position = "none")

# Mostrar el gráfico cartesiano de egreso
print(grafico_egreso_cartesiano)

# Guardar el gráfico cartesiano de egreso como una imagen JPG
ggsave("grafico_egreso_cartesiano_azul.jpg", grafico_egreso_cartesiano, width = 6, height = 6, dpi = 300)
