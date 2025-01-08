#Normalizes the intensity values of a given image.
#Normalizes the intensity values to a range between 0 and 1 using min-max scaling, while preserving the original image's metadata
#args:
#image: This is expected to be a SimpleITK image object.


def NormalizeImageIntensityNumpy(image):

    image_array = sitk.GetArrayFromImage(image)
    min_intensity = np.min(image_array)
    max_intensity = np.max(image_array)

    normalized_array = (image_array - min_intensity) / (max_intensity - min_intensity)
    normalized_image = sitk.GetImageFromArray(normalized_array)
    normalized_image.CopyInformation(image)
    return normalized_image

#ct_normalized = NormalizeImageIntensityNumpy(ct_sitk)
