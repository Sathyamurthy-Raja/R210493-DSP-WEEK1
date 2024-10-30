import numpy as np
import matplotlib.pyplot as plt

# Parameters
f = 200  # Frequency in Hz
duration = 0.5  # Duration in seconds
fs1 = 8000  # Sampling rate 1 in Hz
fs2 = 1000  # Sampling rate 2 in Hz
levels = 8  # Quantization levels

# Generate the original signal
t1 = np.arange(0, duration, 1/fs1)
x1 = np.sin(2 * np.pi * f * t1)

# Resample the signal
t2 = np.arange(0, duration, 1/fs2)
x2 = np.interp(t2, t1, x1)
'''
t2: The x-coordinates of the new data points.
t1: The x-coordinates of the known data points.
x1: The y-coordinates of the known data points.'''
# Quantize the signal
x2_quantized = np.round(x2 * (levels-1)/2) / ((levels-1)/2)

# Save the quantized signal in binary format
#with open('quantized_signal.bin', 'wb') as f:
 #   f.write(x2_quantized.astype(np.float32).tobytes())

x2_quantized.astype(np.float32).tofile('quantized_signal.bin')
# Plot the original, resampled, and quantized signals
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t1, x1)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t2, x2)
plt.title('Resampled Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t2, x2_quantized)
plt.title('Quantized Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
