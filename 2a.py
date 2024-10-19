import numpy as np
import imageio.v2 as imageio
import matplotlib.pyplot as plt

def analyze_red_channel(image_path, leaf_name):
    """
    Menganalisis channel warna merah dari gambar daun
    """
    try:
        image = imageio.imread(image_path)
    except FileNotFoundError:
        print(f"Error: File {image_path} tidak ditemukan")
        return None

    red_channel = image[:,:,0]
    

    plt.figure(figsize=(15, 5))
    
    plt.subplot(131)
    plt.imshow(image)
    plt.title(f'Gambar Asli\n{leaf_name}')
    plt.axis('off')
    
    plt.subplot(132)
    plt.imshow(red_channel, cmap='Reds')
    plt.title('Channel Merah')
    plt.axis('off')
    
    plt.subplot(133)
    plt.hist(red_channel.ravel(), bins=256, color='red', alpha=0.7)
    plt.title('Histogram Channel Merah')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    
    plt.tight_layout()
    plt.show()
    
    print(f"\nAnalisis Statistik Channel Merah - Daun {leaf_name}:")
    print(f"Nilai Minimum: {np.min(red_channel)}")
    print(f"Nilai Maksimum: {np.max(red_channel)}")
    print(f"Nilai Rata-rata: {np.mean(red_channel):.2f}")
    print(f"Nilai Median: {np.median(red_channel):.2f}")
    print(f"Standar Deviasi: {np.std(red_channel):.2f}")
    
    return {
        'leaf_name': leaf_name,
        'red_channel': red_channel,
        'statistics': {
            'min': np.min(red_channel),
            'max': np.max(red_channel),
            'mean': np.mean(red_channel),
            'median': np.median(red_channel),
            'std': np.std(red_channel)
        }
    }

def compare_red_channels(results):
    """
    Membandingkan channel merah dari beberapa daun
    """
    names = []
    means = []
    stds = []
    
    for result in results:
        if result is not None:
            names.append(result['leaf_name'])
            means.append(result['statistics']['mean'])
            stds.append(result['statistics']['std'])
    
    plt.figure(figsize=(10, 6))
    x = np.arange(len(names))
    width = 0.35
    
    plt.bar(x - width/2, means, width, label='Rata-rata', color='red', alpha=0.7)
    plt.bar(x + width/2, stds, width, label='Standar Deviasi', color='darkred', alpha=0.7)
    
    plt.xlabel('Jenis Daun')
    plt.ylabel('Nilai')
    plt.title('Perbandingan Intensitas Channel Merah')
    plt.xticks(x, names)
    plt.legend()
    
    plt.tight_layout()
    plt.show()

def save_red_channel(image_path, output_path):
    """
    Menyimpan gambar channel merah ke file
    """
    try:
        image = imageio.imread(image_path)
        red_channel = image[:,:,0]
        imageio.imwrite(output_path, red_channel)
        print(f"Channel merah berhasil disimpan ke {output_path}")
    except Exception as e:
        print(f"Error saat menyimpan gambar: {str(e)}")

if __name__ == "__main__":
    # Daftar gambar daun yang akan dianalisis
    leaves = [
        {'name': 'Pepaya', 'path': 'daun_pepaya.jpg'},
        {'name': 'Singkong', 'path': 'daun_singkong.jpg'},
        {'name': 'Kenikir', 'path': 'daun_kenikir.jpg'}
    ]

    results = []
    for leaf in leaves:
        print(f"\nMenganalisis daun {leaf['name']}...")
        result = analyze_red_channel(leaf['path'], leaf['name'])
        if result is not None:
            results.append(result)
            
            # Simpan channel merah ke file
            output_path = f"red_channel_{leaf['name'].lower()}.jpg"
            save_red_channel(leaf['path'], output_path)
    
    if len(results) > 1:
        print("\nMembuat perbandingan antar daun...")
        compare_red_channels(results)

def detailed_red_analysis(image_path, leaf_name):
    """
    Analisis lebih detail untuk channel merah
    """
    try:
        image = imageio.imread(image_path)
        red_channel = image[:,:,0]
        
        percentiles = np.percentile(red_channel, [25, 50, 75])
        
        print(f"\nAnalisis Detail Channel Merah - Daun {leaf_name}")
        print("Distribusi Intensitas:")
        print(f"Q1 (25%): {percentiles[0]:.2f}")
        print(f"Q2 (50%): {percentiles[1]:.2f}")
        print(f"Q3 (75%): {percentiles[2]:.2f}")
        print(f"IQR: {(percentiles[2] - percentiles[0]):.2f}")
        
        print("\nAnalisis Region:")
        print(f"Piksel Terang (>200): {np.sum(red_channel > 200)} piksel")
        print(f"Piksel Sedang (100-200): {np.sum((red_channel > 100) & (red_channel <= 200))} piksel")
        print(f"Piksel Gelap (<100): {np.sum(red_channel <= 100)} piksel")
        
        return True
    except Exception as e:
        print(f"Error dalam analisis detail: {str(e)}")
        return False

for leaf in leaves:
    detailed_red_analysis(leaf['path'], leaf['name'])
