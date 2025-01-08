#Print Relevant Headers in STIK
def RelevantHeaders(sitk_image,string):
  print(string)
  print("Origin",sitk_image.GetOrigin(),"Dimension",sitk_image.GetDimension(),"Size",sitk_image.GetSize(),"Spacing:",sitk_image.GetSpacing(),"Direction",sitk_image.GetDirection())

  image_array = sitk.GetArrayFromImage(sitk_image)
  print(f"Min val {np.min(image_array)} Max val {np.max(image_array)}")
