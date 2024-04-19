#####################################
#### PYTHON CODE FOR CONDITION #####
ESCALA_SALARIAL01 = 34685.00
result = GROSS > ESCALA_SALARIAL01



#####################################
#### PYTHON CODE FOR COMPUTATION #####


ESCALA_SALARIAL01 = 34685.00

# SFSDEPT ONLY IS IN SOME SALARY STRUCTURE 
DEDUCCIONES = SFS + AFP + SFSDEPT if 'SFSDEPT' in locals() or 'SFSDEPT' in globals() else SFS + AFP

# SFS y AFP son negativos! 
# Esto vendria siendo, ej.:  35000 + -2000 = 33000
CALCULO = GROSS  + DEDUCCIONES
result = - (CALCULO - ESCALA_SALARIAL01) * 0.15