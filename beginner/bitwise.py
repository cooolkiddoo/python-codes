def max():
   	x=int(input())
   	y=int (input())
   	z=int(input())
   	if (x>y):
      if(x>z):
    			print (x)
   		else :
    			print(z)
   	elif (b>c):
   		print (y)
   	else:
   		print (z)
def main():
   	try:
    		max()
   	except ValueError:
    		print('invalid')
main()
