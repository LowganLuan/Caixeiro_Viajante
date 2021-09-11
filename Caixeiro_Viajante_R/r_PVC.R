aleatorio   <- read.table("aleatorio.txt")
semi_guloso <- read.table("semi_guloso.txt")
guloso      <- read.table("guloso.txt")

aleatorio = as.numeric(aleatorio)
mean(aleatorio)
sd(aleatorio)

semi_guloso = as.numeric(semi_guloso)
mean(semi_guloso)
sd(semi_guloso)

guloso = as.numeric(guloso)
mean(guloso)
sd(guloso)

boxplot(aleatorio,
        semi_guloso,
        guloso,
        names = c("Aleatório", "SemiGuloso", "Guloso"),
        border = c("blue", "green", "brown"),
        varwidth = TRUE)