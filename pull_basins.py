from os import getcwd
from wget import download
from zipfile import ZipFile

def extractShapeFile(folder_name, source_path, destination_path):
    zf = ZipFile(source_path)
    zf.extractAll(destination_path, [folder_name + '.shp'])


base_url = 'http://earlywarning.usgs.gov/hydrodata/sa_shapefiles_zip/'
folder_names = ['af_bas_30s_beta', 'as_bas_30s_beta',
    'au_bas_30s_beta', 'ca_bas_30s_beta', 'eu_bas_30s_beta',
    'na_bas_30s_beta', 'sa_bas_30s_beta']

current_directory = getcwd()
destination_path = current_directory + '/basins'


for folder in folder_names:
    url = base_url + folder + '.zip'
    download(url)
    file_path = current_directory + '/' + folder
    extractShapeFile(folder, file_path, destination_path + '/' + folder)
