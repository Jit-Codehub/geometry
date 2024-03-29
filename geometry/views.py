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

def random_number_generator2(end,lenght):
  a = set()
  while len(a) < lenght:
      a.add(random.randint(0,end))
  return a

def get_float_list(start, stop, size):
    '''generates unique random float numbers list'''
    result = []
    unique_set = set()
    for i in range(size):
        x = round(random.uniform(start, stop),2)
        while x in unique_set:
            x = round(random.uniform(start, stop),2)
        unique_set.add(x)
        result.append(x)

    return result

        

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





def supplementarycalculator(request):
  try:
    if request.method == "GET":
      return render(request,"geometry/supplementary.html")
    else:
      angle = request.POST['Angle']
      angle_type = request.POST['AG_TY']

      if angle_type == "radian" and float(angle)>math.pi:
        return render(request,"geometry/supplementary.html",{'message':f"Angle can not be greater than {math.pi} radians",'Angle':"angle","AG_TY":angle_type})

      return redirect(f'/geometry/supplementary-angle-of-{angle}-in-{angle_type}/')
  except:
    return render(request,"geometry/supplementary.html",{'message':"Something went wrong, please try again"})



def tailsupplementarycalculator(request,angle=None,angle_type=None):
  try:
    print("I am tail")
    print(f'angle_type={angle_type}')
    print(f'angle={angle}')
    
    query=supplementary.objects.filter(input=angle,input_type=angle_type)
    if angle != None and len(query)!=0:
      q = query[0]
      context = {
        'Angle':q.input,
        'value':q.result,
        'detailSteps':q.detailSteps,
        "exp":list(random_number_generator2(180,10)) if angle_type == 'degree' else get_float_list(0, 3.14, 10)
      }
      print(context)
      print("***DATABASE******DATABASE*************")
      if angle_type == 'degree':
        return render(request,"geometry/supplementary-Degree.html",context)
      else:
        return render(request,"geometry/supplementary-Radian.html",context)
    print(f'I am outside degree')
    if angle != None and angle_type == 'degree':
      print(f'I am inside degree')
      input = float(angle)
      value=180-input
      if int(value) == value:
        value = int(value)
      

      detailSteps = f'''<h4>Supplementary angle of {angle}<sup>°</sup> is 
                {value}<sup>°</sup></h4><h1></h1>

                <p>To find the suplement of an angle, say 'x', use the formula below:</p><p>Suplement of x° = 180° - x</p>

              <p>So, the supplementary angle of {angle}° = 180 - {angle} = {value}</p>

              <p style="color: red;">Important: the angle unit is set to degrees.</p>'''
      url = f'/geometry/supplementary-angle-of-{angle}-in-{angle_type}/'
      
      
      obj = supplementary(input=angle,input_type=angle_type,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":list(random_number_generator2(180,10))
      }
      print(context)
      print("****************I am saved in Degree Database*************")
      
      return render(request,"geometry/supplementary-Degree.html",context)

    if angle != None and angle_type == 'radian':
      print(f'I am inside radian')
      input = float(angle)
      value=math.pi-input
      if int(value) == value:
        value = int(value)
      value2=value/math.pi
      print('value2=',value2)
      

      detailSteps = f'''<h4>Supplementary angle of {angle}<sup>rad</sup> is 
                {value}<sup>rad</sup> (in terms of π)</h4><h1></h1>

                <p>To find the suplement of an angle, say 'x', use the formula below:</p><p>Suplement of x<sup>rad</sup> = π - x</p>

              <p>So, the suplementary angle of {angle} radian = π - {angle} = {value}<sup>rad</sup></p>

              <p style="color: red;">Important: the angle unit is set to radians.</p>'''
      url = f'/geometry/supplementary-angle-of-{angle}-in-{angle_type}/'
      
      
      obj = supplementary(input=angle,input_type=angle_type,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":get_float_list(0, 3.14, 10)
      }
      print(context)
      print("****************I am saved in Radian Database*************")
      
      return render(request,"geometry/supplementary-Radian.html",context)
  except:
    return render(request,"geometry/supplementary.html",{'message':"Something went wrong, please try again"})



def complementarycalculator(request):
  try:
    if request.method == "GET":
      return render(request,"geometry/complementary.html")
    else:
      angle = request.POST['Angle']
      angle_type = request.POST['AG_TY']

      if angle_type == "radian" and float(angle)>(math.pi/2):
        return render(request,"geometry/complementary.html",{'message':f"Angle can not be greater than {math.pi/2} radians",'Angle':"angle","AG_TY":angle_type})

      return redirect(f'/geometry/complementary-angle-of-{angle}-in-{angle_type}/')
  except:
    return render(request,"geometry/complementary.html",{'message':"Something went wrong, please try again"})




def tailcomplementarycalculator(request,angle=None,angle_type=None):
  try:
    print("I am tail")
    print(f'angle_type={angle_type}')
    print(f'angle={angle}')
    
    query=complementary.objects.filter(input=angle,input_type=angle_type)
    if angle != None and len(query)!=0:
      q = query[0]
      context = {
        'Angle':q.input,
        'value':q.result,
        'detailSteps':q.detailSteps,
        "exp":list(random_number_generator2(90,10)) if angle_type == 'degree' else get_float_list(0, 1.57, 10)
      }
      print(context)
      print("***DATABASE******DATABASE*************")
      if angle_type == 'degree':
        return render(request,"geometry/complementary-Degree.html",context)
      else:
        return render(request,"geometry/complementary-Radian.html",context)
    print(f'I am outside degree')
    if angle != None and angle_type == 'degree':
      print(f'I am inside degree')
      input = float(angle)
      value=90-input
      if int(value) == value:
        value = int(value)
      

      detailSteps = f'''<h4>Complementary angle of {angle}<sup>°</sup> is 
                {value}<sup>°</sup></h4><h1></h1>

                <p>To find the complement of an angle, say 'x', use the formula below:</p><p>Complement of x° = 90° - x</p>

              <p>So, the complementary angle of {angle}° = 90 - {angle} = {value}</p>

              <p style="color: red;">Important: the angle unit is set to degrees.</p>'''
      url = f'/geometry/complementary-angle-of-{angle}-in-{angle_type}/'
      
      
      obj = complementary(input=angle,input_type=angle_type,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":list(random_number_generator2(90,10))
      }
      print(context)
      print("****************I am saved in Degree Database*************")
      
      return render(request,"geometry/complementary-Degree.html",context)

    if angle != None and angle_type == 'radian':
      print(f'I am inside radian')
      input = float(angle)
      value=(math.pi/2)-input
      if int(value) == value:
        value = int(value)

      

      detailSteps = f'''<h4>Complementary  angle of {angle}<sup>rad</sup> is 
                {value}<sup>rad</sup> (in terms of π)</h4><h1></h1>

                <p>To find the Complementary  of an angle, say 'x', use the formula below:</p><p>Complementary of x<sup>rad</sup> = π/2 - x</p>

              <p>So, the suplementary angle of {angle} radian = π/2 - {angle} = {value}<sup>rad</sup></p>

              <p style="color: red;">Important: the angle unit is set to radians.</p>'''
      url = f'/geometry/complementary-angle-of-{angle}-in-{angle_type}/'
      
      
      obj = complementary(input=angle,input_type=angle_type,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":get_float_list(0, 1.57, 10)
      }
      print(context)
      print("****************I am saved in Radian Database*************")
      
      return render(request,"geometry/complementary-Radian.html",context)
  except:
    return render(request,"geometry/complementary.html",{'message':"Something went wrong, please try again"})




def reflexcalculator(request):
  try:
    if request.method == "GET":
      return render(request,"geometry/reflex.html")
    else:
      angle = request.POST['Angle']
      angle_type = request.POST['AG_TY']

      if angle_type == "radian" and float(angle)>(2*math.pi):
        return render(request,"geometry/reflex.html",{'message':f"Angle can not be greater than {2*math.pi} radians",'Angle':"angle","AG_TY":angle_type})

      return redirect(f'/geometry/reflex-angle-of-{angle}-in-{angle_type}/')
  except:
    return render(request,"geometry/reflex.html",{'message':"Something went wrong, please try again"})



def tailreflexcalculator(request,angle=None,angle_type=None):
  try:
    print("I am tail")
    print(f'angle_type={angle_type}')
    print(f'angle={angle}')
    
    query=reflex.objects.filter(input=angle,input_type=angle_type)
    if angle != None and len(query)!=0:
      q = query[0]
      context = {
        'Angle':q.input,
        'value':q.result,
        'detailSteps':q.detailSteps,
        "exp":list(random_number_generator2(360,10)) if angle_type == 'degree' else get_float_list(0, 6.28, 10)
      }
      print(context)
      print("***DATABASE******DATABASE*************")
      if angle_type == 'degree':
        return render(request,"geometry/reflex-Degree.html",context)
      else:
        return render(request,"geometry/reflex-Radian.html",context)
    print(f'I am outside degree')
    if angle != None and angle_type == 'degree':
      print(f'I am inside degree')
      input = float(angle)
      value=360-input
      if int(value) == value:
        value = int(value)
      

      detailSteps = f'''<h4>Reflex angle of {angle}<sup>°</sup> is 
                {value}<sup>°</sup></h4><h1></h1>

                <p>To find the Reflex of an angle, say 'x', use the formula below:</p><p>Reflex of x° = 360° - x</p>

              <p>So, the Reflex angle of {angle}° = 360 - {angle} = {value}</p>

              <p style="color: red;">Important: the angle unit is set to degrees.</p>'''
      url = f'/geometry/reflex-angle-of-{angle}-in-{angle_type}/'
      
      
      obj = reflex(input=angle,input_type=angle_type,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":list(random_number_generator2(360,10))
      }
      print(context)
      print("****************I am saved in Degree Database*************")
      
      return render(request,"geometry/reflex-Degree.html",context)

    if angle != None and angle_type == 'radian':
      print(f'I am inside radian')
      input = float(angle)
      value=(2*math.pi)-input
      if int(value) == value:
        value = int(value)

      

      detailSteps = f'''<h4>Reflex angle of {angle}<sup>rad</sup> is 
                {value}<sup>rad</sup> (in terms of π)</h4><h1></h1>

                <p>To find the Reflex of an angle, say 'x', use the formula below:</p><p>Reflex of x<sup>rad</sup> = 2π - x</p>

              <p>So, the Reflex angle of {angle} radian = 2π - {angle} = {value}<sup>rad</sup></p>

              <p style="color: red;">Important: the angle unit is set to radians.</p>'''
      url = f'/geometry/reflex-angle-of-{angle}-in-{angle_type}/'
      
      
      obj = reflex(input=angle,input_type=angle_type,result=value,detailSteps=detailSteps,url=url,date_modified=datetime.now())
      obj.save()
      context = {
        'Angle':angle,
        'value':value,
        'detailSteps':detailSteps,
        "exp":get_float_list(0, 6.28, 10)
      }
      print(context)
      print("****************I am saved in Radian Database*************")
      
      return render(request,"geometry/reflex-Radian.html",context)
  except:
    return render(request,"geometry/reflex.html",{'message':"Something went wrong, please try again"})



  