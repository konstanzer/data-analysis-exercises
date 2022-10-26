import numpy as np

#1
days = np.array([3,5,1])
price = 3
total = np.sum(price*days)

#2
rates = dict(goog=400, amzn=380, fb=350)
hours = dict(goog=6, amzn=4, fb=10)

def earnings(rates, hours):
	earned = 0
	for k, v in hours.items():
		earned += rates[k]*v
	return earned

#3
student_slots = np.zeros(10)
class_slots = [0,4] 
class_enrollment = 18;

def can_enroll(class_enrollment, class_slots, student_slots):
	max_class_size = 21
	if class_enrollment >= max_class_size:
		return False
	for s in class_slots:
		if student_slots[s] == 1:
			return False
		else:
			student_slots[s] == 1
	return True

#4
cart_items = 2
offer_expired = False
premium = False

def apply_offer(cart_items, offer_expired, premium):
	if cart_items > 2 and not offer_expired:
		return True
	elif premium:
		return True
	else:
		return False

#5
username = 'codeup'
password = 'notastrongpassword'

def verify(username, password):
	verified = np.zeros(4)

	if len(password) >= 5:
		verified[0] = True
	if len(username) <= 20:
		verified[1] = True
	if username != password:
		verified[2] = True
	if username.strip() == username:
		if password.strip() == password:
			verified[3] = True
	
	return all(verified)


if __name__ == "__main__":
	print("Rentals cost ${0:.2f}".format(total))
	print("You made ${0:.2f}".format(earnings(rates, hours)))
	print("Student enrolled: " +
		str(can_enroll(class_enrollment, class_slots, student_slots)))
	print("Apply offer: " +
		str(apply_offer(cart_items, offer_expired, premium)))
	print("Verified: " + str(verify(username, password)))


