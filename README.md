# Soft actor critic for satisfying STL specifications with network delays (Ver. 1)
This repository includes source codes for https://arxiv.org/abs/2108.01317v1 (Ver. 1), which are beta version. We will add the descriptions by coment out and may revise these source codes. We should use gym 0.18.0.

## Dynamics
In this study (Ver. 1), we consider the continuous control system. We do not use a numerical integration solver, but we compute the system dynamics as follows: 
```
        # next step================================================
        if abs(true_action[1]) <= 0.01:
            self.state[0] += true_action[0] * np.cos(self.state[2]) * self.dt
            self.state[1] += true_action[0] * np.sin(self.state[2]) * self.dt
        else:
            self.state[0] += (true_action[0]/true_action[1]) * (np.sin(self.state[2] + true_action[1]*self.dt)-np.sin(self.state[2]))
            self.state[1] += (true_action[0]/true_action[1]) * (np.cos(self.state[2])-np.cos(self.state[2] + true_action[1]*self.dt))
        self.state[2] += true_action[1] * self.dt

        if self.state[2] < -np.pi:
            self.state[2] += np.pi * 2.0
        elif math.pi < self.state[2]:
            self.state[2] -= np.pi * 2.0
        #======================================================================
```
Please check STL_SAC_NCSs_dynamics/dynamics.pdf (https://github.com/pondbooks/STL_SAC_NCSs/blob/main/STL_SAC_NCSs_dynamics/dynamics.pdf).

## Update Version
Please show https://github.com/pondbooks/STL_SAC_NCSs_Ver2.
