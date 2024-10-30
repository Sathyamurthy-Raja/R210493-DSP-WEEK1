import numpy as np
import matplotlib.pyplot as plt

def quantize_4bit(x):
    """Quantizes input data to 4 bits.

    Args:
        x: Input data to be quantized.

    Returns:
        Quantized data.
    """

    # Determine the minimum and maximum values of the input data
    x_min, x_max = np.min(x), np.max(x)

    # Calculate the step size for 4-bit quantization
    step_size = (x_max - x_min) / 15#2**4-1

    # Quantize the input data using uniform quantization
    x_quantized = np.round((x - x_min) / step_size) * step_size + x_min

    return x_quantized

# Generate a sample signal
x = np.linspace(-1, 1, 1000)
y = np.sin(2 * np.pi * 5 * x) + 0.5 * np.sin(2 * np.pi * 10 * x)

# Quantize the signal to 4 bits
y_quantized = quantize_4bit(y)

# Plot the original and quantized signals
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Original Signal')
plt.plot(x, y_quantized, 'r--', label='Quantized Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
