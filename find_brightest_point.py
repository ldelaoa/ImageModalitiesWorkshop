# @title
#finds the pixel(s) with the highest intensity, and returns both the maximum intensity and the location of those pixels
# This function is likely intended to be used to find the most active region in a PET 

def find_brightest_point(sitk_image):
    image_array = sitk.GetArrayFromImage(sitk_image)
    max_value = np.max(image_array)
    max_indices = np.where(image_array == max_value)
    return max_value, max_indices

max_value, max_indices = find_brightest_point(pet_sitk_origin)
#RegionOfInterest is a function from the SimpleITK library used to extract a rectangular sub-region (also known as a region of interest or ROI) from an image.
#The size [249, 249, 137] defines the dimension of the cropped image, and [0, 0, 0] defines the starting index. 
#The clipped_ct_sitk is the input image that is being cropped.
cropped_CT = sitk.RegionOfInterest(clipped_ct_sitk,[clipped_ct_sitk.GetSize()[0],clipped_ct_sitk.GetSize()[1],max_indices[2],[0,0,0])
