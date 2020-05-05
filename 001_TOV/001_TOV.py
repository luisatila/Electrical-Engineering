# ------------------------------------------------------------------------------
# TOV - Transient Overvoltage
# Calculation of overvoltages on the unfalted phases
# Single-phase-to-ground fault
# ------------------------------------------------------------------------------
# Luis Átila, v1 05/2020
#
# --- Input data --- Positive and zero sequence equivalent impedances
R1 = 0.03663
X1 = 0.83945
R0 = 29.01668
X0 = -5.18287
#
# --- Calculation
import cmath as mt
z11 = complex(R1, X1)
z00 = complex(R0, X0)
a1 = complex(mt.cos(120*mt.pi/180), mt.sin(120*mt.pi/180))
a2 = complex(mt.cos(240*mt.pi/180), mt.sin(240*mt.pi/180))
Vb = a2-(z00/z11-1)/(z00/z11+2)
Vc = a1-(z00/z11-1)/(z00/z11+2)
#
# --- Results
print('Vb = ' + str(abs(Vb)) + ' pu / ' + str(mt.phase(Vb)*180/mt.pi) + ' graus')
print('Vc = ' + str(abs(Vc)) + ' pu / ' + str(mt.phase(Vc)*180/mt.pi) + ' graus')
