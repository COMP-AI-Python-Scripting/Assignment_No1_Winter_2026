import turtle as t

t.setworldcoordinates(-50, -50, 325, 325)
t.pensize(4)

colours = {'walls': 'red', 'roof': 'green', 'door': 'blue'}

house_components ={
        'walls': {'start': (0,0), 'path': [(200,0), (200,200), (0,200), (0,0)]},
        'roof' : {'start': (200,200), 'path': [(100, 250), (0,200)]},
        'door' : {'start': (75,0), 'path': [(75,125), (125,125), (125,0), (75,0)]}
}

for component, structure in house_components.items():
    print(f"Building the {component}.")
    t.color(colours[component])
    t.teleport(*structure['start'])
    coordinates = structure['path']
    if component == 'door':
        t.begin_fill()
        t.fillcolor('green')
        for point in coordinates:
            t.goto(*point)
        t.end_fill()
        t.exitonclick()
    else:
        for point in coordinates:
            t.goto(*point)

t.exitonclick()
