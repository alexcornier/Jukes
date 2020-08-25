import random
import matplotlib.pyplot as plt
import math

#FUNCTION

#Return a string with the alphabet associated to
#the type passed as a string
def alphabet(type):
    if (type == "nucleic"):
       return "acgt"
    elif (type == "protein"):
        return "AVLIPFWYMCGDENQSTKRH"
    elif (type == "iupac_nucleic"):
        return "ACGTRYSWKMBDHVN"
    elif (type == "iupac_protein"):
        return "ACDEFGHIKLMNPQRSTVWY"


#Return as a string a Sequence built randomly using
#the lengh as integer
#the alphabet as a string
def randseq(num,alpha):
    seq = str("")
    for alphacount in range (num):
        irand = random.randint(0,len(alpha)-1)
        seq = seq + alpha[irand]
    return seq


#Return as integer the hamming distance between
#the two sequences passed as string
def hamming(seq1,seq2):
    iham = 0
    ihrange = len(seq1)
    #Test both sequences length, set counter to the lowest
    #add the gap to the distance
    #Returning an error is also an option
    #as different lengths doesn't make sense here
    if (len(seq1) != len(seq2)):
        if  (len(seq1) >  len(seq2)):
            ihrange = len(seq2)
            iham = len(seq1)-len(seq2)
            
        elif (len(seq1) < len(seq2)):
             ihrange = len(seq1)
             iham = len(seq2)-len(seq1)
    #Add one if the current letter in both seq is different
    ihcount = 0
    for ihcount in range (ihrange) :
        if ((seq1[ihcount]) != (seq2[ihcount])):
            iham = iham + 1
    return iham


#Return as a list the hamming distance and the mutated sequence (as a list)
#for an initial sequence passed as a string
#and a number of substitutions passed as integer
#Functions used: alphabet, randseq and hamming
def mutate(seq,num_subs):
    lsmutate =[]
    #Convert the sequence from string to list of characters
    for ilscount in range (len(seq)):
        lsmutate.append(seq[ilscount])
    #Execute the number of substitutions requested
    #one letter at a time, randomly from the alphabet
    for imcount in range (num_subs):
        imrand = random.randint(0,len(seq)-1)
        almutate = alphabet("nucleic")
        cmutate = randseq(1,almutate)
        lsmutate[imrand] = cmutate
    hmutate = hamming(seq,lsmutate)
    return hmutate, lsmutate


#Return a list of hamming distance and mutated sequence (as list)
# for number of experiments
#le: Sequence length as integer
#su: Number of substitutions as integer
#nb: Number of experiments as integer
#Functions used: alphabet, randseq and mutate
def experiments(le,su,nb):
   v = []
   for i in  range(nb):
       alexp = alphabet("nucleic")
       seq = randseq(le,alexp)
       v.append( mutate(seq,su) )
   return v


#Return the mean computed from a list of integers passed as arguments
def mean(data):
    itotal = 0
    ilenmean = len(data)
    for icountmean in range (ilenmean) :
        itotal = itotal + data[icountmean]
    imean =int(itotal/ilenmean)
    return imean


#Return the variance computed from a list of integers
#using the Welford’s method in a single pass
def variance(data):
    ivmean = 0
    ivsum = 0
    ivlen = len(data)
    for ivcount in range (ivlen) :
        idata = data[ivcount]
        ivoldmean = ivmean
        ivmean = ivmean + (idata - ivmean)/(ivcount+1)
        ivsum = ivsum + (idata - ivmean)*(idata - ivoldmean)
    result = ivsum/(ivlen-1)
    return result


#Return the standard deviation computed from a list of integers
#Functions used: variance and sqrt from the math module
def std(data):
    varstd = variance(data)
    return math.sqrt(varstd)


#Return the genetic distance according to the Jukes Cantor model (1969)
#means: mean of hamming distance for instance, passed as integer
#L: sequence length
#Function used: log from the math module (natural logarithm)
def distanceJC69(means, L):
    d =  means / L
    result = (-3/4)* math.log(1-(4*d/3))
    return result


#Return a list of hamming distances and JC69 distances computed
#for a range of substitutions
#le: sequence length as integer
#nb: number of experiments as integer
#xx: number of substitutions as a list of integers
#Functions used: experiments, mean and distanceJC69
def generate(le,nb,xx):
    lsexp = []
    lsham = []
    lsJC69 = []
    #Compute hamming and JC69 for each number of substitutions
    for icountsubst in range (len(xx)) :
        lsdis = []
        #Load as a list the result of experiments
        lsexp.append(experiments(le, xx[icountsubst], nb))
        #Load as a list only the hamming distance for the nb experiments
        #from the preloaded list
        for icountexp in range (nb):
             lsdis.append(lsexp[icountsubst][icountexp][0])
        #Compute the mean of hamming distances for the current number
        #of substitutions
        imeandis = mean(lsdis)
        #Create the result list of hamming distances
        lsham.append(imeandis)
        #Create the result list of JC69 distances
        lsJC69.append (distanceJC69(imeandis, le))
    return lsham, lsJC69

#Plot distances by substitution nb ----------
L = 1000
R = 10
x = list(range(100,2200,200))
data = generate(L,R,x)
#print(data[0])
#print(data[1])

#Set Data
xx = x
yy = data[0]
zz = data[1]

# Create first axis
fig = plt.figure()
ax1 = fig.add_subplot(111)

ax1.set_xlabel('Number of Substitutions')
ax1.set_ylabel('Hamming Distances')
ax1.plot(xx, yy, color='b', label='Hamming Distances (means)')
ax1.tick_params(axis='y', labelcolor='b')

#Create second axis
ax2 = ax1.twinx()
ax2.set_ylabel('JC69 Distances')
ax2.plot(xx, zz, color='r', label='JC69 Distances')
ax2.tick_params(axis='y', labelcolor='r')

#Handle legend
fig.legend(loc="upper left", bbox_to_anchor=(0,1), bbox_transform=ax1.transAxes)

#Plot
plt.title("True Substitution number vs Hamming and JC69 Distances")
fig.tight_layout()
plt.show()
