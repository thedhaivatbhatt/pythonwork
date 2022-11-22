# Write a programe to findout distance between 2 planets 
# https://www.jpl.nasa.gov/edu/pdfs/scaless_reference.pdf
sun=1391400
planet1=int(input('''
Enter 1 for mercury 
Enter 2 for venus 
Enter 3 for Earth 
Enter 4 for Mars
Enter 5 for Jupiter 
Enter 6 for saturn 
Enter 7 for Uranus 
Enter 8 for Neptune \n'''))

if planet1==1:
    mercury=41879
    distance=sun-mercury
    print("sun to mercury :",distance)
elif planet1==2:
    venus=12104
    distance=sun-venus
    print("sun to venus :",distance)
elif planet1==3:
    earth=12756
    distance=sun-earth
    print("sun to earth :",distance)
elif planet1==4:
    mars=6792
    distance=sun-mars
    print("sun to mars :",distance)
elif planet1==5:
    jupiter=142984
    distance=sun-jupiter
    print("sun to jupiter:",distance)
elif planet1==6:
    saturn=120536
    distance=sun-saturn
    print("sun to saturn:",distance)
elif planet1==7:
    uranus=51118
    distance=sun-uranus
    print("sun to uranus:",distance)
elif planet1==8:
    neptune=49528
    distance=sun-neptune
    print("sun to neptune:",distance)
else:
    print('invalid')
