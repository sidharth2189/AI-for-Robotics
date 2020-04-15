#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

# Initial Belief
p=[0, 1, 0, 0, 0] 

# Environment
world=['green', 'red', 'red', 'green', 'green']

# Measurments
measurements = ['red', 'green']

# Sense propabilities
pHit = 0.6
pMiss = 0.2

# Move probabilities
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# Sense (Input : belief, measurement)
def sense(p, Z):
    q=[]
    for i in range(len(p)):
	# Multiplication
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

# Move (Input : belief, motion model)
def move(p, U):
    q = []
    for i in range(len(p)):
        # Initial Belief
p=[0, 1, 0, 0, 0] 

# Environment
world=['green', 'red', 'red', 'green', 'green']

# Measurments
measurements = ['red', 'green']

# Sense propabilities
pHit = 0.6
pMiss = 0.2

# Move probabilities
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

# Sense (Input : belief, measurement)
def sense(p, Z):
    q=[]
    for i in range(len(p)):
	# Multiplication
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

# Move (Input : belief, motion model)
def move(p, U):
    q = []
    for i in range(len(p)):
        # Convolution
        s = pExact * p[(i-U)%len(p)] + pOvershoot * p[(i-U-1) %len(p)] + pUndershoot * p[(i-U+1) %len(p)]
        q.append(s)
    return q
    
k = 0
m = p
while (k != 1000):
    m = move(m, 1)
    k = k+1;

print (m)
        q.append(s)
    return q
    

print move(p, 1)