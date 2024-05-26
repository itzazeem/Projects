import ast
input_type={
  int: 'integer',
  float: 'float',
  complex: 'complex',
  bool: 'boolean',
  str: 'string',
  list: 'list',
  tuple: 'tuple',
  dict: 'dictionary',
}
a=input("Enter Value For Checking The Data Type ")
try:
  b=int(a)
  print("Input Is Of Type",input_type[int])
  
    # print(a)
except:
  try:
    b=float(a)
    print("Input Is Of Type",type(b).__name__)
  except:
    try:
      b=complex(a)
      print("Input Is Of Type",type(b).__name__)
    except:
        if (a=='true' or a=='True' or a=='false' or a=='False'):
          b=bool(a)
          print("Input Is Of Type",input_type[bool])
        else:
          try:
            b = ast.literal_eval(a)
            if isinstance(b, tuple):
              print("Input Is Of Type",type(b).__name__) 
            elif isinstance(b, list):
              print("Input Is Of Type",type(b).__name__)  
            elif isinstance(b, dict):
              print("Input Is Of Type",input_type[dict])  
            else:
              print("Input Is Of Type",type(b).__name__)
          except:
            print("Input Is Of Type",input_type[str])
            