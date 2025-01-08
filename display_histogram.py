# Plot Histogram
#Visualize the distribution of pixel intensities in an image.
#args:
#`sitk_image`: This is expected to be an image object of the `SimpleITK` library, from which pixel data will be extracted.
#`title`: This is a string that will be used as the title of the histogram plot, and defaults to "Image Histogram".
#`exclude_Lowest`: This is a boolean that determines whether the lowest pixel value will be excluded from the histogram. It defaults to `False`.

def display_histogram(sitk_image, title="Image Histogram",exclude_Lowest=False):
    image_array = sitk.GetArrayFromImage(sitk_image)
    if exclude_Lowest:
      unique_values = np.unique(image_array.flatten())
      minv = np.min(unique_values)+5
      unique_values = unique_values[unique_values > minv]
      print(np.min(unique_values))
      plt.hist(unique_values, bins=256, edgecolor='black')
    else:
      plt.hist(image_array.flatten(), bins=256, edgecolor='black')
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()

#display_histogram(ct_sitk, title="CT Image Histogram",exclude_Lowest=True)
