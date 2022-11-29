# Write a programe to findout distance between 2 planets 
# https://www.jpl.nasa.gov/edu/pdfs/scaless_reference.pdf
planet1=int(input('''
Enter 1 for mercury 
Enter 2 for venus 
Enter 3 for Earth 
Enter 4 for Mars
Enter 5 for Jupiter 
Enter 6 for saturn 
Enter 7 for Uranus 
Enter 8 for Neptune '''))
planet2=int(input('''
Enter 1 for mercury 
Enter 2 for venus 
Enter 3 for Earth 
Enter 4 for Mars
Enter 5 for Jupiter 
Enter 6 for saturn 
Enter 7 for Uranus 
Enter 8 for Neptune '''))

answer=0
if  planet1==1 and planet2==2:
    answer=-57900000-(-108200000)
    print(" distance between Mercury to Venus",answer)
elif planet1==2 and planet2==3:
    answer=-108200000-(-149600000)
    print("distance between Venus to Earth",answer)
elif planet1==3 and planet2==4:
    answer=-149600000-(-227900000)
    print("distance between Earth to Mars",answer)
# elif planet1=4 and     