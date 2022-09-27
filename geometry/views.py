from django.shortcuts import render, redirect
from fractions import Fraction
import math
import random
from .models import *
from datetime import datetime


def random_number_generator(start,lenght):
  a = set()
  while len(a) < lenght:
      a.add(random.randint(start,start+500))
  return a

        

def degtoradcalculator(request):
  try:
    if request.method == "GET":
      return render(request,"geometry/degree.html")
    else:
      angle = request.POST['Angle']
      return redirect(f'/geometry/angle-of-{angle}-in-radian/')
  except:
    return render(request,"geometry/degree.html",{'message':"Something went wrong, please try again"})
      

def taildegtoradcalculator(request, angle=None):
  try:
    print(f'angelllll={angle}, {type(angle)}')
    print("I am tail")
    query=degtorad.objects.filter(input=angle)
    if angle != None and len(query)!=0:
      q = query[0]
      context = {
        'Angle':q.input,
        'value':q.result,
        'detailSteps':q.detailSteps,
        "exp":list(random_number_generator(int(float(angle)),15))
      }
      print(context)
      print("***DATABASE******DATABASE*************")
      return render(request,"geometry/taildegtoradcalculator.html",context)

    if angle != None:
      input = float(angle)
      value=math.radians(input)
      value2="{:.2f}".format(value/math.pi)
      value2=Fraction(value2) 
      detailSteps = f'''<h4>{angle}° = {value} radians = {value2} π </h4>
      <br>
      <p>Given that 180° is equal to pi, we can write the following degrees to radians conversion formula:</p>
      <p>α in π radians = α in degrees × π/180, OR</p>
      <p>α rad = α° × π/180</p>
      <p>Plugging the angle value, in degrees, in the previous formula, we get:</p>
      <p>α rad = π × {angle}/180 = {value2} π</p>
      <p style="color:red;">Note: {value2} π rad can be expressed as real number or as a decimal as {value/math.pi}π rad = {value} radian.</p>
      '''
      url = f'/geometry/angle-of-{angle}-in-radian/'
    
      obj = degtorad(input=angle,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":list(random_number_generator(int(float(angle)),15))
      }
      print(context)
      print("****************I am saved in Database*************")
      
      return render(request,"geometry/taildegtoradcalculator.html",context)
  except:
    return render(request,"geometry/degree.html",{'message':"Something went wrong, please try again"})






def radtodegcalculator(request):
  try:
    if request.method == "GET":
      return render(request,"geometry/radian.html")
    else:
      angle = request.POST['Angle']
      return redirect(f'/geometry/angle-of-{angle}-radian-in-degree/')
  except:
    return render(request,"geometry/radian.html",{'message':"Something went wrong, please try again"})




def tailradtodegcalculator(request, angle=None):
  try:
    print(f'angelllll={angle}, {type(angle)}')
    print("I am tail")
    query=radtodeg.objects.filter(input=angle)
    if angle != None and len(query)!=0:
      q = query[0]
      context = {
        'Angle':q.input,
        'value':q.result,
        'detailSteps':q.detailSteps,
        "exp":list(random_number_generator(int(float(angle)),15))
      }
      print(context)
      print("***DATABASE******DATABASE*************")
      return render(request,"geometry/tailradian.html",context)

    if angle != None:
      input = float(angle)
      value=math.degrees(input)

      detailSteps = f'''<h4>{angle}<sup>rad</sup> = {value} degrees</h4>
      <br>
      <p>Given that pi rad is equal to 180°, we can write the following radians to degrees conversion formula:</p>
      <p>α in degrees = α in π radians × 180/π, OR</p>
      <p>α° = α rad × 180/π</p>
      <p>Plugging the given angle value, in radians, in the previous formula, we get:</p>
      <p>α° = ({angle} × 180/π) = {value} degrees</p>
      '''
      url = f'/geometry/angle-of-{angle}-radian-in-degree/'
    
      obj = radtodeg(input=angle,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":list(random_number_generator(int(float(angle)),15))
      }
      # print(context)
      print("****************I am saved in Database*************")
      
      return render(request,"geometry/tailradian.html",context)
  except:
    return render(request,"geometry/radian.html",{'message':"Something went wrong, please try again"})


  