#
# Function for Bayesian Optimization for fitting hyperfoam to
# experimental data in the foam properties database.
#
# Alex Landauer, NIST MML MMSD, Dec. 2023
#
import pandas as pd
import numpy as np
import subprocess as sp
import matplotlib.pyplot as plt
from matplotlib import gridspec
import requests
import h5py
from bayes_opt import BayesianOptimization
from bayes_opt import UtilityFunction

def hyperfoam_objective_function(mu0,a0,mu1,a1,b0,b1):
    """ This function computes cost for the current parameter guess. """

    #read in stress and strain data
    #make sure "dest" is the same as in the run script
    dest = "./VN01_001_003_QS06_00_dic.mat"
    dic_data = h5py.File(dest)

    #get stress and stretch
    T_exp = -1.0e6*(np.array(dic_data['complete_data']['eng_stress']))
    T_exp = np.transpose(T_exp[0:200,0])
    L_0 = np.array(dic_data['complete_data']['E'][0, 0:200])
    L_1 = np.array(dic_data['complete_data']['E'][1, 0:200])

    print("Current guess:")
    print([mu0, a0, mu1, a1, b0, b1])

    #compute the model stress
    T_th = hyperfoam_stress_function(L_0, L_1, mu0, a0, mu1, a1, b0, b1)

    #compute the objective function value from the normalized diviation between 
    #the model and the experimental stress for the range of stretches used. 
    #With the BO framework it always maximizes the objective, so we invert and 
    #thus look for the highest cost
    N = np.shape(T_exp)
    #obj_val = N[0]**4/(np.sum((T_th - T_exp)**2))
    obj_val = N[0]**2/(np.sum((1.0 - np.divide(T_th,T_exp))**2))
    
    print("Objective func value:")
    print(obj_val)

    return obj_val 


def hyperfoam_stress_function(L_0, L_1, mu0, a0, mu1, a1, b0, b1):
    """ This function computes the theoretical stress vector according to the 
    N=2 hyperfoam constitutive relationship. """
    
    #mean poisson's ratio during loading (only need if betas aren't free params)
    #poissons = np.mean(-np.divide(L_1,L_0))
    #b0 = poissons/(1-2*poissons)
    #b1 = b0

    #volume change and beta parameters
    J = L_0*L_1*L_1

    # compute the theoretical stress for each strain point
    sizeL = np.size(L_1)
    T_th = np.zeros(sizeL)
    for k in range(sizeL):
        #theoretical stress
        T_th_0 = mu0/a0*(L_0[k]**a0 - J[k]**(-a0*b0))
        T_th_1 = mu1/a1*(L_1[k]**a1 - J[k]**(-a1*b1))
        
        T_th[k] = -2/L_0[k]*(T_th_0 + T_th_1)

    return T_th



# BO plotting functions
def posterior(optimizer, x_obs, y_obs, grid):
    optimizer._gp.fit(x_obs, y_obs)

    mu, sigma = optimizer._gp.predict(grid, return_std=True)
    return mu, sigma

def plot_gp(optimizer, x, y):
    fig = plt.figure(figsize=(16, 10))
    steps = len(optimizer.space)
    fig.suptitle(
        'Gaussian Process and Utility Function After {} Steps'.format(steps),
        fontdict={'size':30}
    )
    
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1]) 
    axis = plt.subplot(gs[0])
    acq = plt.subplot(gs[1])
    
    x_obs = np.array([[res["params"]["x"]] for res in optimizer.res])
    y_obs = np.array([res["target"] for res in optimizer.res])
    
    mu, sigma = posterior(optimizer, x_obs, y_obs, x)
    axis.plot(x, y, linewidth=3, label='Target')
    axis.plot(x_obs.flatten(), y_obs, 'D', markersize=8, label=u'Observations', color='r')
    axis.plot(x, mu, '--', color='k', label='Prediction')

    axis.fill(np.concatenate([x, x[::-1]]), 
              np.concatenate([mu - 1.9600 * sigma, (mu + 1.9600 * sigma)[::-1]]),
        alpha=.6, fc='c', ec='None', label='95% confidence interval')
    
    axis.set_xlim((-2, 10))
    axis.set_ylim((None, None))
    axis.set_ylabel('f(x)', fontdict={'size':20})
    axis.set_xlabel('x', fontdict={'size':20})
    
    utility_function = UtilityFunction(kind="ucb", kappa=5, xi=0)
    utility = utility_function.utility(x, optimizer._gp, 0)
    acq.plot(x, utility, label='Utility Function', color='purple')
    acq.plot(x[np.argmax(utility)], np.max(utility), '*', markersize=15, 
             label=u'Next Best Guess', markerfacecolor='gold', markeredgecolor='k', markeredgewidth=1)
    acq.set_xlim((-2, 10))
    acq.set_ylim((0, np.max(utility) + 0.5))
    acq.set_ylabel('Utility', fontdict={'size':20})
    acq.set_xlabel('x', fontdict={'size':20})
    
    axis.legend(loc=2, bbox_to_anchor=(1.01, 1), borderaxespad=0.)
    acq.legend(loc=2, bbox_to_anchor=(1.01, 1), borderaxespad=0.)




