class DoesnotMatch(Exception):
    def __init__(self,msg="Key and Value not Matched"):
        Exception.__init__(self,msg)
d1={
    "a":"p1",
    "b":"p2",
    "c":"p3",
    "d":"p4",
    "e":"p5"
}
try:
  key=input('Enter the key: ')
  pwd=input('Enter the Password')
  for i in d1:
    if i not in d1.keys():
        print("Match correct")
  else:
        raise DoesnotMatch

except DoesnotMatch as e:
    print(e)
except Exception as e:
    print(e)
print("some task")

