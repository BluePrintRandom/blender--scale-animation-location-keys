import bpy

scale = .125     #change this value  'scaling factor'

   
for action in  bpy.data.actions :
    for fcurve in action.fcurves :
        print(fcurve.data_path)
        data = fcurve.data_path.split(".")
        
        if data[-1] == 'location':
            print('found')
            for p in fcurve.keyframe_points:
                p.co[1] *= scale
                
                