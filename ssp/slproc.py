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

FIG_X_REALIZACIJE_PROCESA = 6
FIG_Y_REALIZACIJE_PROCESA = 3

FIG_X_PDF_PROCESI = 8
FIG_Y_PDF_PROCESI = 8

FIG_X_pdf_PROCESI = 8
FIG_Y_pdf_PROCESI = 8

FIG_X_KORELACIONA = 3.7
FIG_Y_KORELACIONA = 3.7

FIG_X_KORELACIONA_STACIONARNA = 6
FIG_Y_KORELACIONA_STACIONARNA = 3



def realizacije(t, X_t, indeksi=[0], signal2=None, b=None, signal3=None,
            x_labela ='$t$', y_labela = None, naslov = None, 
            promjenljiva = 'X', legenda=None):
    
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
        plt.figure(figsize=(FIG_X_REALIZACIJE_PROCESA , FIG_Y_REALIZACIJE_PROCESA ))
    else:
        plt.figure()
    
    for i in indeksi:
        plt.plot(t, X_t[i,:])
    
    plt.title(naslov)
    plt.xlabel(x_labela)
    plt.ylabel(y_labela)
    
    if legenda is not None:
        plt.legend(legenda, loc='upper right', framealpha=1)
    else:
        legenda = []
        for i in indeksi:
            legenda.append('$'+promjenljiva+'_{'+str(i)+'}(t)$')
        
        plt.legend(legenda, loc='upper right', framealpha=1)
    
    plt.show()




def PDF(t, X_t, step = 0.1, prosirenje_opsega = 0.2, 
        prikaz = True,
        naslov = '$P(t,x)$',
        x_labela = '$t$', y_labela = '$x$'):
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
    M, N = np.shape(X_t)
    
    raspon_x = np.max(X_t) - np.min(X_t)
    x = np.arange(np.min(X_t)-prosirenje_opsega*raspon_x ,
                  np.max(X_t)+prosirenje_opsega*raspon_x ,step)
    
    
    P_t_x = np.empty((len(x),N))
    
    for t_i in range(N):
        # slucajna promjenljiva X(t_1)
        x_ti = X_t[:,t_i]
        P_x = np.zeros((len(x))) 
            
        for i in range(len(x)):
            P_x[i] = sum (np.heaviside(x[i]-x_ti, 1))/N
        
        P_t_x[:,t_i] = P_x
        
    
    if prikaz == True:
        Tm, Xm = np.meshgrid(t, x)
                    
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
            
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_PDF_PROCESI , FIG_Y_PDF_PROCESI ))
        else:
            plt.figure()
        
        ax = plt.axes(projection='3d');
        ax.view_init(elev=20, azim=200)
        ax.set_xlabel(x_labela); 
        ax.set_ylabel(y_labela); 
        ax.set_title(naslov);
        ax.plot_surface(Tm, Xm, P_t_x);
        
        plt.show() 
    
    return t, x, P_t_x


def pdf(t, X_t, step = 0.1, prosirenje_opsega = 0.2, 
        prikaz = True,
        naslov = '$p(t,x)$',
        x_labela = '$t$', y_labela = '$x$'):
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
    M, N = np.shape(X_t)
    
    raspon_x = np.max(X_t) - np.min(X_t)
    x = np.arange(np.min(X_t)-prosirenje_opsega*raspon_x ,
                  np.max(X_t)+prosirenje_opsega*raspon_x ,step)
    
    p_t_x = np.empty((len(x)-1,N))
    P_t_x = np.empty((len(x),N))
    
    for t_i in range(N):
        # slucajna promjenljiva X(t_1)
        x_ti = X_t[:,t_i]
        P_x = np.zeros((len(x))) 
        p_x = np.zeros((len(x)-1)) 

        for i in range(len(x)):
            P_x[i] = sum (np.heaviside(x[i]-x_ti, 1))/N
        
        P_t_x[:,t_i] = P_x
        
        p_x = np.diff(P_x)/step
        p_t_x[:,t_i] = p_x
    
    x = x[1:]
    
    if prikaz == True:
        Tm, Xm = np.meshgrid(t, x)
        
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
            
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_pdf_PROCESI , FIG_Y_pdf_PROCESI ))
        else:
            plt.figure()
        
        ax = plt.axes(projection='3d');
        ax.view_init(elev=20, azim=200)
        ax.set_xlabel(x_labela); 
        ax.set_ylabel(y_labela); 
        ax.set_title(naslov);
        ax.plot_surface(Tm, Xm, p_t_x);
        
        plt.show() 
    
    return t, x, p_t_x




def korelacija(X_t, Y_t, tip = 'obicna', 
               promjenljiva1 = 'X',
               promjenljiva2 = 'Y',
               prikaz = True,
               naslov = None,
               x_labela = '$t_1$', y_labela = '$t_2$'):
    """
    Opis
    
    Args:
        param1 (float): dafadsfsa
        param2 (float): dsafdfa

        style - plot, stem, dots
    Returns:
        float: dfafdsa
    """
    N = X_t.shape[1]  # broj kolona
    M = Y_t.shape[1]
                
    Kor_fja = np.empty((N, M))

    if tip == 'obicna':
        # Određivanje korelacionih funkcija:
        for t1 in range(N):
            for t2 in range(M):
                Kor_fja[t1,t2] = np.mean(X_t[:, t1] * Y_t[:, t2])
    if tip == 'centrirana':
        eta_X_t = np.mean(X_t, axis=0)
        eta_Y_t = np.mean(Y_t, axis=0)
        # Određivanje korelacionih funkcija:
        for t1 in range(N):
            for t2 in range(M):
                Kor_fja[t1,t2]  = np.mean((X_t[:, t1] - eta_X_t[t1]) * (Y_t[:, t2] - eta_Y_t[t2]))
   
    if prikaz == True:                    
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
                
        fig, ax = plt.subplots(figsize=(FIG_X_KORELACIONA, FIG_Y_KORELACIONA))
        
        #transponujemo da zadrzimo reprezentaciju (t1,t2)
        ax.matshow(Kor_fja.T, cmap=plt.cm.Blues) 
        ax.xaxis.set_ticks_position('bottom') 
        plt.xlabel(x_labela)
        plt.ylabel(y_labela)
        plt.title(naslov)
        plt.show()

    return Kor_fja
            


def korelacija_stacionarna(R, delta_t,
                           prikaz = True,
                           naslov= None):

    # Formiranje autokorelacione fje R(tau) (tau= t1-t2, za t2=0, tau ide od 0 do t1max)
    R_xx_tau = R[:, 0]
    tau_vektor = np.arange(0, len(R_xx_tau) * delta_t, delta_t)
    
    if prikaz == True:                    
        if ssp.REZOLUCIJA == "HIGH":
            plt.rcParams['figure.dpi'] = ssp.FIG_DPI
            plt.rcParams['savefig.dpi'] = ssp.FIG_DPI
        if ssp.FORMATIRANJE_PRIKAZA == "BOOK":
            plt.figure(figsize=(FIG_X_KORELACIONA_STACIONARNA,
                        FIG_Y_KORELACIONA_STACIONARNA))
        else:
            plt.figure()        
            
        plt.plot(tau_vektor, R_xx_tau,'b')
        plt.title(naslov)
        plt.xlabel("$\\tau$")
        plt.show()

    return tau_vektor, R_xx_tau

