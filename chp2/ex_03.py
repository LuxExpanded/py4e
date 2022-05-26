Hours = input('Enter Hours: ')
Rate = input('Enter Payrate: ')
OT = input('Enter Overtime, Enter 0 if none:')
Pay = float(Hours) * float(Rate) + (float(OT) *(1.5*float(Rate)))
Net = Pay * .8535
print('Gross Pay: ',Pay)
print('Net Pay: ',Net)
