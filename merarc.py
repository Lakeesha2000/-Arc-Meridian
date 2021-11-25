import math
def merarc(a,equad,lat1,lat2):
    b=a*math.sqrt(1-equad)
    n=(a-b)/(a+b)
    a0=1.+((n**2)/4.)+((n**4)/64.)
    a2=(3./2.)*(n-((n**3)/8.))
    a4=(15./16.)*((n**2)-((n**4)/4.))
    a6=(35./48.)*(n**3)

    s1=a/(1+n)*(a0*lat1-a2*math.sin(2.*lat1)+a4*math.sin(4.*lat1)-a6*math.sin(6.*lat1))
    s2=a/(1+n)*(a0*lat2-a2*math.sin(2.*lat2)+a4*math.sin(4.*lat2)-a6*math.sin(6.*lat2))
    return s2-s1
    
a = 6378137.
equad =0.00669437999
lat=53.5
lat0=53.5
lat0=math.radians(lat0)
y=merarc(a,equad,lat0,lat)
print(y)
