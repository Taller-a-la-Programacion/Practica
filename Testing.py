import Portafolio2A;
import pytest;
    
def test_numeroAbundate_1():
    assert Portafolio2A.numeroAbundante(12) == True
def test_numeroAbundate_2():
    assert Portafolio2A.numeroAbundante(8) == False
def test_numeroAbundate_3():
    assert isinstance(Portafolio2A.numeroAbundante(-8), str) == isinstance("Error: La entrada, debe ser número positivo", str)    
    
#############################################################################################

def test_adyacentesImpares_1():
    assert Portafolio2A.adyacentesImpares (9252783) == True 
    
def test_adyacentesImpares_2():
    assert Portafolio2A.adyacentesImpares (51730) == False
    
def test_adyacentesImpares_3():
    assert Portafolio2A.adyacentesImpares (5836) == True
    
def test_adyacentesImpares_4():
    assert isinstance(Portafolio2A.adyacentesImpares (-9), str) == isinstance("Error: Número debe ser positivo", str)
    
#############################################################################################

def test_convertirNumero_1():
    assert Portafolio2A.convertirNumero(12558, 4) == 16258
def test_convertirNumero_2():
    assert Portafolio2A.convertirNumero(-94161, 5) == -916
def test_convertirNumero_3():
    assert Portafolio2A.convertirNumero(8517210, 5) == 511680720
def test_convertirNumero_4():
    assert isinstance(Portafolio2A.convertirNumero('8517210', 5), str) == isinstance("Error: Debe ser entero", str)    
    
#############################################################################################

def test_comprimirNumero_1():
    assert Portafolio2A.comprimirNumero (15532) == 1532 
def test_comprimirNumero_2():
    assert Portafolio2A.comprimirNumero (82581534) == 281534
def test_comprimirNumero_3():
    assert Portafolio2A.comprimirNumero (-82581534) == -281534    
def test_comprimirNumero_4():
    assert isinstance(Portafolio2A.comprimirNumero('82581534'), str) == isinstance("Error: Debe ser entero", str)     

############################################################################################    
    
def test_numeroHermano_1():
    assert Portafolio2A.numeroHermano(20)  == True
def test_numeroHermano_2():
    assert Portafolio2A.numeroHermano(8) == False
def test_numeroHermano_3():
    assert isinstance(Portafolio2A.numeroHermano(-8), str) == isinstance("Error: La entrada, debe ser número positivo", str)    
    
#############################################################################################

def test_adyacentesPares_1():
    assert Portafolio2A.adyacentesPares(6241753) == True 
    
def test_adyacentesPares_2():
    assert Portafolio2A.adyacentesPares(32820) == False
    
def test_adyacentesPares_3():
    assert Portafolio2A.adyacentesPares(5726) == True
    
def test_adyacentesPares_4():
    assert isinstance(Portafolio2A.adyacentesPares(-9), str) == isinstance("Error: Número debe ser positivo", str)
    
#############################################################################################

def test_convertirNumero2_1():
    assert Portafolio2A.convertirNumero2(25682525, 4) == 2632855
def test_convertirNumero2_2():
    assert Portafolio2A.convertirNumero2(-943161, 3) == -4931
def test_convertirNumero2_3():
    assert Portafolio2A.convertirNumero2(7210, 10) == 2100
def test_convertirNumero2_4():
    assert isinstance(Portafolio2A.convertirNumero2('7210', 10), str) == isinstance("Error: Debe ser entero", str)      
    
#############################################################################################
    
def test_superPrimo_1():
    assert Portafolio2A.superPrimo(807491)  == True
def test_superPrimoo_2():
    assert Portafolio2A.superPrimo(12) == False
def test_superPrimo_3():
    assert isinstance(Portafolio2A.superPrimo(-8), str) == isinstance("Error: La entrada, debe ser número positivo", str)    
    
#############################################################################################

def test_adyacentes_1():
    assert Portafolio2A.adyacentes(6242754) == True 
    
def test_adyacentes_2():
    assert Portafolio2A.adyacentes(41830) == False
    
def test_adyacentes_3():
    assert Portafolio2A.adyacentes(8736) == True
    
def test_adyacentes_4():
    assert isinstance(Portafolio2A.adyacentes(-9), str) == isinstance("Error: Número debe ser positivo", str)
    
#############################################################################################

def test_convertirNumero3_1():
    assert Portafolio2A.convertirNumero3(25682525, 4) == 262055
def test_convertirNumero3_2():
    assert Portafolio2A.convertirNumero3(-943161, 3) == -4101
def test_convertirNumero3_3():
    assert Portafolio2A.convertirNumero3(7210, 10) == 20
def test_convertirNumero3_4():
    assert isinstance(Portafolio2A.convertirNumero3('7210', 10), str) == isinstance("Error: Debe ser entero", str)        
