import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
import os

def ScreenshotViews(CT,BW_tumor,saveJPEG_Path_Px=None,struct_name=None,Px=None,logger=None):
  try:
    #ct_np = np.flip(sitk.GetArrayFromImage(CT),axis=0)
    #rt_np = np.flip(sitk.GetArrayFromImage(BW_tumor),axis=0)

    ct_np = sitk.GetArrayFromImage(sitk.ReadImage(CT))
    rt_np = sitk.GetArrayFromImage(sitk.ReadImage(BW_tumor))

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
    plt.subplot(131),plt.contour(rt_np[axial_indices[axial_mid],:,:],colors='red',linewidths=0.5),plt.axis('off')
    plt.subplot(132),plt.imshow(ct_np[:,coronal_indices[coronal_mid],:],cmap='gray')
    plt.subplot(132),plt.contour(rt_np[:,coronal_indices[coronal_mid],:],colors='red',linewidths=0.5),plt.axis('off')
    plt.subplot(133),plt.imshow(ct_np[:,:,sagittal_indices[sagittal_mid]],cmap='gray')
    plt.subplot(133),plt.contour(rt_np[:,:,sagittal_indices[sagittal_mid]],colors='red',linewidths=0.5),plt.axis('off')
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
    logger.info(Px+" Corrupt RTStruct"+str(e))
    return False
    
  return True

root = "/home/umcg/Desktop/NBIA_Multim/CT_PET_RT_nii/001/"
CT = root+"CT_ct.nii.gz"
BW_tumor = root+"RT_CT_rtstruct_GTV_Mass.nii.gz"
saveroot = "/home/umcg/Desktop/NBIA_Multim/JPEGS/"
_ = ScreenshotViews(CT,BW_tumor,saveJPEG_Path_Px=saveroot,struct_name="img1_",Px="001",logger=None)