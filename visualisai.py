import numpy as np
import matplotlib.pyplot as plt

# Create sample images
def create_sample_images():
    # Create a simple color image (RGB)
    color_img = np.zeros((100, 100, 3))
    color_img[20:80, 20:80, 0] = 1.0  # Red channel
    color_img[30:70, 30:70, 1] = 1.0  # Green channel
    color_img[40:60, 40:60, 2] = 1.0  # Blue channel

    # Create a grayscale image
    grayscale_img = np.zeros((100, 100))
    for i in range(100):
        grayscale_img[:,i] = i/100.0

    # Create a binary image
    binary_img = np.zeros((100, 100))
    binary_img[25:75, 25:75] = 1.0

    # Display images
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    ax1.imshow(color_img)
    ax1.set_title('Citra Berwarna (RGB)')
    ax1.axis('off')

    ax2.imshow(grayscale_img, cmap='gray')
    ax2.set_title('Citra Grayscale')
    ax2.axis('off')

    ax3.imshow(binary_img, cmap='binary')
    ax3.set_title('Citra Biner')
    ax3.axis('off')

    plt.tight_layout()
    plt.show()

    # Show color image channels separately
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

    ax1.imshow(color_img[:,:,0], cmap='Reds')
    ax1.set_title('Channel Merah')
    ax1.axis('off')

    ax2.imshow(color_img[:,:,1], cmap='Greens')
    ax2.set_title('Channel Hijau')
    ax2.axis('off')

    ax3.imshow(color_img[:,:,2], cmap='Blues')
    ax3.set_title('Channel Biru')
    ax3.axis('off')

    plt.tight_layout()
    plt.show()

create_sample_images()
