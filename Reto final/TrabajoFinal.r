SIR.model <- function(t, b, g){ # function of t, b and g
  require(deSolve) # call in of the deSolve package
  N = 4500
  init <- c(S=1-(10/4500),I=10/4500,R=0)
  parameters <- c(beta=b,gamma=g) #paramters in the ode
  time <- seq(0,t,by=t/(2*length(1:t))) #time sequence for the ode solution
  eqn <- function(time,state,parameters){ #SIR odes
    with(as.list(c(state,parameters)),{ #so lve the ode using the parameters
      dS <- -beta*S*I #change in proportion of susceptibles (dS/dt)
      dI <- beta*S*I-gamma*I #change in proportion of infected (dI/dt)
      dR <- gamma*I #change in proportion of the recovered (dR/dt)
      return(list(c(dS,dI,dR)))}) #out as a list containing the values
  }
  out<-ode(y=init,times=time,eqn,parms=parameters, method = "rk4") #solve the ode using ode() in deSolve package
  out.df<-as.data.frame(out) #create a data frame of the output of ode()
  require(ggplot2) #call in ggplot2 package
  mytheme4 <- theme_minimal()
  theme_set(mytheme4) #http://docs.ggplot2.org/current/theme_update.html
  title <- bquote("Propagación de la pandemia por Covid-19 en Santa Marta") #title for plot
  subtit<-bquote(list(beta==.(parameters[1]),~gamma==.(parameters[2]))) #use of bquote to include Greek symbols of beta and gamma into subtitle
  res<-ggplot(out.df,aes(x=time))+ #set plot of ode data frame output and x-variable as time
    ggtitle(bquote(atop(bold(.(title)),atop(bold(.(subtit))))))+ # create the title and subtitle based on http://stackoverflow.com/q/30338719/6168956
    geom_line(aes(y=S,colour="Susceptibles"))+ #assign plot line as S from out.df
    geom_line(aes(y=I,colour="Infectados"))+ #assign plot line as I from out.df
    geom_line(aes(y=R,colour="Recuperados"))+ #assign plot line as R from out.df
    ylab(label="Proporción")+ #y-axis label
    xlab(label="Tiempo (días)")+ #x-axis label
    theme(legend.justification=c(1,0), legend.position=c(1,0.5))+ #legend justification - anchorpoint of legend, legend.position based on two-element numeric vector (x,y)
    theme(legend.title=element_text(size=12,face="bold"), #set font specification of title
          legend.background = element_rect(fill='#FFFFFF',size=0.5,linetype="solid"), #legend background set to white
          legend.text=element_text(size=10), #set legend text size
          legend.key=element_rect(colour="#FFFFFF", #set legend keys border to white
                                  fill='#C2C2C2', #fill set to gray
                                  size=0.25, #size of border
                                  linetype="solid"))+ #line type of border
    scale_colour_manual("Líneas", #title of legend
                        breaks=c("Susceptibles","Infectados","Recuperados"), #each level of lines, set to colour
                        values=c("blue","red","darkgreen")) #colours for each respective level
  print(res) #print output of plot
  ggsave(plot=res, # call plot name
         filename=paste0("SIRplot_","time",t,"beta",b,"gamma",g,".png"), #set the filename with parameters of time, beta and gamma
         width=5.75,height=4,dpi=120) #dimensions and resolution of .png file
  getwd() #display working directory for saved .png file location
  ic = g/(b*c)
  c <- which(out.df[['S']]<ic)-1
}
SIR.model(365,0.6,0.21)
Beta<-0.6
c <-3.5
gama<- 0.21
N1<-4500
I0<-10/N1
S0<-1-I0
R0<-0
p<-1
#SOlucion analitica del modelo SI
#dj = 1000000 * e^(0.8x) / (e^(1000000*c) + e^(0.8x))
#c = 0.0000115129154
analitica <- function(x) {
  r <- 4500 * exp(0.6*x) / (exp((4500)*3.5) + exp(0.6*x))
  return(r)
}
plot(t,resultados,type = "l",lwd = 2,main="Modelo SI (Susceptible-infectados) Solucion analitica\nCRv2(Code red 1)\nJulio 19 de 2001",xlab= "t(horas)",ylab = "# de infectados")
resultados = c()
for(i in t){
  resultados = c(resultados,analitica(i))
}
d<-365
S<-function(x,y,z,t) -Beta*x*y
I<-function(x,y,z,t) Beta*x*y-gama*y
R<-function(x,y,z,t) gama*y
vS<-replicate(d+1,0)
vI<-replicate(d+1,0)
vR<-replicate(d+1,0)
vS[1]<-S0
vI[1]<-I0
vR[1]<-R0
p<-2
while(p<=d+1){
  xi<-vS[p-1]
  yi<-vI[p-1]
  zi<-vR[p-1]
  k1<-p*S(xi,yi,zi,ti)
  l1<-p*I(xi,yi,zi,ti)
  m1<-p*R(xi,yi,zi,ti)
  k2<-p*S(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+p/2)
  l2<-p*I(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+p/2)
  m2<-p*R(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+p/2)
  k3<-p*S(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+p/2)
  l3<-p*I(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+p/2)
  m3<-p*R(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+p/2)
  k4<-p*S(xi+k3,yi+l3,zi+m3,ti+p)
  l4<-p*I(xi+k3,yi+l3,zi+m3,ti+p)
  m4<-p*R(xi+k3,yi+l3,zi+m3,ti+p)
  vS[p]<-xi+(1/6)*(k1+2*k2+2*k3+k4)
  vI[p]<-yi+(1/6)*(l1+2*l2+2*l3+l4)
  vR[p]<-zi+(1/6)*(m1+2*m2+2*m3+m4)
  p<-p+1
}
mi<- max(vI)
mi*N1
dmi<-which.max(vI)
dmi
mr<- max(vR)
MaxRec*N1
dmaxrec <- which.max(vR)
dmaxrec
pi<- mi
pi
pr<- mr
pr
cr<-integer(d)
for (i in 1:d){
  if (gama/(Beta*vI[i])>vS[i]){
    cr[i]<-1
  } 
}
plot(cr)
vr<- integer(60)
for(i in 1:60){
  vr[i]<-Beta*c*vS[i]/(gama*N1)   #(Beta*vI[i]*vS[i])/gama
}
max(vr)
plot(vr, type="l")
d <- 71
vS2<-replicate(d+1,0)
vI2<-replicate(d+1,0)
vR2<-replicate(d+1,0)
vS2[1]<-1
vI2[1]<-14
vR2[1]<-0
p<-2
while(p<=d+1){
  xi<-vS[p-1]
  yi<-vI[p-1]
  zi<-vR[p-1]
  k1<-p*S(xi,yi,zi,ti)
  l1<-p*I(xi,yi,zi,ti)
  m1<-p*R(xi,yi,zi,ti)
  k2<-p*S(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+p/2)
  l2<-p*I(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+p/2)
  m2<-p*R(xi+(1/2)*k1,yi+(1/2)*l1,zi+(1/2)*m1,ti+p/2)
  k3<-p*S(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+p/2)
  l3<-p*I(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+p/2)
  m3<-p*R(xi+(1/2)*k2,yi+(1/2)*l2,zi+(1/2)*m2,ti+p/2)
  k4<-p*S(xi+k3,yi+l3,zi+m3,ti+p)
  l4<-p*I(xi+k3,yi+l3,zi+m3,ti+p)
  m4<-p*R(xi+k3,yi+l3,zi+m3,ti+p)
  vS2[p]<-xi+(1/6)*(k1+2*k2+2*k3+k4)
  vI2[p]<-yi+(1/6)*(l1+2*l2+2*l3+l4)
  vR2[p]<-zi+(1/6)*(m1+2*m2+2*m3+m4)
  p<-p+1
}
plot(vS2, type="l", col="blue",axes=F,xlab = "Dias",ylab="Porcentaje")
par(new=TRUE)
plot(vI2, type="l",col="red",axes=F,xlab = "Dias",ylab="Porcentaje")
par(new=TRUE)
plot(vR2, type="l",col="black",xlab = "Dias",ylab="Porcentaje")
title(main="Contagio real de Covid-19 en Santa Marta")
legend(x = "right", legend = c("Susceptibles", "Infectados", "Recuperados"), fill = c("blue", "red","black"),box.lty=0)
tablaErrores<-matrix(0:0, nrow=10, ncol=12)
tablaErrores<-data.frame(tablaErrores)
colnames(tablaErrores)<-c("SusceptibleReal","SusceptibleAprox", "ErrorrelativoS","ErrorAbsolutoS",
                          "InfectadosReal", "InfectadosAprox", "ErrorrelativoI","ErrorAbsolutoI",
                          "RecuperadosReal","RecuperadosAprox", "ErrorrelativoR", "ErrorAbsolutoR")
tablaErrores$SusceptibleReal<-vS2[1:10]
tablaErrores$SusceptibleAprox<-vS[1:10]
tablaErrores$InfectadosReal<-vI2[1:10]
tablaErrores$InfectadosAprox<-vI[1:10]
tablaErrores$RecuperadosReal<-vR2[1:10]
tablaErrores$RecuperadosAprox<-vR[1:10]
for (i in 1:10){ 
  tablaErrores$ea[i]<-abs(vS[i]-vS2[i])
  tablaErrores$er[i]<-tablaErrores$er[i]/vS[i]
  tablaErrores$eai[i]<-abs(vI[i]-vI2[i])
  tablaErrores$eri[i]<-tablaErrores$eri[i]/vI[i]
  tablaErrores$ear[i]<-abs(vR[i]-vR2[i])
  tablaErrores$err[i]<-tablaErrores$err[i]/vR[i]
}
View(tablaErrores)
