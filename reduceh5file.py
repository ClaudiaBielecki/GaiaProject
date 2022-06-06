import h5py

hf = h5py.File('download.hdf5', 'r')
hfout = h5py.File('data01.hdf5','w')

listkeep = ['source_id', 'ra', 'dec', 'parallax','pmra', 'pmdec', 'radial_velocity', 'l','b']
cond1 = hf['parallax'][:] > 0.2
cond2 = hf['parallax_over_error'][:] > 5
ind = cond1 & cond2

for item in listkeep:
        hfout.create_dataset(item, data=hf[item][:][ind]) 


#print(hf['dec'][0].dtype)
#print(type(hf))
#print(type(hf['dec']))
#print(hf.keys())


#hfout.create_dataset('source_id', data=hf['source_id']) 
#hfout.create_dataset('dec', data=hf['dec']) 



#cond1 = data['parallax_over_error'] > 5 
#cond3 = data['parallax'] > 0.2
#ind =  cond1 & cond3
#datared = data[ind]
#print('rows reduced')
#datafinal = datared['source_id', 'ra', 'dec', 'parallax','pmra', 'pmdec', 'dr2_radial_velocity','l', 'b']
#print('columns reduced')
#datafinal.write('GaiaData1.hdf5')
#print('file saved')
#list1 = ['A0', 'a_g_bp_val', 'a_g_rp_val', 'a_g_val', 'age', 'alpha', 'b_true', 'bp_g', 'bp_g_int', 'bp_g_true', 'bp_rp', 'bp_rp_int', 'bp_rp_true', 'calcium', 'carbon', 'dec_error', 'dec_true', 'dhel_true', 'dmod_true', 'e_bp_min_rp_val', 'ebv', 'feh', 'g_rp', 'g_rp_int', 'g_rp_true', 'helium', 'l_true', 'logg', 'lognh', 'lum_val', 'mact', 'magnesium', 'mini', 'mtip', 'neon', 'nitrogen', 'oxygen', 'parallax_error', 'parallax_true', 'parentid', 'partid', 'phot_bp_mean_mag', 'phot_bp_mean_mag_error', 'phot_bp_mean_mag_int', 'phot_bp_mean_mag_true', 'phot_g_mean_mag', 'phot_g_mean_mag_error', 'phot_g_mean_mag_int', 'phot_g_mean_mag_true', 'phot_rp_mean_mag', 'phot_rp_mean_mag_error', 'phot_rp_mean_mag_int', 'phot_rp_mean_mag_true', 'pmb_true', 'pmdec_error', 'pmdec_true', 'pml_true', 'pmra_error', 'pmra_true', 'px_true', 'py_true', 'pz_true', 'ra_error', 'ra_true', 'radial_velocity_error', 'radial_velocity_true', 'random_index', 'silicon', 'sulphur', 'teff_val', 'vx_true', 'vy_true', 'vz_true']
