# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by martinpletz on Sat Nov 25 15:29:27 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.992064, 0.95339), width=146.032, 
    height=94.5763)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('../model_abaqus.py', __main__.__dict__)
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#: Warning: findAt could not find a geometric entity at (-100.0, 0.0, 0.0)
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: Warning: findAt could not find a geometric entity at (52.0020365279993, -0.0234848605821721, 0.0)
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: Warning: findAt could not find a geometric entity at (-1000.0, -1000.0, 0.0)
#: Length of edge = 2.9999962290934
#: Length of edge = 2.9999930738447
#: Length of edge = 2.99999725568573
#: Length of edge = 3.00000370467593
#: Length of edge = 3.00000218430183
#: Length of edge = 0.000342127782739997
#: Length of edge = 2.99998797561424
#: Length of edge = 0.000262581621127124
#: Length of edge = 2.99965596566626
#: Length of edge = 0.000278825871151739
#: Length of edge = 2.99975205105208
#: Length of edge = 0.000388334730574109
#: Length of edge = 2.99971849062979
#: Length of edge = 0.000368963380577281
#: Length of edge = 2.99959173637671
#: Length of edge = 4.22401303048315e-06
#: Length of edge = 2.99962132705907
#: Length of edge = 3.00011903149021
#: Length of edge = 4.22391353716023e-06
#: Length of edge = 3.00010624462165
#: Length of edge = 2.9996462318289
#: Length of edge = 2.99964181349715
#: Length of edge = 0.000359253817925088
#: Length of edge = 2.99971632179354
#: Length of edge = 0.000378115395562927
#: Length of edge = 2.99971568882573
#: Length of edge = 0.000286361705513529
#: Length of edge = 2.99966877907732
#: Length of edge = 0.000269681496991748
#: Length of edge = 3.00001202443191
#: Length of edge = 0.000333124419267244
#: Length of edge = 2.9999978157105
#: Length of edge = 2.99999629532405
#: Length of edge = 3.00000280371266
#: Length of edge = 3.00000686675693
#: Length of edge = 3.00000377090659
#: Length of edge = 2.9999931347824
#: Length of edge = 2.99999951519375
#: Length of edge = 10.0000045894943
#: Length of edge = 3.00000686615517
#: Length of edge = 3.00000048386869
#: Length of edge = 9.99999541050568
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: Warning: findAt could not find a geometric entity at (80.0020007154882, -0.00725969468712863, 0.0)
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: Warning: findAt could not find a geometric entity at (-1000.0, -1000.0, 0.0)
#: Length of edge = 4.01786764123041
#: Length of edge = 2.99964780840714
#: Length of edge = 2.0188080906082e-05
#: Length of edge = 2.99972623983988
#: Length of edge = 0.000361974690254371
#: Length of edge = 1.98225760696961
#: Length of edge = 0.000291419457870185
#: Length of edge = 0.000371757789979838
#: Length of edge = 2.99968304504285
#: Length of edge = 2.99959827143123
#: Length of edge = 4.01780713933901
#: Length of edge = 2.01876813981094e-05
#: Length of edge = 0.000299295659420801
#: Length of edge = 1.98224204703891
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: The model database has been saved to "Z:\Documents\_Papers\inc_cracks_spline\fe-model\des-crack-hole060-expl-da030\inc-18-01.cae".
#: Model: Z:/Documents/_Papers/inc_cracks_spline/fe-model/des-crack-hole060-expl-da030/inc-18-01.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       18
#: Number of Node Sets:          23
#: Number of Steps:              1
#: INFO: create field output CON_F (step=load-000; frame=0)
#: INFO: create field output CON_F (step=load-000; frame=1)
#: INFO: create field output U_GLOBAL_CSYS (instance=PART-1-1; step=load-000; frame=0)
#: INFO: create field output S_GLOBAL_CSYS (instance=PART-1-1; step=load-000; frame=0)
#: INFO: create field output U_GLOBAL_CSYS (instance=PART-1-1; step=load-000; frame=1)
#: INFO: create field output S_GLOBAL_CSYS (instance=PART-1-1; step=load-000; frame=1)
#: Model: Z:/Documents/_Papers/inc_cracks_spline/fe-model/des-crack-hole060-expl-da030/inc-18-01.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       18
#: Number of Node Sets:          23
#: Number of Steps:              1
#:  
#: conforce - log summary
#: ----------------------
#:   6 x INFO
#: ----------------------
#:  
#: Model: Z:/Documents/_Papers/inc_cracks_spline/fe-model/des-crack-hole060-expl-da030/inc-18-01.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       18
#: Number of Node Sets:          23
#: Number of Steps:              1
#: Model: Z:/Documents/_Papers/inc_cracks_spline/fe-model/des-crack-hole060-expl-da030/inc-18-01.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       18
#: Number of Node Sets:          23
#: Number of Steps:              1
print 'RT script done'
#: RT script done
