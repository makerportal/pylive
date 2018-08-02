import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,identifier=''):
    if line1==[]:
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()

    line1.set_ydata(y1_data)
    plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    plt.pause(0.1)
    
    return line1
