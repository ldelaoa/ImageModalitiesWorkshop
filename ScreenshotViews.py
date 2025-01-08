# @title
#Designed to visualize 3D medical image data, specifically CT and tumor segmentation, along with an optional secondary image (like a PET scan). 
#It generates a series of 2D slices from the 3D volumes in three different orientations (axial, coronal, and sagittal) 
#Displays or saves them as a JPEG image

#args:
#CT: A SimpleITK image object representing the CT scan or any other image.
#BW_tumor: A SimpleITK image object representing the tumor segmentation (binary mask).
#saveJPEG_Path_Px: An optional string specifying the path to save the output JPEG image. If None, the image is displayed.
#struct_name: An optional string for naming the output image file.
#Px: Not used in this version
#SecondImage: An optional SimpleITK image object representing a second image to overlay on the CT.
  
def ScreenshotViews(CT,BW_tumor,saveJPEG_Path_Px=None,struct_name=None,Px=None,SecondImage=None):
  try:
    ct_np = sitk.GetArrayFromImage(CT)
    rt_np = sitk.GetArrayFromImage(BW_tumor)
    if SecondImage is not None:
      SecondImage = sitk.GetArrayFromImage(SecondImage)

    slice_sums = np.sum(rt_np, axis=(1, 2))
    axial_indices = np.where(slice_sums > 0)[0]
    axial_mid = len(axial_indices)//2

    coronal_sums = np.sum(rt_np, axis=(0, 2))
    coronal_indices = np.where(coronal_sums > 0)[0]
    coronal_mid = len(coronal_indices)//2

    sagittal_sums = np.sum(rt_np, axis=(0, 1))
    sagittal_indices = np.where(sagittal_sums > 0)[0]
    sagittal_mid = len(sagittal_indices)//2


    plt.subplot(131),plt.imshow(ct_np[axial_indices[axial_mid],:,:],cmap='gray')
    plt.subplot(131),plt.contour(rt_np[axial_indices[axial_mid],:,:],colors='red',linewidths=0.5),plt.axis('on')
    if SecondImage is not None:
      plt.subplot(131),plt.imshow(SecondImage[axial_indices[axial_mid],:,:],alpha=0.5,cmap='hot'),plt.axis('on')
    plt.subplot(132),plt.imshow(ct_np[:,coronal_indices[coronal_mid],:],cmap='gray')
    plt.subplot(132),plt.contour(rt_np[:,coronal_indices[coronal_mid],:],colors='red',linewidths=0.5),plt.axis('on')
    if SecondImage is not None:
      plt.subplot(132),plt.imshow(SecondImage[:,coronal_indices[coronal_mid],:],alpha=0.5,cmap='hot'),plt.axis('on')
    plt.subplot(133),plt.imshow(ct_np[:,:,sagittal_indices[sagittal_mid]],cmap='gray')
    plt.subplot(133),plt.contour(rt_np[:,:,sagittal_indices[sagittal_mid]],colors='red',linewidths=0.5),plt.axis('on')
    if SecondImage is not None:
      plt.subplot(133),plt.imshow(SecondImage[:,:,sagittal_indices[sagittal_mid]],alpha=0.5,cmap='hot'),plt.axis('on')
    plt.tight_layout()

    if saveJPEG_Path_Px is None:
      plt.show()
    else:
      plt.savefig(os.path.join(saveJPEG_Path_Px,struct_name+".jpeg"),dpi=150,format="jpeg")
    plt.clf()
    plt.close()
  except Exception as e:
    print("Screenshot ex:",e)
    print("Struct:",struct_name)
    print("Path:",saveJPEG_Path_Px)
    return False

  return True

#_ = ScreenshotViews(CT_image,CTTumor_image,saveJPEG_Path_Px=None,struct_name="img1_",Px="001",SecondImage=None)
