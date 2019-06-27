#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project: Update and crop osm dump file for Moscow Oblast
# Author: Artem Svetlov <artem.svetlov@nextgis.com>



import os

#if prevdump not exists - download CFO from geofabrik and crop to MosOblast
def updateDump():
    
    dump_url='https://download.openstreetmap.fr/extracts/russia/north_caucasian_federal_district-latest.osm.pbf'
    directory='/data'
    
    downloaded_dump='central-fed-district-latest.osm.pbf'
    work_dump=os.path.join(directory,'work_dump.osm.pbf')
    updated_dump=os.path.join(directory,'updated_dump.osm.pbf')
    poly_file='area.poly'
    
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    #frist run of program
    if os.path.exists(work_dump) == False:
        cmd = 'curl -o {work_dump} {dump_url}'.format(work_dump = work_dump, dump_url=dump_url)
        print cmd
        os.system(cmd)


    #if prevdump dump exists - run osmupdate, it updating it to last hour state with MosOblast clipping, and save as currentdump
    cmd='osmupdate '+ work_dump + ' ' + updated_dump + '   -v -B='+poly_file #--day --hour 
    print cmd
    os.system(cmd)
    
    #if osmupdate not find updates in internet - new file not created so we use downloaded file
    if os.path.exists(work_dump) == True: 
        #rename currentdump to prevdump
        os.remove(work_dump)
        os.rename(updated_dump, work_dump)

    return 0

updateDump()
