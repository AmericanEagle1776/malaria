#!/usr/bin/env Rscript

suppressPackageStartupMessages(install.packages("parallel"))
suppressPackageStartupMessages(install.packages("dMod"))
suppressPackageStartupMessages(install.packages("ggplot2"))

options(scipen=999)
suppressPackageStartupMessages(library(dMod))

reactionList <- list(
Reaction0		= "(IN - R0_kcat_b * s1)",
Reaction1		= "(R1_kcat_f * s1 - R1_kcat_b * s2)",
Reaction2		= "(R2_kcat_f * s2)"
)

f <- eqnvec(
			s1 = paste0("1*", reactionList["Reaction0"],"-1*", reactionList["Reaction1"]),
			s2 = paste0("1*", reactionList["Reaction1"],"-1*", reactionList["Reaction2"])
						)

# ODE model
model <- odemodel(f, modelname = "toymodel", compile=TRUE)

x <- Xs(model)

observables <- eqnvec(
					  s1_obs = "s1",
					  s2_obs = "s2"
					  )

g <- Y(observables, f, compile = TRUE, modelname = "obsfn", attach.input = FALSE)
innerpars <- getParameters(g*x)
trafo <- structure(paste0("exp(log_", innerpars, ")"), names = innerpars)
trafo["IN"] <- 5#if you remove this the parameters become unidentfiable
trafo["R0_kcat_b"] <- 3 #if you remove this the parameters become unidentfiable
trafo["R1_kcat_b"] <- 2 #if you remove this the parameters become unidentfiable

p <- NULL
p <- p + P(trafo, condition = "data")

outerpars <- getParameters(p)
pouter <- structure(rep(0, length(outerpars)), names=outerpars)

fluxTimes <- c(0,10,15,20)
data.df <- data.frame(name=character(),
					 time=numeric(), 
					 value=numeric(), 
					 sigma=numeric(),
					 stringsAsFactors=FALSE)
data.df <- rbind(data.df, data.frame(
								   name = paste0("s1_obs"),
								   time = fluxTimes,
								   value = c(1.0, 1.2, 1.3, 1.3),
								   sigma = 0.1,
								   stringsAsFactors = FALSE
								   )
)
data.df <- rbind(data.df, data.frame(
								   name = paste0("s2_obs"),
								   time = fluxTimes,
								   value = c(2.1, 2.2, 2.3, 2.3),
								   sigma = 0.1,
								   stringsAsFactors = FALSE
								   )
)

# write.table(data.df, "~/data.txt")

# data.df <- read.table("~/data.txt")

dataList <- list()
dataList[["data"]] <- data.df
dataList <- as.datalist(dataList)

obj <- normL2(dataList, g*x*p)
myfit <- trust(obj, pouter, studyname = "SS", rinit = 1, rmax = 10000, iterlim = 100)

maxtime <- 20
times <- seq(0,maxtime,length.out=(maxtime*100+1))
notFittedResult <- (g*x*p)(times, pouter)
fittedResult <- (g*x*p)(times, myfit$argument)
names(fittedResult) <- "fitted"
names(notFittedResult) <- "not fitted"
results <- c(fittedResult, notFittedResult)
plot(results, dataList)
print(paste0("Not fitted obj: ", obj(pouter)$value, " Fitted obj: ", obj(myfit$argument)$value))

suppressPackageStartupMessages(library(parallel))
availableCores = 4
profiles <- do.call(rbind, 
						mclapply(names(myfit$argument), 
								 function(n) profile(obj, myfit$argument, n), 
								 mc.cores = availableCores, mc.preschedule = FALSE)
						)
invisible(readline(prompt="Press [enter] to continue"))

suppressPackageStartupMessages(library(ggplot2))
plotProfile(profiles) + ggtitle("Profiles of the parameters")
