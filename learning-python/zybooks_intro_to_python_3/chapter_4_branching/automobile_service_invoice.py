# Automobile service invoice
# The following program outputs automotive services and their costs, then prompts the user
# for 2 services from the list of automotive services, then outputs an invoice for the
# services selected while giving the user the option to enter a dash to indicate no service.
# Date: 09/19/2019
# Author: Edmond Weiss

AUTOMOTIVE_SERVICES = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12
}
MSG_NO_SERVICE = 'No service'

print('Edmond\'s auto shop service')
print('Oil change -- $%s' % AUTOMOTIVE_SERVICES['Oil change'])
print('Tire rotation -- $%s' % AUTOMOTIVE_SERVICES['Tire rotation'])
print('Car wash -- $%s' % AUTOMOTIVE_SERVICES['Car wash'])
print('Car wax -- $%s' % AUTOMOTIVE_SERVICES['Car wax'], end='\n\n')

first_service = input('Select first service: \n\n')
second_service = input('Select second service: \n\n\n')

msg_invoice_first_service = MSG_NO_SERVICE
msg_invoice_second_service = MSG_NO_SERVICE
services_to_sum = []

if (first_service != '-'):
    msg_invoice_first_service = first_service + ', $' + str(AUTOMOTIVE_SERVICES[first_service])
    services_to_sum.append(AUTOMOTIVE_SERVICES[first_service])

if (second_service != '-'):
    msg_invoice_second_service = second_service + ', $' + str(AUTOMOTIVE_SERVICES[second_service])
    services_to_sum.append(AUTOMOTIVE_SERVICES[second_service])

total_auto_services_cost = sum(services_to_sum)

print('Edmond\'s auto shop invoice\n')
print('Service 1: %s' % msg_invoice_first_service)
print('Service 2: %s\n' % msg_invoice_second_service)
print('Total: $%d' % total_auto_services_cost)
