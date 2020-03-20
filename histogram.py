import numpy as np 
import matplotlib.pyplot as plt 
import nibabel as nib 
import seaborn as sns
import SimpleITK as sitk

img = '/media/fabio/Disco locale/Scaricati/ADNI/002_S_0295/MPR__GradWarp__B1_Correction__N3__Scaled/2006-04-18_08_20_30.0/S13408/ADNI_002_S_0295_MR_MPR__GradWarp__B1_Correction__N3__Scaled_Br_20070319113623975_S13408_I45108.nii'
def return_img(img, ax=None, n_bins =1200, alpha=0.8,lw=3, **kwargs):

    img_nii = nib.load(img)
    print(img_nii.header)
    data = img_nii.get_data()
    hist, bin_edges = np.histogram(data.flatten(), n_bins, **kwargs)
    bins = np.diff(bin_edges)/2 + bin_edges[:-1]
    
    data = np.array(data.flatten())
    data = [x for x in data if x!=0]
    t2 = (np.percentile(data, 2))
    t98 = (np.percentile(data, 98))
    return t2, t98, data

if __name__ == '__main__':
    counter = 0
    center_x = 0
    center_y = 0
    center_z = 0
    t2, t98, t = return_t2_t98_t(img)
    t = t2 + 0.1*(t98 - t2)
    tmp = t - t2
    img_nii = nib.load(img)
    data = img_nii.get_fdata()
    print(data.shape)
    for i in range(0, data.shape[0]):
        for j in range(0, data.shape[1]):
            for k in range(0, data.shape[2]):
                c = data[i][j][k] - t2

                if c>tmp:
                    print(c)
                    c = np.minimum(c, t98 - t2)
                    print(t98-t2)

                    counter += c
                    center_x +=  c*i
                    center_y +=  c*j
                    center_z +=  c*k
    print(center_x/counter, center_y/counter, center_z/counter)
                

    print(t98)

