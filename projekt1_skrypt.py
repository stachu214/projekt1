# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:33:56 2024

@author: Stanisław
"""
import sys

import numpy as np


class Transfromacje:
    """Klasa zawierająca transformacje w formie metod klasy"""
    
    def __init__(self, elipsoida: list):
        """Inicjalizacja instancji klasy przyjmująca jako argument listę parametór elipsoidy"""
        self.a = elipsoida[0]
        self.e2 = elipsoida[1]
    
    def Npu(self, fi: float):
        return self.a / np.sqrt(1 - self.e2 * np.sin(fi)**2)
    

    def XYZ2BLH(self, X: float, Y: float, Z: float):
        p = np.sqrt(X**2 + Y**2)
        f = np.arctan(Z / (p * (1 - self.e2)))
        while True:
            N = self.Npu(f)
            h = (p / np.cos(f)) - N
            fs = f
            f = np.arctan(Z / (p * (1 - self.e2 * (N / (N + h)))))
            if np.abs(fs - f) < (0.000001 / 206265):
                break
        l = np.arctan2(Y, X)    
        return f'{np.rad2deg(f)} {np.rad2deg(l)} {h} \n'


    def BLH2XYZ(self,fi,lam,h):
        N = self.Npu(fi)
        X = (N+h)*np.cos(fi)*np.cos(lam)
        Y = (N+h)*np.cos(fi)*np.sin(lam)
        Z = (N*(1-self.e2)+h)*np.sin(fi)   
        return f'{X} {Y} {Z} \n'
        
    
    def PL1992(self,fi,lama,m=0.9993):  
        lama0 = np.deg2rad(19)
  
        b2 = self.a**2*(1-self.e2)
        ep2 = (self.a**2-b2)/b2
        dellama = lama - lama0
        t = np.tan(fi)
        ni2 = ep2*(np.cos(fi)**2)
        N = self.Npu(fi)
     
        A0 = 1- (self.e2/4)-(3*self.e2**2/64)-(5*self.e2**3/256)
        A2 = (3/8)*(self.e2+(self.e2**2/4)+(15*self.e2**3/128))
        A4 = (15/256)*(self.e2**2+((3*self.e2**3)/4))
        A6 = (35*self.e2**3)/3072
        sigma = self.a *(A0*fi-A2*np.sin(2*fi)+A4*np.sin(4*fi)-A6*np.sin(6*fi))

        xgk =  sigma    +    ( ((dellama**2/2)*N*np.sin(fi)*np.cos(fi))    *    (1   +   ((dellama**2/12)*(np.cos(fi)**2)*(5 - t**2 + 9*ni2 + 4*ni2**2))      +         ((dellama**4/360)*(np.cos(fi)**4)*(61 - 58*t**2 + t**4 + 270*ni2 - 330*ni2*t**2))))
        ygk =  (dellama* N * np.cos(fi))  *   ( 1 +  ((dellama**2/6)   *   (np.cos(fi)**2)   *  (1 - t**2 + ni2))     +     (((dellama**4/120)*(np.cos(fi)**4)) * (5 - (18*t**2) + t**4 + (14 * ni2) - (58*ni2*t**2))))
        x92 = xgk * m - 5300000
        y92 = ygk*m + 500000
        
        return f'{x92} {y92} \n'
        
    def PL2000(self,fi,lama,m=0.999923):
        
        lama = np.deg2rad(lama)
        if lama >np.deg2rad(13.5) and lama < np.deg2rad(16.5):
            strefa = 5
            lama0 = np.deg2rad(15)
        elif lama >np.deg2rad(16.5) and lama < np.deg2rad(19.5):
            strefa = 6
            lama0 = np.deg2rad(18)
        elif lama >np.deg2rad(19.5) and lama < np.deg2rad(22.5):
            strefa =7
            lama0 = np.deg2rad(21)
        elif lama >np.deg2rad(22.5) and lama < np.deg2rad(25.5):
            strefa = 8
            lama0 = np.deg2rad(24)
        
        b2 = self.a**2*(1-self.e2)    
        ep2 = (self.a**2-b2)/b2
        dellama = lama - lama0
        t = np.tan(fi)
        ni2 = ep2*(np.cos(fi)**2)
        N = self.Npu(fi)
             
        A0 = 1- (self.e2/4)-(3*self.e2**2/64)-(5*self.e2**3/256)
        A2 = (3/8)*(self.e2+(self.e2**2/4)+(15*self.e2**3/128))
        A4 = (15/256)*(self.e2**2+((3*self.e2**3)/4))
        A6 = (35*self.e2**3)/3072
            
        sigma = self.a *(A0*fi-A2*np.sin(2*fi)+A4*np.sin(4*fi)-A6*np.sin(6*fi))
            
        xgk =  sigma    +    ( ((dellama**2/2)*N*np.sin(fi)*np.cos(fi))    *    (1   +   ((dellama**2/12)*(np.cos(fi)**2)*(5 - t**2 + 9*ni2 + 4*ni2**2))      +         ((dellama**4/360)*(np.cos(fi)**4)*(61 - 58*t**2 + t**4 + 270*ni2 - 330*ni2*t**2))))
        ygk =  (dellama* N * np.cos(fi))  *   ( 1 +  ((dellama**2/6)   *   (np.cos(fi)**2)   *  (1 - t**2 + ni2))     +     (((dellama**4/120)*(np.cos(fi)**4)) * (5 - (18*t**2) + t**4 + (14 * ni2) - (58*ni2*t**2))))
            
        x2000 = xgk * m 
        y2000 = ygk*m + (strefa *1000000) +500000
            
        return f'{x2000} {y2000} \n'
        
    
    def Rneu(self, phi, lam):
        Rneu = np.array([[-np.sin(phi)*np.cos(lam), -np.sin(lam), np.cos(phi)*np.cos(lam)],
                         [-np.sin(phi)*np.sin(lam), np.cos(lam), np.cos(phi)*np.sin(lam)],
                         [np.cos(phi), 0, np.sin(phi)]])
        
        return Rneu
    
    def XYZ2NEUP(self, X, Y, Z, X0, Y0, Z0):
        p = np.sqrt(X0**2+Y0**2)
        fi = np.arctan(Z0/(p*(1-self.e2)))
        while True:
            N = self.Npu(fi)
            h = (p/np.cos(fi)) - N
            fi_poprzednia = fi
            fi = np.arctan((Z0/p)/(1-((N*self.e2)/(N+h))))
            if abs(fi_poprzednia-fi)<(0.000001/206265):
                break 
        N = self.Npu(fi)
        h = p/np.cos(fi) - N
        lam = np.arctan(Y0/X0)
        
        R_neu = self.Rneu(fi, lam)

        X_sr = [X-X0, Y-Y0, Z-Z0] 
        X_rneu = R_neu.T@X_sr
            
        return f'{str(X_rneu.T)} \n'


# funkcja rozpoczynająca program 
if __name__ == "__main__":

    elipsoidy = {
        'WGS84':[6378137.000, 0.00669438002290],
        'GRS80':[6378137.000, 0.00669438002290],
        'KRASOWSKI':[6378245.000, 0.00669342162296],
        }
    transformacje = {
        'XYZ2BLH': 'XYZ2BLH',
        'BLH2XYZ': 'BLH2XYZ',
        'PL2000':'PL2000',
        'PL1992':'PL1992',
        'XYZ2NEUP':'XYZ2NEUP'
    }

    argumenty = sys.argv[1:]
    
    