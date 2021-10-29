aiuaba <- read.csv("Aiuaba.csv") #leer los datos del csv
humedad <-aiuaba$Umidade.Relativa.do.Ar.2m....

#Datos al 70%
tam<-length(humedad)
por<-tam*0.7
sorteado<-sort(sample(1:tam,por, replace = F))
faltantes<-1:tam
faltantes <- faltantes[-sorteado]
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
legend(626, 40, legend=c("Aiuaba"),
       col=c("black"), lty=1:2, cex=0.8)

#El primer y ultimo punto de los datos sorteados (70%)
if(sorteado[1] != 1){
  faltantes[1] = sorteado[1]
  sorteado[1] = 1
}
if(sorteado[length(sorteado)] != tam){
  faltantes[length(faltantes)] = sorteado[length(sorteado)]
  sorteado[length(sorteado)] = tam
}
datos<-humedad[sorteado] #70% de los datos aleatoriamente seleccionados

print(sorteado)
print(datos)

#interpolacion por spline cubico 70%
spli<-spline(sorteado, datos, n=tam)
for(i in spli){
  spli$y[i] = round(spli$y[i],2)
}
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
lines(1:tam, spli$y, col="red")
legend(580, 41, legend=c("Aiuaba", "Spline cubico (70%)"),
       col=c("black", "red"), lty=1:2, cex=0.7)

#interpolacion de tipo Hermite 70%
c <- splinefun(sorteado, datos)
print(c)
c<-c(1:tam)
for(i in 1:tam){
  c[i] = round(c[i],2)
}
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
lines(1:tam, c, col="blue")
legend(610, 41, legend=c("Aiuaba", "Hermite (70%)"),
       col=c("black", "blue"), lty=1:2, cex=0.7)
 
#interpolacion lineal 70%
l <-approx(sorteado, datos, method = "linear", n=tam)
for(i in l){
  l$y[i] = round(l$y[i],2)
}
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
lines(1:tam, l$y, col="green")
legend(620, 41, legend=c("Aiuaba", "Lineal (70%)"),
       col=c("black", "green"), lty=1:2, cex=0.7)


#50% de los datos
por2<-tam*0.5
sorteado2<-sort(sample(1:tam,por2, replace = F))
faltantes2<-1:tam
faltantes2 <- faltantes2[-sorteado2]
datos2<-humedad[sorteado2] #50% de los datos aleatoriamente seleccionados

#El primer y ultimo punto de los datos sorteados (50%)
if(sorteado2[1] != 1){
  faltantes2[1] = sorteado2[1]
  sorteado2[1] = 1
}
if(sorteado2[length(sorteado2)] != tam){
  faltantes2[length(faltantes2)] = sorteado2[length(sorteado2)]
  sorteado2[length(sorteado2)] = tam
}

#interpolacion por spline cubico 50%
spli2<-spline(sorteado2, datos2, n=tam)
for(i in spli2){
  spli2$y[i] = round(spli2$y[i],2)
}
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
lines(1:tam, spli2$y, col="red")
legend(580, 41, legend=c("Aiuaba", "Spline cubico (50%)"),
       col=c("black", "red"), lty=1:2, cex=0.7)

#interpolacion de tipo Hermite 50%
c2 <- splinefun(sorteado2, datos2 )
c2<-c2(1:tam)
for(i in 1:tam){
  c2[i] = round(c2[i],2)
}
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
lines(1:tam, c2, col="blue")
legend(610, 41, legend=c("Aiuaba", "Hermite (50%)"),
       col=c("black", "blue"), lty=1:2, cex=0.7)

#interpolacion lineal 50%
l2 <-approx(sorteado2, datos2, method = "linear", n=tam)
for(i in l2){
  l2$y[i] = round(l2$y[i],2)
}
plot(1:tam, humedad , type="l",xlab = "Indices ideales",ylab = "Humedad relativa",main = "Humedad")
lines(1:tam, l2$y, col="green")
legend(620, 41, legend=c("Aiuaba", "Lineal (50%)"),
       col=c("black", "green"), lty=1:2, cex=0.7)

#Calculo de errores
#Error con el 70% de los datos
errorSplineCubico <- c()
errorHermite <- c()
errorLineal <- c()
errorSplineCubicoSq <- c()
errorHermiteSq <- c()
errorLinealSq <- c()
jspline = 0
jlineal = 0
jhermite = 0

for(i in faltantes){
  #error spline cubico
  e = 0
  e = abs(humedad[i]-spli$y[i])
  if(e < 0.5){
    jspline = jspline + 1
  }
  esq = e^2
  errorSplineCubico<- c(errorSplineCubico,e)
  errorSplineCubicoSq<- c(errorSplineCubicoSq,esq)
  #error Hermite
  e = 0
  e = abs(humedad[i]- c[i])
  if(e < 0.5){
    jhermite = jhermite + 1
  }
  esq = e^2
  errorHermite<- c(errorHermite,e)
  errorHermiteSq<- c(errorHermiteSq,esq)
  #error interpolacion lineal
  e = 0
  e = abs(humedad[i]-l$y[i])
  if(e < 0.5){
    jlineal = jlineal + 1
  }
  esq = e^2
  errorLineal<- c(errorLineal,e)
  errorLinealSq<- c(errorLinealSq,esq)
} 

#Error con el 50% de los datos
errorSplineCubico2 <- c()
errorHermite2 <- c()
errorLineal2 <- c()
errorSplineCubico2Sq <- c()
errorHermite2Sq <- c()
errorLineal2Sq <- c()
jspline2 = 0
jlineal2 = 0
jhermite2 = 0

for(i in faltantes2){
  #error spline cubico
  e = 0
  e = abs(humedad[i]-spli2$y[i])
  if(e < 0.5){
    jspline2 = jspline2 + 1
  }
  esq = e^2
  errorSplineCubico2<- c(errorSplineCubico2,e)
  errorSplineCubico2Sq<- c(errorSplineCubico2Sq,esq)
  #error Hermite
  e = 0
  e = abs(humedad[i]- c2[i])
  if(e < 0.5){
    jhermite2 = jhermite2 + 1
  }
  esq = e^2
  errorHermite2<- c(errorHermite2,e)
  errorHermite2Sq<- c(errorHermite2Sq,esq)
  #error interpolacion lineal
  e = 0
  e = abs(humedad[i]-l2$y[i])
  if(e < 0.5){
    jlineal2 = jlineal2 + 1
  }
  esq = e^2
  errorLineal2<- c(errorLineal2,e)
  errorLineal2Sq<- c(errorLineal2Sq,esq)
} 

#Impresion de errores con el 70% y 50% de los datos
#70%
cat("error minimo del spline cubico (70%)",min(errorSplineCubico),'\n')
cat("error maximo del spline cubico (70%)",max(errorSplineCubico),'\n')
cat("error absoluto medio del spline cubico (70%)",round((sum(errorSplineCubico))/tam,2),'\n')
cat("error cuadratico medio del spline cubico (70%)",round(sqrt((sum(errorSplineCubicoSq))/tam),2),'\n')
ijaccardSC = (jspline/length(faltantes))*100
cat("indice de Jaccard del spline cubico (70%)",round(ijaccardSC,2),"%",'\n') #grado de similitud entre dos conjuntos

cat("error minimo interpolacion de tipo Hermite (70%)",min(errorHermite),'\n')
cat("error maximo interpolacion de tipo Hermite (70%)",max(errorHermite),'\n')
cat("error absoluto medio interpolacion de tipo Hermite (70%)",round((sum(errorHermite))/tam,2),'\n')
cat("error cuadratico medio interpolacion de tipo Hermite (70%)",round(sqrt((sum(errorHermiteSq))/tam),2),'\n')
ijaccardSC = (jhermite/length(faltantes))*100
cat("indice de Jaccard interpolacion de tipo Hermite (70%)",round(ijaccardSC,2),"%",'\n') #grado de similitud entre dos conjuntos

cat("error minimo  de la interpolacion lineal (70%)",min(errorLineal),'\n')
cat("error maximo de la interpolacion lineal (70%)",max(errorLineal),'\n')
cat("error absoluto medio de la interpolacion lineal (70%)",round((sum(errorLineal))/tam,2),'\n')
cat("error cuadratico medio de la interpolacion lineal (70%)",round(sqrt((sum(errorLinealSq))/tam),2),'\n')
ijaccardL = (jlineal/length(faltantes))*100
cat("indice de Jaccard de la interpolacion lineal (70%)",round(ijaccardL,2),"%",'\n') #grado de similitud entre dos conjuntos

#50%
cat("error minimo del spline cubico (50%)",min(errorSplineCubico2),'\n')
cat("error maximo del spline cubico (50%)",max(errorSplineCubico2),'\n')
cat("error absoluto medio del spline cubico (50%)",round((sum(errorSplineCubico2))/tam,2),'\n')
cat("error cuadratico medio del spline cubico (50%)",round(sqrt((sum(errorSplineCubico2Sq))/tam),2),'\n')
ijaccardSC2 = (jspline2/length(faltantes2))*100
cat("indice de Jaccard del spline cubico (50%)",round(ijaccardSC2,2),"%",'\n') #grado de similitud entre dos conjuntos

cat("error minimo interpolacion de tipo Hermite (50%)",min(errorHermite2),'\n')
cat("error maximo interpolacion de tipo Hermite (50%)",max(errorHermite2),'\n')
cat("error absoluto medio interpolacion de tipo Hermite (50%)",round((sum(errorHermite2))/tam,2),'\n')
cat("error cuadratico medio interpolacion de tipo Hermite (50%)",round(sqrt((sum(errorHermite2Sq))/tam),2),'\n')
ijaccardSC2 = (jhermite2/length(faltantes2))*100
cat("indice de Jaccard interpolacion de tipo Hermite (50%)",round(ijaccardSC2,2),"%",'\n') #grado de similitud entre dos conjuntos

cat("error minimo  de la interpolacion lineal (50%)",min(errorLineal2),'\n')
cat("error maximo de la interpolacion lineal (50%)",max(errorLineal2),'\n')
cat("error absoluto medio de la interpolacion lineal (50%)",round((sum(errorLineal2))/tam,2),'\n')
cat("error cuadratico medio de la interpolacion lineal (50%)",round(sqrt((sum(errorLineal2Sq))/tam),2),'\n')
ijaccardL2 = (jlineal2/length(faltantes2))*100
cat("indice de Jaccard de la interpolacion lineal (50%)",round(ijaccardL2,2),"%",'\n') #grado de similitud entre dos conjuntos


