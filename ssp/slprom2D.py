#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:03:47 2024

@author: emir
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:03:47 2024

@author: emir
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  
from scipy.ndimage import gaussian_filter
import numpy as np
import ssp

from . import slprom1D

# Konstante

FIG_A_X_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE = 2.5
FIG_A_Y_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE = 3
FIG_B_X_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE = 2.8
FIG_B_Y_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE = 3

FIG_X_ZAJEDNICKA_RASPODJELA_VJEROVATNOCE = 3.5#4.5
FIG_Y_ZAJEDNICKA_RASPODJELA_VJEROVATNOCE = 3.5#4.5
FIG_X_ZAJEDNICKA_GUSTINA_VJEROVATNOCE = 3.5#4.5
FIG_Y_ZAJEDNICKA_GUSTINA_VJEROVATNOCE = 3.5#4.5

FIG_X_pdf_marg = 3.3 #2.5
FIG_Y_pdf_marg = 3

FIG_X_PDF_marg = 3.3 #2.5
FIG_Y_PDF_marg = 3

FIG_X_VISEDIMENZIONALNO = 3.5
FIG_Y_VISEDIMENZIONALNO = 3.5


def grafik(X, Y, F,
           x_labela ='$X$', y_labela = '$Y$', z_labela = None,
           naslov = '$F(X,Y)$',
           elevacija=30, azimut=200):
    
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
        plt.figure(figsize=(FIG_X_VISEDIMENZIONALNO , FIG_Y_VISEDIMENZIONALNO))
    else:
        plt.figure()
    
    ax = plt.axes(projection='3d');
    ax.view_init(elev=elevacija, azim=azimut)
    ax.dist = 11.5
    ax.set_xlabel(x_labela); 
    ax.set_ylabel(y_labela); 
    ax.set_zlabel(z_labela); 
    ax.set_title(naslov);
    ax.plot_surface(X, Y, F);
    # Redukcija ticksova
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
    
    plt.show()    
    
    

def realizacije(X, Y, 
                promjenljiva1 = 'X', promjenljiva2 = 'Y',
                naslov = None, legenda=None,
                dijagrami = 'sve'):        
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
    
    if (dijagrami == 'sve'):
        #crtaju se sva tri dijagrama, u protivnom samo posljednji
        
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_A_X_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE, 
                                FIG_A_Y_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE))
        else:
            plt.figure()       
        
        plt.plot(X,'b.')
        plt.title('Sl.promjenljiva $'+promjenljiva1+'$')
        plt.xlabel('$i$')
        plt.show()
        
        
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_A_X_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE, 
                                FIG_A_Y_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE))
        else:
            plt.figure()           
    
        plt.plot(Y,'b.')
        plt.title('Sl.promjenljiva $'+promjenljiva2+'$')
        plt.xlabel('$i$')
        plt.show()
           
    
    if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
        plt.figure(figsize=(FIG_B_X_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE, 
                            FIG_B_Y_REALIZACIJA_PAROVA_SLUCAJNE_PROMJENLJIVE))
    else:
        plt.figure()
        
    plt.plot(X,Y,'b.')
    if naslov == None:
        naslov = 'Parovi promjenljivih $(' + promjenljiva1 + ',' + promjenljiva2 +')$'
    plt.title(naslov)
    
    plt.xlabel('Sl.promjenljiva $'+promjenljiva1+'$')
    plt.ylabel('Sl.promjenljiva $'+promjenljiva2+'$')
    plt.axis('equal')
    plt.show()


def PDF(X, Y, step = 0.1, prosirenje_opsega = .2,
        prikaz = True,                         
        promjenljiva1 = 'X', promjenljiva2 = 'Y',
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
    raspon_y = np.max(Y) - np.min(Y)
    
    x = np.arange(np.min(X)-prosirenje_opsega*raspon_x ,
                  np.max(X)+prosirenje_opsega*raspon_x ,step)
    y = np.arange(np.min(Y)-prosirenje_opsega*raspon_y, 
                  np.max(Y)+prosirenje_opsega*raspon_y,step)
    
    Xm, Ym = np.meshgrid(x, y)
    P = np.zeros((len(x),len(y)))

    N = len(X)

    #Formiranje funkcije raspodjele vjerovatnoce
    for i in range(len(x)):
        for j in range(len(y)):        
            P[i,j]= sum(np.heaviside(x[i]-X,1) * np.heaviside(y[j]-Y,1))/N  
    
    # Prikaz ------------------------------
    if prikaz == True :
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
        
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_ZAJEDNICKA_RASPODJELA_VJEROVATNOCE, 
                                FIG_Y_ZAJEDNICKA_RASPODJELA_VJEROVATNOCE))
        else:
            plt.figure()
            
        Xm, Ym = np.meshgrid(x, y)
        ax = plt.axes(projection="3d")        
        ax.view_init(elev=30, azim=200)
        #ax.set_box_aspect(None, zoom=0.85)
        ax.dist = 11.5
        ax.plot_surface(Xm, Ym, np.transpose(P), cmap='cividis')  
        
        x_labela = promjenljiva1.lower()
        y_labela = promjenljiva2.lower()
            
        if naslov is None:
            naslov = 'Zajednička funkcija raspodjele \nvjerovatnoće P$(' + x_labela + ',' + y_labela +')$'
        ax.set_title(naslov)   
        ax.set_xlabel(x_labela)
        ax.set_ylabel(y_labela)
        
        # Redukcija ticksova
        ax.xaxis.set_major_locator(plt.MaxNLocator(4))
        ax.yaxis.set_major_locator(plt.MaxNLocator(4))
        
        plt.show()    
    
    return x, y, P



def pdf(X, Y, step = 0.1, prosirenje_opsega = .2,
        prikaz = True,                         
        promjenljiva1 = 'X', promjenljiva2 = 'Y',
        naslov = None,
        koef_filtriranja = 0):
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
    raspon_y = np.max(Y) - np.min(Y)
    
    x = np.arange(np.min(X)-prosirenje_opsega*raspon_x ,
                  np.max(X)+prosirenje_opsega*raspon_x ,step)
    y = np.arange(np.min(Y)-prosirenje_opsega*raspon_y, 
                  np.max(Y)+prosirenje_opsega*raspon_y,step)
    
    Xm, Ym = np.meshgrid(x, y)
    P = np.zeros((len(x),len(y)))

    N = len(X)

    #Formiranje funkcije raspodjele vjerovatnoce
    for i in range(len(x)):
        for j in range(len(y)):        
            P[i,j]= sum(np.heaviside(x[i]-X,1) * np.heaviside(y[j]-Y,1))/N  
    
    # Formiranje funkcije gustine vjerovatnoce
    if koef_filtriranja != 0:
        P_smooth = gaussian_filter(P, sigma = koef_filtriranja)  # sigma može biti prilagođen
        p_xy = np.diff(np.diff(P_smooth, axis=0) / step, axis=1) / step
    else:
        p_xy = np.diff(np.diff(P,1, axis = 0)/step,1, axis = 1)/step
        
    x = x[1:]
    y = y[1:]
    
    # Prikaz ------------------------------
    if prikaz == True :
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
        
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_ZAJEDNICKA_GUSTINA_VJEROVATNOCE, 
                                FIG_Y_ZAJEDNICKA_GUSTINA_VJEROVATNOCE))
        else:
            plt.figure()
            
        Xm, Ym = np.meshgrid(x, y)
        ax = plt.axes(projection="3d")        
        ax.view_init(elev=30, azim=200)
        #ax.set_box_aspect(None, zoom=0.85)
        ax.dist = 11.5
        ax.plot_surface(Xm, Ym, np.transpose(p_xy), cmap='cividis')  
        
        x_labela = promjenljiva1.lower()
        y_labela = promjenljiva2.lower()
        
        if naslov is None:                
            naslov = 'Zajednička funkcija gustine \nvjerovatnoće p$(' + x_labela + ',' + y_labela +')$'
        ax.set_title(naslov)   
        ax.set_xlabel(x_labela)
        ax.set_ylabel(y_labela)
        # Redukcija ticksova
        ax.xaxis.set_major_locator(plt.MaxNLocator(4))
        ax.yaxis.set_major_locator(plt.MaxNLocator(4))
        
        plt.show()    
        
    return x, y, p_xy
    



def pdf_marg(X = None, Y = None, step = 0.1, prosirenje_opsega = .2,
             x = None, y = None, p_xy = None, 
            prikaz = True,                         
            promjenljiva1 = 'X', promjenljiva2 = 'Y',
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
    # 1. Racunaju se iz slucajnih promjenljivih X i Y
    if p_xy is None:
        x, px = slprom1D.pdf(X, step, prosirenje_opsega, prikaz, promjenljiva1, naslov)
        y, py = slprom1D.pdf(Y, step, prosirenje_opsega, prikaz, promjenljiva2, naslov)
        
    # 2. Racunaju se iz zajednicke funkcije gustine vjerovatnoce pdf(x,y)
    else:
                 
        px = np.sum(p_xy, axis=1)*step
        py = np.sum(p_xy, axis=0)*step
    
        # Prikaz ------------------------------
        if prikaz == True :
            # 1. dijagram
            if ssp.REZOLUCIJA == "HIGH":
                plt.rcParams['figure.dpi'] = ssp.FIG_DPI
                plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
                
            if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
                plt.figure(figsize=(FIG_X_pdf_marg, 
                                    FIG_Y_pdf_marg))
            else:
                plt.figure()
                
            plt.plot(x, px,'b')
            indeks_var = promjenljiva1.lower() 
            if naslov == None:                     
                naslov = '$p_'+promjenljiva1+'(' + indeks_var + ')$'
            
            plt.title(naslov)   
            plt.xlabel('$'+indeks_var+'$')
            
            plt.show() 
            
            # 2. dijagram
            if ssp.REZOLUCIJA == "HIGH":
                plt.rcParams['figure.dpi'] = ssp.FIG_DPI
                plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
                
            if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
                plt.figure(figsize=(FIG_X_pdf_marg, 
                                    FIG_Y_pdf_marg))
            else:
                plt.figure()
                
            plt.plot(y, py,'b') 
            indeks_var = promjenljiva2.lower() 
            #if naslov is None:                     
            #doraditi!
            naslov = '$p_'+promjenljiva2+'(' + indeks_var + ')$'
            
            plt.title(naslov)   
            plt.xlabel('$'+indeks_var+'$')
            
            plt.show() 
    
    return x, px, y, py
    



def PDF_marg(X = None, Y = None, step = 0.1, prosirenje_opsega = .2,
             x = None, y = None, P_xy = None, 
            prikaz = True,                         
            promjenljiva1 = 'X', promjenljiva2 = 'Y',
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
    # 1. Racunaju se iz slucajnih promjenljivih X i Y
    if P_xy is None:
        x, Px = slprom1D.PDF(X, step, prosirenje_opsega, prikaz, promjenljiva1, naslov)
        y, Py = slprom1D.PDF(Y, step, prosirenje_opsega, prikaz, promjenljiva2, naslov)
        
    # 2. Racunaju se iz zajednicke funkcije gustine vjerovatnoce pdf(x,y)
    else:
                 
        Px = P_xy[:,-1]
        Py = P_xy[-1,:]

        # Prikaz ------------------------------
        if prikaz == True :
            # 1. dijagram
            if ssp.REZOLUCIJA == "HIGH":
                plt.rcParams['figure.dpi'] = ssp.FIG_DPI
                plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
                
            if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
                plt.figure(figsize=(FIG_X_PDF_marg, 
                                    FIG_Y_PDF_marg))
            else:
                plt.figure()
                
            plt.plot(x, Px,'b')
            indeks_var = promjenljiva1.lower() 
            if naslov == None:                     
                naslov = '$P_'+promjenljiva1+'(' + indeks_var + ')$'
            
            plt.title(naslov)   
            plt.xlabel('$'+indeks_var+'$')
            
            plt.show() 
            
            # 2. dijagram
            if ssp.REZOLUCIJA == "HIGH":
                plt.rcParams['figure.dpi'] = ssp.FIG_DPI
                plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
                
            if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
                plt.figure(figsize=(FIG_X_PDF_marg, 
                                    FIG_Y_PDF_marg))
            else:
                plt.figure()
                
            plt.plot(y, Py,'b') 
            indeks_var = promjenljiva2.lower() 
            #if naslov is None:                     
            #doraditi!                    
            naslov = '$P_'+promjenljiva2+'(' + indeks_var + ')$'
            
            plt.title(naslov)   
            plt.xlabel('$'+indeks_var+'$')
            
            plt.show() 
    
    return x, Px, y, Py    