import numpy as np
import matplotlib.pyplot as plt

# Parameters
n = 1.5
Vt = 0.026
Id0 = 1e-9
Vth = 1.2

# Vgs range
Vgs = np.linspace(0, 1.5, 200)

# Subthreshold current model
Id = Id0 * np.exp((Vgs - Vth) / (n * Vt))

# Plot (log scale)
plt.figure()
plt.semilogy(Vgs, Id)
plt.xlabel("Vgs (V)")
plt.ylabel("Id (A) [log scale]")
plt.title("Subthreshold Id-Vgs Characteristics")
plt.grid(True)

plt.show()
