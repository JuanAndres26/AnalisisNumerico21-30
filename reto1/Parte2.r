#lectura de datos de las estaciones
crato <- read.csv("Crato.csv") #leer los datos del csv
santana <- read.csv("Santana do Cariri.csv") #leer los datos del csv
jati <- read.csv("Jati.csv") #leer los datos del csv

datosCrato = crato$Temp..do.Ar.2m.ºC.
datosSantana = santana$Temp..do.Ar.2m.ºC.
datosJati = jati$Temp..do.Ar.2m.ºC.

tam = length(datosCrato)
porcentaje = length(datosSantana)
toma = sort(sample(1:length(datosSantana),porcentaje, replace = F))
datosSantana = datosSantana[toma]
plot(1:length(datosCrato), datosCrato, type="l",xlab = "Indices ideales",ylab = "Temperatura del aire",main = "Temperatura")
legend(660, 16.5, legend=c("Crato"),
       col=c("black"), lty=1:2, cex=0.6)

#interpolacion por spline cubico Santana
spli = spline(toma,datosSantana,n=length(datosCrato))
for(i in spli){
  spli$y[i] = round(spli$y[i],2)
}
plot(1:length(datosCrato),datosCrato,type="l",xlab = "Indices ideales",ylab = "Temperatura del aire",main = "Temperatura")
lines(1:length(datosCrato),spli$y,col="red")
legend(600,17, legend=c("Crato", "Spline cubico (Santana)"),
       col=c("black", "red"),lty=1:2, cex=0.5)

#interpolacion lineal Santana
l<-approx(toma, datosSantana, method = "linear", n=length(datosCrato))
for(i in l){
  l$y[i] = round(l$y[i],2)
}
plot(1:length(datosCrato),datosCrato,type="l",xlab = "Indices ideales",ylab = "Temperatura del aire",main = "Temperatura")
lines(1:length(datosCrato),l$y,col="green")
legend(630,17, legend=c("Crato", "Lineal (Santana)"),
       col=c("black", "green"), lty=1:2, cex=0.5)

porcentaje = length(datosJati)
toma = sort(sample(1:length(datosJati),porcentaje, replace = F))
datosJati = datosJati[toma]

#interpolacion por spline cubico Jati
spli2 = spline(toma,datosJati,n=length(datosCrato))
for(i in spli2){
  spli2$y[i] = round(spli2$y[i],2)
}
plot(1:length(datosCrato),datosCrato,type="l",xlab = "Indices ideales",ylab = "Temperatura del aire",main = "Temperatura")
lines(1:length(datosCrato),spli2$y,col="red")
  legend(610,17, legend=c("Crato", "Spline cubico (Jati)"),
       col=c("black", "red"),lty=1:2, cex=0.5)

#interpolacion lineal Jati
l2<-approx(toma, datosJati, method = "linear", n=length(datosCrato))
for(i in l2){
  l2$y[i] = round(l2$y[i],2)
}
plot(1:length(datosCrato),datosCrato,type="l",xlab = "Indices ideales",ylab = "Temperatura del aire",main = "Temperatura")
lines(1:length(datosCrato),l2$y,col="green")
legend(650,17, legend=c("Crato", "Lineal (Jati)"),
       col=c("black", "green"), lty=1:2, cex=0.5)

#Calculo de errores
#Error con los datos de Santana
errorSplineCubico <- c()
errorLineal <- c()
errorSplineCubicoSq <- c()
errorLinealSq <- c()
jspline = 0
jlineal = 0

for(i in 1:length(datosCrato)){
  #error spline cubico
  e = 0
  e = abs(datosCrato[i]-spli$y[i])
  if(e < 0.5){
    jspline = jspline + 1
  }
  esq = e^2
  errorSplineCubico<- c(errorSplineCubico,e)
  errorSplineCubicoSq<- c(errorSplineCubicoSq,esq)
  #error interpolacion lineal
  e = 0
  e = abs(datosCrato[i]-l$y[i])
  if(e < 0.5){
    jlineal = jlineal + 1
  }
  esq = e^2
  errorLineal<- c(errorLineal,e)
  errorLinealSq<- c(errorLinealSq,esq)
} 

#Error con los datos de Jati
errorSplineCubico2 <- c()
errorLineal2 <- c()
errorSplineCubico2Sq <- c()
errorLineal2Sq <- c()
jspline2 = 0
jlineal2 = 0

for(i in 1:length(datosCrato)){
  #error spline cubico
  e = 0
  e = abs(datosCrato[i]-spli2$y[i])
  if(e < 0.5){
    jspline2 = jspline2 + 1
  }
  esq = e^2
  errorSplineCubico2<- c(errorSplineCubico2,e)
  errorSplineCubico2Sq<- c(errorSplineCubico2Sq,esq)
  #error interpolacion lineal
  e = 0
  e = abs(datosCrato[i]-l2$y[i])
  if(e < 0.5){
    jlineal2 = jlineal2 + 1
  }
  esq = e^2
  errorLineal2<- c(errorLineal2,e)
  errorLineal2Sq<- c(errorLineal2Sq,esq)
} 

#Impresion de errores con datos de Santana y de Jati
#Santana
cat("error minimo del spline cubico (Santana)",round(min(errorSplineCubico),2),'\n')
cat("error maximo del spline cubico (Santana)",round(max(errorSplineCubico),2),'\n')
cat("error absoluto medio del spline cubico (Santana)",round((sum(errorSplineCubico))/tam,2),'\n')
cat("error cuadratico medio del spline cubico (Santana)",round(sqrt((sum(errorSplineCubicoSq))/tam),2),'\n')
ijaccardSC = (jspline/length(datosCrato))*100
cat("indice de Jaccard del spline cubico (Santana)",round(ijaccardSC,2),'\n') #grado de similitud entre dos conjuntos

cat("error minimo  de la interpolacion lineal (Santana)",round(min(errorLineal),2),'\n')
cat("error maximo de la interpolacion lineal (Santana)",round(max(errorLineal),2),'\n')
cat("error absoluto medio de la interpolacion lineal (Santana)",round((sum(errorLineal))/tam,2),'\n')
cat("error cuadratico medio de la interpolacion lineal (Santana)",round(sqrt((sum(errorLinealSq))/tam),2),'\n')
ijaccardL = (jlineal/length(datosCrato))*100
cat("indice de Jaccard de la interpolacion lineal (Santana)",round(ijaccardL,2),'\n') #grado de similitud entre dos conjuntos

#Jati
cat("error minimo del spline cubico (Jati)",round(min(errorSplineCubico2),2),'\n')
cat("error maximo del spline cubico (Jati)",round(max(errorSplineCubico2),2),'\n')
cat("error absoluto medio del spline cubico (Jati)",round((sum(errorSplineCubico2))/tam,2),'\n')
cat("error cuadratico medio del spline cubico (Jati)",round(sqrt((sum(errorSplineCubico2Sq))/tam),2),'\n')
ijaccardSC2 = (jspline2/length(datosCrato))*100
cat("indice de Jaccard del spline cubico (Jati)",round(ijaccardSC2,2),'\n') #grado de similitud entre dos conjuntos

cat("error minimo  de la interpolacion lineal (Jati)",round(min(errorLineal2),2),'\n')
cat("error maximo de la interpolacion lineal (Jati)",round(max(errorLineal2),2),'\n')
cat("error absoluto medio de la interpolacion lineal (Jati)",round((sum(errorLineal2))/tam,2),'\n')
cat("error cuadratico medio de la interpolacion lineal (Jati)",round(sqrt((sum(errorLineal2Sq))/tam),2),'\n')
ijaccardL2 = (jlineal2/length(datosCrato))*100
cat("indice de Jaccard de la interpolacion lineal (Jati)",round(ijaccardL2,2),'\n') #grado de similitud entre dos conjuntos