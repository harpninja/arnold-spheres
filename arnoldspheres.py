'''
Demonstration of Maya 2018 scene creation using Python.
Shaders are configured for Arnold render.
'''
import random
import math
import maya.cmds as cmds

# place n random size and colour spheres on a plane
i = 0
n = 100
PADDING = 0.2
sphereList = []

def add_sphere():
    '''
    Add sphere name to list of spheres.
    Create and add a sphere to scene.
    Create a randomly coloured Arnold shader.
    Add shader to the sphere.
    '''
    sphereList.append(nameSphere)
    name_shader = 'aiStandardSurface'+nameSphere
    red = random.uniform(0.8, 1.0)
    green = random.uniform(0.2, 1.0)
    blue = random.uniform(0.2, 1.0)
    cmds.polySphere(n=nameSphere, r=radius)
    cmds.move(x, radius, z)
    cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=name_shader+'SG')
    cmds.shadingNode('aiStandardSurface', asShader=True, name=name_shader)
    cmds.setAttr(name_shader+'.baseColor', red, green, blue, type='double3')
    cmds.setAttr(name_shader+'.base', 0.85)         # diffuse weight
    cmds.setAttr(name_shader+'.specular', 0.05)     # specular weight
    cmds.connectAttr(name_shader+'.outColor', name_shader+'SG.surfaceShader')
    cmds.sets(nameSphere, edit=True, forceElement=name_shader+'SG')

def intersection_test():
    '''
    Test for intersections before placing a sphere.
    '''
    for j in range(0, len(sphereList)):
        obj_name = 'sphere'+str(j)
        poly_name = 'polySphere'+str(j + 1)
        x1 = cmds.getAttr(obj_name+'.tx')
        z1 = cmds.getAttr(obj_name+'.tz')
        r1 = cmds.getAttr(poly_name+'.radius')

        x_axis = (x1-x)**2
        z_axis = (z1-z)**2
        d = math.sqrt(x_axis + z_axis)

        if d < (r1 + radius + PADDING):
            return 1
    return 0

# draw!
while i < n:
    x = random.uniform(-20, 20)
    z = random.uniform(-20, 20)
    radius = random.uniform(0.2, 0.8)

    if not sphereList:
        nameSphere = 'sphere'+str(i)
        add_sphere()
        i = i + 1

    if intersection_test() == 0:
        nameSphere = 'sphere'+str(i)
        add_sphere()
        i = i + 1
