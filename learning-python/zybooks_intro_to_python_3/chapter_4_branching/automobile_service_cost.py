# Automobile Service Cost
# The following program prompts the user for an automobile service and outputs
# the user's input. Then the program outputs the price of the requested
# service. The program supports the following services: oil change $35, tire
# rotation $19, and car wash $7. An error message is displayed when a service
# entered by a user is not in the list.

services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7
}
unlisted_service_err_msg = 'Error: Requested service is not recognized.'

requested_service = input('Enter desired auto service: \n')
print('You entered:', requested_service, end='\n\n')
if requested_service in services:
    print('Cost of %s: $%d' %
          (requested_service.lower(), services[requested_service]))
else:
    print(unlisted_service_err_msg)
