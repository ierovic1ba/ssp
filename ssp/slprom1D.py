#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:03:47 2024

@author: emir
"""

import matplotlib.pyplot as plt
import numpy as np
import ssp

# Konstante

FIG_X_SIGNALI = 3
FIG_Y_SIGNALI = 3

FIG_X_REALIZACIJA_SLUCAJNE_PROMJENLJIVE = 6
FIG_Y_REALIZACIJA_SLUCAJNE_PROMJENLJIVE = 3

FIG_X_PDF = 3.3#2.9
FIG_Y_PDF = 3

FIG_X_pdf = 3.3#2.9
FIG_Y_pdf = 3

    

def grafik(n, signal1 , m=None, signal2=None, b=None, signal3=None,
            stil1='b', stil2='r', stil3='g', 
            x_labela ='$t$', y_labela = None, naslov = None, 
            legenda=None, lokacija_lgd = 'upper right'):
    
    """
    Opis
    
    Args:
        param1 (float): dafadsfsa
        param2 (float): dsafdfa

        style - plot, stem, dots
    Returns:
        float: dfafdsa
    """
    if ssp.REZOLUCIJA == "HIGH":
        plt.rcParams['figure.dpi'] = ssp.FIG_DPI
        plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
        
    if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
        plt.figure(figsize=(FIG_X_SIGNALI , FIG_Y_SIGNALI))
    else:
        plt.figure()
    
    if (signal1 is not None):
        if n is None:
            n = np.arange(len(signal1))
        plt.plot(n, signal1, stil1)
    
    if (signal2 is not None):
        plt.plot(m, signal2, stil2)
        
    if (signal3 is not None):
        plt.plot(b, signal3, stil3)
    
    plt.title(naslov)
    plt.xlabel(x_labela)
    plt.ylabel(y_labela)
    
    if legenda is not None:
        plt.legend(legenda, loc=lokacija_lgd, framealpha=1)
    
    plt.show()
     

def realizacije(n, signal1, m=None, signal2=None,
                stil1='b.', stil2='r',
                x_labela='Realizacija', y_labela = None, naslov = None, 
                legenda=None):
        
        """
        Opis
        
        Args:
            param1 (float): dafadsfsa
            param2 (float): dsafdfa

            style - plot, stem, dots
        Returns:
            float: dfafdsa
        """
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
            
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_REALIZACIJA_SLUCAJNE_PROMJENLJIVE , 
                                FIG_Y_REALIZACIJA_SLUCAJNE_PROMJENLJIVE))
        else:
            plt.figure()
        
        if (signal1 is not None):
            # ovo su tipicno tackice
            plt.plot(n, signal1, stil1)
        
        if (signal2 is not None):
            # ovo je linija ocekivanih vrijednosti ili slicno
            if isinstance(signal2, float):
                signal2 = signal2 * np.ones(len(m))  # Ako je float, proširi ga na niz
            plt.plot(m, signal2, stil2)

        
        plt.title(naslov)
        plt.xlabel(x_labela)
        plt.ylabel(y_labela)
        
        if legenda is not None:
            plt.legend(legenda, loc='upper right', framealpha=1)
        
        plt.show()


def PDF(X, step = 0.1, prosirenje_opsega = 0.2, 
        prikaz = True,
        promjenljiva = 'X',
        naslov = None):
    """
    Opis
    
    Args:
        param1 (float): dafadsfsa
        param2 (float): dsafdfa

        style - plot, stem, dots
    Returns:
        float: dfafdsa
    """
    
    # Izracun ------------------------------
    raspon_x = np.max(X) - np.min(X)
    x = np.arange(np.min(X)-prosirenje_opsega*raspon_x ,
                  np.max(X)+prosirenje_opsega*raspon_x ,step)
    
    N = len(X)
    P_x = np.zeros((len(x))) 
    for i in range(len(x)):
        P_x[i] = sum (np.heaviside(x[i]-X, 1))/N
            
    
    # Prikaz ------------------------------
    if prikaz == True :
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
            
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_PDF, 
                                FIG_Y_PDF))
        else:
            plt.figure()
            
        plt.plot(x, P_x,'b')      
        indeks_var = promjenljiva.lower()  
        if naslov == None:            
            naslov = '$P_'+promjenljiva+'(' + indeks_var + ')$'
        
        plt.title(naslov)   
        plt.xlabel('$'+indeks_var+'$')
        
        plt.show()                
        
        
    return x, P_x


def pdf(X, step = 0.1, prosirenje_opsega = 0.2, 
        prikaz = True,
        promjenljiva = 'X',
        naslov = None):
    """
    Opis
    
    Args:
        param1 (float): dafadsfsa
        param2 (float): dsafdfa

        style - plot, stem, dots
    Returns:
        float: dfafdsa
    """
    
    # Izracun ------------------------------
    raspon_x = np.max(X) - np.min(X)
    x = np.arange(np.min(X)-prosirenje_opsega*raspon_x ,
                  np.max(X)+prosirenje_opsega*raspon_x ,step)
    
    N = len(X)
    P_x = np.zeros((len(x))) 
    for i in range(len(x)):
        P_x[i] = sum (np.heaviside(x[i]-X, 1))/N
           
    p_x = np.diff(P_x)/step
    x = x[1:]
    
    # Prikaz ------------------------------
    if prikaz == True :
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
            
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_pdf, 
                                FIG_Y_pdf))
        else:
            plt.figure()
            
        plt.plot(x, p_x,'b')      
        indeks_var = promjenljiva.lower() 
        if naslov == None:             
            naslov = '$p_'+promjenljiva+'(' + indeks_var + ')$'
        
        plt.title(naslov)   
        plt.xlabel('$'+indeks_var+'$')
        
        plt.show()                
        
        
    return x, p_x


            
       