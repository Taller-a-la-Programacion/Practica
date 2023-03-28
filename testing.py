import Practica;
import pytest;
    

#############################################################################################

def test_convertirNumero_1():
    assert Practica.convertirNumero(12558, 4) == 16258
def test_convertirNumero_2():
    assert Practica.convertirNumero(-94161, 5) == -916
def test_convertirNumero_3():
    assert Practica.convertirNumero(8517210, 5) == 511680720
def test_convertirNumero_4():
    assert isinstance(Practica.convertirNumero('8517210', 5), str) == isinstance("Error: Debe ser entero", str)  
    
#############################################################################################   
    
def test_invertirLista_1():
    assert Practica.invertirLista([5,8,45,96]) == [96, 45, 8, 5]
    
def test_invertirLista_2():
    assert Practica.invertirLista([56, 85,8,45,96]) == [96, 45, 8, 85, 56]

def test_invertirLista_2():
    assert isinstance(Practica.invertirLista([]), str) == isinstance("Error: La lista debe contener al menos 2 elementos", str)

def test_invertirLista_2():
    assert isinstance(Practica.invertirLista([2,5,7,"ABC"]), str) == isinstance("Error: La lista debe contener elementos tipo entero", str)
    
    
#####################################################################################################

def test_extremosLista_1():
    assert Practica.extremosLista([18,5,8,45,96, 60]) == [5,96]

def test_extremosLista_2():
    assert Practica.extremosLista([96, 96,96]) == [96]

def test_extremosLista_3():
    assert isinstance(Practica.extremosLista([]), str) == isinstance("Error: La lista debe contener al menos 2 elementos", str)

def test_extremosLista_4():
    assert isinstance(Practica.extremosLista([2,5,7,"ABC"]), str) == isinstance("Error: La lista debe contener elementos tipo entero", str)
