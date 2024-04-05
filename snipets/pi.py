#69 digits of pi
import decimal
decimal.getcontext().prec = 69
def binary_split(a, b):
    if b == a + 1:
        if a == 0:
            Pab, Qab = 1, 1
        else:
            Pab = -(6*a - 5)*(2*a - 1)*(6*a - 1)
            Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab
def chudnovsky (n):
    Pon, Qon, Ron = binary_split(0, n)
    return (426880 * decimal. Decimal(10005).sqrt() * Qon) / Ron
print(chudnovsky (7))

