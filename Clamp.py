#modifies an image by limiting its pixel intensity values to a specified range
#It then modifies the image by setting all pixel values below the lower bound to that bound and all pixel values above the upper bound to that bound. 
#This operation is commonly called 'clamping' or 'clipping' and it ensures pixel values are within a defined range.
#args:
#image: This is expected to be a SimpleITK image object.
#lower_bound: This is the minimum pixel value that will be allowed.
#upperbound: This is the maximum pixel value that will be allowed.
  
def Clamp(image,lower_bound,upperbound):
    image_array = sitk.GetArrayFromImage(image)
    clipped_array = np.clip(image_array, lower_bound, upperbound)
    clipped_image = sitk.GetImageFromArray(clipped_array)
    clipped_image.CopyInformation(image)
    return clipped_image
