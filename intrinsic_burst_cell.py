# Our Izhikevich cell super class, which has regular spiking parameters

# The lab exercise today is to create two more Izhikevich cell types
# as subclasses of this class:
# * chattering cell type
# * intrinsically bursting cell type
#
# To do so, you will need to reference the README section of this
# repository (visit the repository page in Github and scroll down)
# to get equations for these cells. From the equations, you will
# figure out the parameter values you need and use them in your
# sub class.
#
# Create each sub class in a separate file:
# intrinsic_burst_cell.py
# chattering_cell.py
#
# Save the files in your repository folder, right next to izhikevich_cells.py
# At the top of each file, import your izhikevich_cells file so that
# the cell class is available to you. Import it by adding the following line:
# import izhikevichcells as izh
#
# Hint: you can now refer to the izhikevich cell object (izhCell) with:
# izh.izhCell
#
# In your intrinsic_burst_cell.py file, define a subclass of the izhCell
# and name it ibCell. Include an __init__ method that calls the izhCell
# __init__ method first and then reassigns any parameters that need to
# be a different value.
#
# When you have finished creating the child class, add a call to create one
# and assign it to the object myCell.
#
# Then run the cell's simulate method
#
# Finally, add a test to check if this new file is running directly:
# if __name__=='__main__':
# and as a substatement (if True), call the plotting function from
# izhikevich_cells.py using dot notation (hint: izh.plot...)
#
# Make sure to run your file to test it.

import numpy as np
import matplotlib.pyplot as plt


class izhCell():
    def __init__(self,stimVal):
        '''
        

        Parameters
        ----------
        stimVal : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        # Define Neuron Parameters
        self.celltype='Bursting Izhikevich' # Intrinsically Bursting
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
    
        
        # Set up the simulation
        self.T=1000 # ms
        self.tau=1 # ms - time step
        self.n=int(np.round(self.T/self.tau))
        
        # Set up the stimulation
        self.I = np.concatenate((np.zeros((1,int(0.1*self.n))),self.stimVal*np.ones((1,int(0.01*self.n))),self.stimVal*.1*np.ones((1,int(0.89*self.n)))), axis=1)

        # Set up placeholders for my outputs from the simulation              
        self.v=self.vr*np.zeros((1,self.n))
        self.u=0*self.v
        
    
    def __repr__(self):
        return self.celltype +' Cell with StimVal=' + str(self.stimVal)

    def simulate(self):    
        # Run the simulation
        print("vpeak = ", self.vpeak)
        for i in range(1,self.n-1):
            self.v[0,i+1]+=self.v[0,i]+self.tau*(self.k*(self.v[0,i]-self.vr)*(self.v[0,i]-self.vt)-self.u[0,i]+self.I[0,i])/self.C
            self.u[0,i+1]=self.u[0,i]+self.tau*self.a*(self.b*(self.v[0,i]-self.vr)-self.u[0,i])
            
            if self.v[0,i+1]>=self.vpeak:
                    self.v[0,i]=self.vpeak
                    self.v[0,i+1]=self.c
                    self.u[0,i+1]=self.u[0,i+1]+self.d 
                    
def plotMyData(somecell, upLim = 1000):
    tau = somecell.tau
    n = somecell.n
    v = somecell.v
    celltype = somecell.celltype

    # Plot the results
    fig = plt.figure()
    plt.plot(tau*np.arange(0,n),v[0,:].transpose(), 'k-')
    plt.xlabel('Time Step')
    plt.xlim([0, upLim])
    plt.ylabel(celltype + ' Cell Response')
    plt.show()

def createCell():
    myCell = izhCell(stimVal=4000)        
    myCell.simulate()
    plotMyData(myCell)
    
if __name__=='__main__':
    createCell()