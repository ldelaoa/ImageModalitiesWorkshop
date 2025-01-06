from Dicom2Nii_Funs import convert_dicom_to_nifty
import numpy as np
import re
import pandas as pd
import os
import yaml
import logging
import nibabel as nib
import pydicom as pdcm

def convertPlanCT(singPlanCT_path,patientID,save_path,Filename):
    input_filepaths = []

    for currSlide in os.listdir(singPlanCT_path):
        input_filepaths.append(os.path.join(singPlanCT_path,currSlide))
        
    image, pixel_spacing, image_position_patient,axial_positions = convert_dicom_to_nifty(input_filepaths,str(patientID),
                            save_path,[],extension='.nii.gz',filename=Filename,
                            pixel_spacing = None, image_position_patient=None,axial_positions=None,
                            np_image=None,dtype_image=np.float32,dtype_mask=np.uint8,)
            
    return  image, pixel_spacing, image_position_patient,axial_positions

    
def convertRT(RTStruct_path,patientID,Filename,save_path,target_labels,image, pixel_spacing, image_position_patient,axial_positions):
    image, pixel_spacing, image_position_patient,axial_positions = convert_dicom_to_nifty([RTStruct_path],str(patientID),
                            save_path,target_labels,extension='.nii.gz',filename=Filename,
                            pixel_spacing = pixel_spacing, image_position_patient=image_position_patient,axial_positions=axial_positions,
                                np_image=image,dtype_image=np.float32,dtype_mask=np.uint8,)
                    
    return 1

def main():            
    root_img = "/home/umcg/Desktop/NBIA_Multim/CT_PET_RT_dii/manifest-1736200275955/Soft-tissue-Sarcoma/STS_001/09-07-2000-NA-PET CT-63929/"
    PlanCT_path = root_img+"2.000000-CT IMAGES - RESEARCH-38601/"
    RTStruct_path_CT = root_img+"1.000000-RTstructCT-77278/1-1.dcm"
    PET_AC_path = root_img+"1.000000-PET AC-51583/"
    RTStruct_path_PET = root_img+"1.000000-RTstructPET-17357/1-1.dcm"
    
    patientID = "001"

    save_path  = "/home/umcg/Desktop/NBIA_Multim/CT_PET_RT_nii"

    #Convert Plan CT
    image, pixel_spacing, image_position_patient,axial_positions = convertPlanCT(PlanCT_path,patientID,save_path,"CT_")
    # RTSTruct
    target_labels = 'gtv'
    convertRT(RTStruct_path_CT,patientID,"RT_CT",save_path,target_labels,image=image, pixel_spacing=pixel_spacing, image_position_patient=image_position_patient,axial_positions=axial_positions)
    
    #PET 
    image, pixel_spacing, image_position_patient,axial_positions = convertPlanCT(PET_AC_path,patientID,save_path,"PET_AC_")
    convertRT(RTStruct_path_PET,patientID,"RT_PET",save_path,target_labels,image=image, pixel_spacing=pixel_spacing, image_position_patient=image_position_patient,axial_positions=axial_positions)

if __name__ == "__main__":
    main()
