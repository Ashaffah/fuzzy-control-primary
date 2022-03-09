import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Variabel dan fungsi keanggotaan
req_max   = np.arange(0, 6000, 1)
req_ready = np.arange(0, 6000, 1)
i_product = np.arange(0, 6000, 1)

# Rules

req_a = fuzz.trapmf(req_max, [0, 0, 100, 5000])
req_b = fuzz.trapmf(req_max, [1000, 5000, 6000, 6000])

ready_a = fuzz.trapmf(req_ready, [0, 0, 100, 600])
ready_b = fuzz.trapmf(req_ready, [100, 600, 700, 700])

product_a = fuzz.trapmf(i_product, [0, 0, 2000, 7000])
product_b = fuzz.trapmf(i_product, [2000, 7000, 9000, 9000])

#PLOTING
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(req_max, req_a, 'b', linewidth=1.5, label='Sedikit')
ax0.plot(req_ready, req_b, 'g', linewidth=1.5, label='Banyak')

ax0.set_title('Permintaan')
ax0.legend()

ax1.plot(req_ready, ready_a, 'b', linewidth=1.5, label='Sedikit')
ax1.plot(req_ready, ready_b, 'g', linewidth=1.5, label='Banyak')


ax1.set_title('Persediaan')
ax1.legend()

ax2.plot(i_product, product_a, 'b', linewidth=1.5, label='Berkurang')
ax2.plot(i_product, product_b, 'g', linewidth=1.5, label='Bertambah')

ax2.set_title('Produksi')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

minta =  4000
sedia =  300

in1 = []
in1.append(fuzz.interp_membership(req_max, req_a, minta))
in1.append(fuzz.interp_membership(req_max, req_b, minta))
in2 = []
in2.append(fuzz.interp_membership(req_ready, ready_a, sedia))
in2.append(fuzz.interp_membership(req_ready, ready_b, sedia))


print("Derajat Keanggotaan Persediaan ")
if in1[0]>0 :
    print("Sedikit : "+str(in2[0]))
if in1[1]>0 :
    print("Banyak  : "+ str(in2[1]))

print("")
print("Derajat Keanggotaan Permintaan")
if in2[0]>0 :
    print("Sedikit : "+str(in1[0]))
if in2[1]>0 :
    print("Banyak  : "+ str(in1[1]))
    
#derajat keanggotaan persediaan
Sedikit : 0.6
Banyak  : 0.4

#derajat keanggotaan permintaan
Sedikit : 0.75
Banyak  : 0.25

## Rules and Inferences Tsukamoto
# krg = 7000 - (active_rule3)*5000
# tbh = 5000*deg + 2000

apred1  = np.fmin(in1[1], in2[1])
print("nilai apred1 = ", apred1)
z1      = 5000*apred1 + 2000

apred2  = np.fmin(in1[0], in2[0])
print("nilai apred2 = ", apred2)
z2      = 7000-(apred2)*5000

apred3  = np.fmin(in1[0], in2[1])
print("nilai apred3 = ", apred3)
z3      = 7000-(apred3)*5000

apred4  = np.fmin(in1[1], in2[0])
print("nilai apred4 = ", apred4)
z4      = 5000*apred4 + 2000

print(z1,z2,z3,z4)
## Defazzyfication
z = (apred1*z1 + apred2*z2 + apred3*z3 + apred4*z4)/ (apred1 + apred2+ apred3 + apred4)

print("Barang yang harus di produksi : "+str(int(z)))