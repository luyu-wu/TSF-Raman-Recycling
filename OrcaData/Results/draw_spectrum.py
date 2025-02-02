import numpy as np
import matplotlib.pyplot as plt
import smplotlib

# Raman data: frequency (cm^-1) and activity (intensity)
data = {
    6: (292.79, 0.054608),
    7: (407.67, 0.356995),
    8: (568.98, 5.080624),
    9: (795.92, 0.321218),
    10: (899.26, 4.378517),
    11: (1044.32, 4.573389),
    12: (1148.21, 2.366532),
    13: (1162.30, 5.047888),
    14: (1250.73, 14.805904),
    15: (1281.69, 5.105864),
    16: (1332.92, 1.467449),
    17: (1408.78, 16.741436),
    18: (1425.01, 12.180519),
    19: (1430.16, 20.726248),
    20: (1457.29, 2.513353),
    21: (2918.57, 148.109859),
    22: (2951.91, 158.298867),
    23: (2960.28, 132.648633),
    24: (3046.94, 68.822251),
    25: (3047.82, 51.559336),
    26: (3465.46, 126.505567),
}

def gaussian(x, mu, intensity, sigma=10):
    return intensity * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

x = np.linspace(200, 3500, 5000)
spectrum = np.zeros_like(x)

for mode, (freq, intensity) in data.items():
    spectrum += gaussian(x, freq, intensity)

# Plot the spectrum
plt.figure(figsize=(10, 6))
plt.plot(x, spectrum, label="Raman Spectrum")
plt.xlabel("Raman Shift (cm$^{-1}$)")
plt.ylabel("Intensity (a.u.)")
plt.title("Theoretically Calculated Raman Spectrum")
plt.grid(alpha=0.3)
plt.legend()
plt.show()
