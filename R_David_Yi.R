duplicados <- Telco.Customer.tvc[duplicated(Telco.Customer.tvc$customerID), "customerID"]
if (length(duplicados) > 0) {
  print("Hay valores de customerID duplicados:")
  print(duplicados)
} else {
  print("No hay repetidos.")
}


vacios <- Telco.Customer.tvc[which(Telco.Customer.tvc$customerID == " "), "customerID"]
if (length(vacios) > 0) {
  print("Hay valores vacíos:")
  print(vacios)
} else {
  print("No hay vacíos.")
}



clientesunicos <- length(unique(Telco.Customer.tvc$customerID))
print(paste("Número de clientes únicos", clientesunicos))


options(max.print = 20000)
tienen1 <- length(Telco.Customer.tvc[which(Telco.Customer.tvc$SeniorCitizen==1),"customerID"])
print(tienen1)

options(max.print = 20000)
tienen0 <- length(Telco.Customer.tvc[which(Telco.Customer.tvc$SeniorCitizen==0),"customerID"])
print(tienen0)

suma <- tienen1+tienen0
print(suma)


options(max.print = 20000)
male <- length(Telco.Customer.tvc[which(Telco.Customer.tvc$gender=="Male"),"customerID"])
print(male)

options(max.print = 20000)
female <- length(Telco.Customer.tvc[which(Telco.Customer.tvc$gender=="Female"),"customerID"])
print(female)


clientes_desertores <- length(Telco.Customer.tvc[which(Telco.Customer.tvc$Churn=="Yes"),"customerID"])
print(clientes_desertores)

clientes_no_desertores <- length(Telco.Customer.tvc[which(Telco.Customer.tvc$Churn=="No"),"customerID"])
print(clientes_no_desertores)

totalclientes = clientes_desertores + clientes_no_desertores
print(totalclientes)

porcentaje_clientes_desertores = (clientes_desertores/totalclientes) * 100
print(porcentaje_clientes_desertores)

porcentaje_clientes_no_desertores = (clientes_no_desertores/totalclientes) * 100
print(porcentaje_clientes_no_desertores)

