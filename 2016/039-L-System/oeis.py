# https://oeis.org/A269962
# 1, 5, 17, 45, 105, 237, 537, 1229, 2825, 6493, 14905, 34189, 78409, 179837, 412505, 946221, 2170473, 4978653, 11420025, 26195213, 60086537, 137826493, 316146457, 725176813, 1663410601, 3815531165, 8752065209, 20075486925, 46049151561, 105627543165

a = [1,5,17,45,105]
b = [1,5,17,45,105]
for n in range(5,20):
    a.append(4*a[n-1] - 5*a[n-2] + 2*a[n-3] + 2*a[n-4] - 2*a[n-5])
    b.append(3*a[n-1] - 2*a[n-2]            + 2*a[n-4]            + 2)
    print a[-1],b[-1]