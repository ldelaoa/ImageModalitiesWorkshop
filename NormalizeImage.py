# @title
#`NormalizeImage` that accepts several arguments:
#*   `image`: This is the input `sitk` image that needs to be processed.
#*   `intFlag`: (Optional) A string that specifies the type of interpolation to be used during resampling. It can be set to `"LabelGaussian"`, `"NN"` for nearest neighbor, or "Linear" for linear interpolation.
#*   `saveFilename`: (Optional) A string specifying the filename to save the resampled image. If `None`, the image will not be saved.
#*  `originReference`: (Optional) An `sitk` image to be used as a reference to determine the new origin. If `None`, it uses the `origin` of the input `image`.
#*   `desired_spacing`: (Optional) A list or tuple representing the desired spacing for the resampled image. If `None`, the original spacing is maintained.
#*   `desired_Size`: (Optional) A list or tuple representing the desired size for the resampled image. If `None`, the original size is maintained.
#*   `rotation`: (Optional) If not `None`, it will rotate the image, and is assumed to be for a specific transformation (not general rotation).
def NormalizeImage(image,intFlag=None,saveFilename=None,originReference=None,desired_spacing = None,desired_Size = None,rotation=None):

    if rotation is not None:
        image = sitk.PermuteAxes(image,[1,0,2])
        print("rotate")

    resampler = sitk.ResampleImageFilter()

    if desired_spacing is not None:
        current_spacing = image.GetSpacing()
        resampling_factor = [current_spacing[i] / desired_spacing[i] for i in range(image.GetDimension())]
        new_size = [int(image.GetSize()[i] * resampling_factor[i]) for i in range(image.GetDimension())]
        resampler.SetSize(new_size)
        resampler.SetOutputSpacing(desired_spacing)
        #print("Change Spacing",desired_spacing)
    elif desired_Size is not None:
        spacing_ratio = [sz1/sz2 for sz1, sz2 in zip(image.GetSize(), desired_Size)]
        new_spacing = [sz * ratio for sz, ratio in zip(image.GetSpacing(), spacing_ratio)]
        resampler.SetSize(desired_Size)
        resampler.SetOutputSpacing(new_spacing)
        #print("Changing Size",desired_Size)
    else:
        resampler.SetSize(image.GetSize())
        resampler.SetOutputSpacing(image.GetSpacing())

    if originReference is None:
        resampler.SetOutputOrigin(image.GetOrigin())
    else:
        resampler.SetOutputOrigin(originReference)
        #print("Change Origin",originReference)

    if intFlag=="LabelGaussian":
        resampler.SetInterpolator(sitk.sitkLabelGaussian)
    elif intFlag=="NN":
        resampler.SetInterpolator(sitk.sitkNearestNeighbor)
    elif instFlag =="Linear":
        resampler.SetInterpolator(sitk.sitkLinear)
    else:
        resampler.SetInterpolator(sitk.sitkLinear)

    if saveFilename is not None:
        sitk.WriteImage(resampled_image,saveFilename)

    resampled_image = resampler.Execute(image)
    return resampled_image
