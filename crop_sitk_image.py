#crop_sitk_image function takes an sitk image and a target_size
#calculates the starting coordinates to center the cropped region within the original image, 
#uses sitk.RegionOfInterest to return the cropped image
def crop_sitk_image(image, target_size):
    image_size = image.GetSize()
    start_x = (image_size[0] - target_size[0]) // 2
    start_y = (image_size[1] - target_size[1]) // 2
    start_z = 0 # Assumes z-dimension is the same
    cropped_image = sitk.RegionOfInterest(image, target_size, [start_x, start_y, start_z])
    return cropped_image
