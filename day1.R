#### Advent of Code 2020 Day 1 puzzle ####
rm(list=ls())
dat <- read.csv('C:/Users/Daniel.Feeney/Desktop/AdventOfCode2020/day1Inputs.csv')

for (i in c(1:199)){
  tmpVal <- dat[i,]
    for (j in c(1:199)){
      tmpVal2 <- dat[j,]
      if (tmpVal + tmpVal2 == 2020) {
        print(tmpVal * tmpVal2)
      }
    }
}


for (i in c(1:199)){
  tmpVal <- dat[i,]
  for (j in c(1:199)){
    tmpVal2 <- dat[j,]
    for (k in c(1:199)){
      tmpVal3 <- dat[k,]
    }
      if (tmpVal + tmpVal2 + tmpVal3 == 2020) {
        print(tmpVal * tmpVal2 * tmpVal3)
    }
  }
}

arrFunc <- function(inputdat, n) {
  
  sum <- 0
  for (i in c(1:199)){
    sum = sum + (inputdat[i,] * (2*n))
    if (sum == 2020){
    }
  }
  return(i)
}
arrFunc(dat, length(dat))
