# ##Download related packages
# install.packages("tidyverse")
# install.packages("openxlsx")
# install.packages("rlang")
# install.packages("reshape2")

library(tidyverse)
library(openxlsx)
library(rlang)
library(reshape2)
##Global reference
open_path="C:/Users/22193/Desktop/Case2/case2-Loc-filter/data"
save_path="C:/Users/22193/Desktop/Case2/case2-Loc-filter/output"
type_name="Subcellular.location.[CC]"
type_class=c("Cytoplasm","Nucleus","Cell membrane","Secreted",
             "cytoskeleton","Cell projection","Endoplasmic reticulum membrane",
             "Mitochondrion","Golgi apparatus")
###Work area
##Read in files
special_name=dir(open_path)%>%
  str_replace_all(".xlsx","")
special_data=openxlsx::read.xlsx(paste0(open_path,"/",special_name,".xlsx"),sheet=1)%>%
  rename(type = eval(type_name))

##Screening needs to be sorted
##Regular expression compilation for classification of global variables
type_class_match=str_c(type_class,collapse = "|")
type_filter=str_subset(special_data[["type"]],type_class_match)
special_data_filter=filter(special_data,type %in% type_filter)
special_data_filter[["type"]]=map(special_data_filter[["type"]],function(x) 
  str_extract_all(x,type_class_match))%>%
  modify( function(x) unique(reduce(x,cbind)))
# ##Replace with standard name
# special_data_filter[["type"]]=modify(special_data_filter[["type"]],function(x)
#   str_replace_all(x,c("Single-pass"="Single-pass membrane protein","Multi-pass"="Multi-pass membrane protein")))
# special_data_filter=as.data.frame(special_data_filter)
##Save results
write.xlsx(special_data_filter,paste0(save_path,"/",special_name,"_case2.xlsx"))
