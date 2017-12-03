class MonteCarlo():

    def optimize(self, r_init, sigma):
        """
        Calculates most likely configuration for the next step.
        
        Uses generates random vector with normal distribution.
        
        Parameters:
        r_init: initial state
        sigma: standard deviation for normal distribution
        
        Returns r_opt
        """
        
        return self.r_opt

    def simulate(self, r_opt, phi_init ):
        """ 
        Calculate the next step
        
        Parameters:
        r_opt: optimal
        phi_init: initial potential
        
        Returns the new initial position and its potential
        """
        return r_init, phi_init
