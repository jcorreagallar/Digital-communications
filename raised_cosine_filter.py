import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact

#Mathematic expression's
def raisedCosineFilter(f,beta,sample_rate):
  T = 1/sample_rate
  f = abs(f)

  if f <= (1-beta)/(2*T):
    return 1
  if f > (1-beta)/(2*T) and f <= (1+beta)/(2*T):
    return 1/2 * (1 + np.cos((np.pi*T/beta) * (f - (1-beta)/(2*T))))
  else:
    return 0 

def impulseResponse(t,beta,sample_rate):
  T = 1/sample_rate

  from ipywidgets import interact
import numpy as np
import matplotlib.pyplot as plt
 
#Mathematic expression's
def raisedCosineFilter(f,beta,sample_rate):
  T = 1/sample_rate
  f = abs(f)
 
  if f <= (1-beta)/(2*T):
    return 1
  if f > (1-beta)/(2*T) and f <= (1+beta)/(2*T):
    return 1/2 * (1 + np.cos((np.pi*T/beta) * (f - (1-beta)/(2*T))))
  else:
    return 0 
 
def impulseResponse(t,beta,sample_rate):
  T = 1/sample_rate

  try:
    t == T/(2*beta)
    return np.pi/(4*T) * np.sinc(1/(2*beta))
  except:
    return (1/T) * np.sinc(t/T) * np.cos(np.pi*beta*t/T)/(1-(2*beta*t/T)**2)
                                                  
#Plotting function
def plot_filter(band_width,beta,sample_rate):
  upper = band_width/2
  lower = -upper 
  f = np.linspace(lower,upper,100)
 
  #Frequency response of raised-cosine filter
  hf = np.array([raisedCosineFilter(pos, beta, sample_rate) for pos in f])
  
  #Impulse response of raised-cosine filter
  t = np.power(f,-1)
  ht = np.array([impulseResponse(pos,beta,sample_rate) for pos in t])
 
  #Plot frequency response of raised-cosine filter
  plt.figure(figsize=(14,3))
  plt.subplot(1,2,1)
  plt.plot(f,hf)
  plt.grid()
  plt.title('Frequency response')
  plt.xlabel('Frequency')
  plt.ylabel('Amplitude')
 
  #Plot impulse response of raised-cosine filter
  plt.subplot(1,2,2)
  plt.plot(t ,ht)
  plt.grid()
  plt.title('Impulse response')
  plt.xlabel('Time')
  plt.ylabel('Amplitude')
  plt.show()
 
@interact(band_width= (30000,100000,5000), beta=(0,1,0.1),sample_rate = (5000,20000,1000))
def call(band_width,beta,sample_rate):
  plot_filter(band_width,beta,sample_rate)

#Plotting function
def plot_filter(band_width,beta,sample_rate):
  upper = band_width/2
  lower = -upper 
  f = np.linspace(lower,upper,100)

  #Frequency response of raised-cosine filter
  hf = np.array([raisedCosineFilter(pos, beta, sample_rate) for pos in f])
  
  #Impulse response of raised-cosine filter
  t = np.power(f,-1)
  ht = np.array([impulseResponse(pos,beta,sample_rate) for pos in t])
 
  #Plot frequency response of raised-cosine filter
  plt.figure(figsize=(14,3))
  plt.subplot(1,2,1)
  plt.plot(f,hf)
  plt.grid()
  plt.title('Frequency response')
  plt.xlabel('Frequency')
  plt.ylabel('Amplitude')

  #Plot impulse response of raised-cosine filter
  plt.subplot(1,2,2)
  plt.plot(t,ht)
  plt.grid()
  plt.title('Impuse response')
  plt.xlabel('Time')
  plt.ylabel('Amplitude')
  plt.show()

@interact(band_width= (30000,100000,5000), beta=(0,1,0.1),sample_rate = (5000,20000,1000))
def call(band_width,beta,sample_rate):
  plot_filter(band_width,beta,sample_rate)
