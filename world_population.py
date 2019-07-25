import json
import pygal
from country_codes import get_country_code
#from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)

cc_population = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))

		code = get_country_code(country_name)
		if code:
			cc_population[code] = population

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	if pop <1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = LightColorizedStyle

wm = pygal.maps.world.World(style = wm_style)
wm.title = "2010各国总人数"
wm.add('0-1000万', cc_pops_1)
wm.add('1000万-10亿', cc_pops_2)
wm.add('大于10亿',cc_pops_3)

wm.render_to_file("world_population_1.svg")
