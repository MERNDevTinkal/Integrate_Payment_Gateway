key_id='rzp_test_z7ypKXM2UO4PKA'
key_secret='y8CiQspCr2K9JWPydVnU3Lyn'


  #checkout
import razorpay
client=razorpay.Client(auth=(key_id,key_secret))

#order_id

data={
    'amount':100*100,
    'currency':'INR',
    'receipt':'AIT COLLEGE',
    'notes':{
    'Name':'Pawan Kumar',
    'Paymentfor':'GFG COURSES'

    
    }

   }

order= client.order.create(data=data)
print(order)


  #{'id': 'order_LePztq8NUQkwXT', 'entity': 'order', 'amount': 10000, 'amount_paid': 0, 'amount_due': 10000, 'currency': 'INR', 'receipt': 'AIT COLLEGE', 'offer_id': None, 'status': 'created', 'attempts': 0, 'notes': {'Name': 'Pawan Kumar', 'Paymentfor': 'GFG COURSES'}, 'created_at': 1681638378}






