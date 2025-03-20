from os import write
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sunpy.visualization.colormaps
import os

def write_colormap_to_xml(cmap_name, file_name):
    cmap = plt.get_cmap(cmap_name)
    colors = cmap(np.linspace(0, 1, cmap.N))
    with open(file_name, 'w') as f:
        f.write('<ColorMaps>\n')
        f.write(f'  <ColorMap name="{cmap_name}" space="RGB">\n')
        for i, color in enumerate(colors):
            x = i / (len(colors) - 1)
            r, g, b, _ = color
            f.write(f'    <Point x="{x:.6f}" o="1" r="{r:.6f}" g="{g:.6f}" b="{b:.6f}"/>\n')
        f.write('  </ColorMap>\n')
        f.write('</ColorMaps>\n')


cm_list = [
    'goes-rsuvi94', 'goes-rsuvi131', 'goes-rsuvi171', 'goes-rsuvi195', 'goes-rsuvi284',
    'goes-rsuvi304', 'sdoaia94', 'sdoaia131', 'sdoaia171', 'sdoaia193', 'sdoaia211',
    'sdoaia304', 'sdoaia335', 'sdoaia1600', 'sdoaia1700', 'sdoaia4500', 'sohoeit171',
    'sohoeit195', 'sohoeit284', 'sohoeit304', 'soholasco2', 'soholasco3', 'sswidlsoholasco2',
    'sswidlsoholasco3', 'stereocor1', 'stereocor2', 'stereohi1', 'stereohi2', 'yohkohsxtal',
    'yohkohsxtwh', 'hinodexrt', 'hinodesotintensity', 'trace171', 'trace195', 'trace284',
    'trace1216', 'trace1550', 'trace1600', 'trace1700', 'traceWL', 'hmimag', 'irissji1330',
    'irissji1400', 'irissji1600', 'irissji2796', 'irissji2832', 'irissji5000', 'irissjiFUV',
    'irissjiNUV', 'irissjiSJI_NUV', 'kcor', 'rhessi', 'std_gamma_2', 'euvi171', 'euvi195',
    'euvi284', 'euvi304', 'solar orbiterfsi174', 'solar orbiterfsi304', 'solar orbiterhri_euv174',
    'solar orbiterhri_lya1216'
]

for cm_name in cm_list:
    write_colormap_to_xml(cm_name, os.path.join('xml', f'{cm_name}.xml'))




