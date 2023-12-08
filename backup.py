#Make a backup of the folder (subdirectiories included)
import shutil
source_folder='/Users/admin/python/Python-scripts'
backup_folder ='/Users/admin/python/backup'
shutil.copytree(source_folder,backup_folder)
