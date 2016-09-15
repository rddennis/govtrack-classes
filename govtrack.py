import urllib2
import json
import pprint

class Bill():
	
	def __init__(self):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill")
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.allBills = billData

	def bill_by_id(self, bill_id):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill/" + str(bill_id))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billInformation = billData
		return self.billInformation


	def bill_by_resolution_type(self, resolution_type):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?q=" + resolution_type)
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByResolutionType = billData
		return self.billsByResolutionType


	def bill_by_bill_type(self, bill_type):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?bill_type=" + bill_type.lower().replace(" ", "_"))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByBillType = billData
		return self.billsByBillType

	def bill_by_committee(self, committee_name):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/committee?limit=306")
		apiRead = apiCall.read()
		committeeData = json.loads(apiRead)
		apiCall.close()
	
		for committees in committeeData["objects"]:
			if committee_name == committees["name"]:
				committee_ID = committees["id"]	
				break

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?committees=" + str(committee_ID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCommittee = billData
		return self.billsByCommittee


	def bill_by_congress(self, congress):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?congress=" + str(congress))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCongress = billData
		return self.billsByCongress

	def bill_by_cosponsor(self, cosponsorName):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person?q=" + cosponsorName.replace(" ", "+"))
		apiRead = apiCall.read()
		cosponsorData = json.loads(apiRead)
		apiCall.close()

		cosponsorID = cosponsorData["objects"][0]["id"]
		

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?cosponsors=" + str(cosponsorID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCosponsor = billData
		return self.billsByCosponsor


	def bill_by_current_status(self, current_status):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?current_status=" + current_status.lower().replace(" ", "_"))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCurrentStatus = billData
		return self.billsByCurrentStatus

	def bill_by_current_status_date(self, current_status_date):
		import datetime

		current_status_date = datetime.datetime(int(current_status_date[0]), int(current_status_date[1]), int(current_status_date[2]))
		current_status_date.strftime('%y%m%d')
		current_status_date = str(current_status_date)
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?current_status_date=" + current_status_date)
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCurrentStatusDate = billData
		return self.billsByCurrentStatusDate


	def bill_by_introduced_date(self, introduced_date):
		import datetime

		introduced_date = datetime.datetime(int(introduced_date[0]), int(introduced_date[1]), int(introduced_date[2]))
		introduced_date.strftime('%y%m%d')
		introduced_date = str(introduced_date)
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?introduced_date=" + introduced_date)
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByIntroducedDate = billData
		return self.billsByIntroducedDate


	def bill_by_number(self, number):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?number=" + str(number))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByNumber = billData
		return self.billsByNumber
	
	def bill_by_sponsor(self, sponsorName):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person?q=" + sponsorName.replace(" ", "+"))
		apiRead = apiCall.read()
		cosponsorData = json.loads(apiRead)
		apiCall.close()

		sponsorID = cosponsorData["objects"][0]["id"]

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?sponsor=" + str(sponsorID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsBySponsor = billData
		return self.billsBySponsor

	def bill_by_terms(self, termID):

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?terms=" + str(termID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByTerms = billData
		return self.billsByTerms
		

class Cosponsorship():

	def __init__(self):
		pass

	def cosponsorship_by_bill(self, billID):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship?bill=" + str(billID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billCoSponsorData = billData

		billCoSponsors = []

		for cosponsor in billData["objects"]:
			billCoSponsors.append({"cosponsorID": cosponsor["person"]})
		
		for person in billCoSponsors:
			apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person/" + str(person["cosponsorID"]))
			apiRead = apiCall.read()
			personData = json.loads(apiRead)
			apiCall.close()

			if person["cosponsorID"] == personData["id"]:
				person["name"] = personData["name"]


		self.billCoSponsors = billCoSponsors

		return self.billCoSponsors
	
	def cosponsorship_by_join_date(self, join_date):
		import datetime

		join_date = datetime.datetime(int(join_date[0]), int(join_date[1]), int(join_date[2]))
		join_date.strftime('%y%m%d')
		join_date = str(join_date)
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship?joined=" + join_date + '&limit=5')
		apiRead = apiCall.read()
		joinDateData = json.loads(apiRead)
		apiCall.close()

		self.joinDateData = joinDateData

		cosponsorbyJoinDateList = []

		for cosponsor in joinDateData["objects"]:
			cosponsorbyJoinDateList.append({"cosponsorID": cosponsor["person"]})
		
		for person in cosponsorbyJoinDateList:
			apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person/" + str(person["cosponsorID"]))
			apiRead = apiCall.read()
			personData = json.loads(apiRead)
			apiCall.close()

			if person["cosponsorID"] == personData["id"]:
				person["name"] = personData["name"]


		self.cosponsorbyJoinDateList = cosponsorbyJoinDateList

		return self.cosponsorbyJoinDateList


	def cosponsorship_by_person(self, cosponsorName):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person?q=" + cosponsorName.replace(" ", "+"))
		apiRead = apiCall.read()
		cosponsorData = json.loads(apiRead)
		apiCall.close()

		cosponsorID = cosponsorData["objects"][0]["id"]
		

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?cosponsors=" + str(cosponsorID))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		self.billsByCosponsor = billData
		return self.billsByCosponsor

	def cosponsorship_by_role(self, roleID):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship?role=" + str(roleID))
		apiRead = apiCall.read()
		cosponsorRoleData = json.loads(apiRead)
		apiCall.close()

		self.cosponsorshipRoleData = cosponsorRoleData

		billList = []

		for bill in cosponsorRoleData["objects"]:
			billList.append({"bill": bill["bill"]})

		for bill in billList:
			apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill/" + str(bill["bill"]))
			apiRead = apiCall.read()
			billData = json.loads(apiRead)
			apiCall.close()

			bill["name"] = billData["title"]

		self.billList = billList

		return self.billList


	def cosponsorship_by_cosponsorshipID(self, cosponsorshipID):
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/cosponsorship/" + str(cosponsorshipID))
		apiRead = apiCall.read()
		cosponsorRoleData = json.loads(apiRead)
		apiCall.close()

		cosponsorInformation = {}

		cosponsorInformation["cosponsorID"] = cosponsorRoleData["person"]	
		cosponsorInformation["billID"] = cosponsorRoleData["bill"]

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill/" + str(cosponsorInformation["billID"]))
		apiRead = apiCall.read()
		billData = json.loads(apiRead)
		apiCall.close()

		cosponsorInformation["billName"] = billData["title"]

		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/person/" + str(cosponsorInformation["cosponsorID"]))
		apiRead = apiCall.read()
		personData = json.loads(apiRead)
		apiCall.close()

		cosponsorInformation["cosponsorName"] = personData["name"]

		self.cosponsorInformation = cosponsorInformation

		return self.cosponsorInformation



print "This will run each method. Should you run into an error, smile, go back and make your updates!!\n"
print "\nBill.bill_by_id(6031): "
pprint.pprint(Bill().bill_by_id(6031))
print "\nBill.bill_by_resolution_type(\"bill\"): "
pprint.pprint(Bill().bill_by_resolution_type("bill"))
print '\nBill.bill_by_bill_type("house bill"): '
pprint.pprint(Bill().bill_by_bill_type("house bill"))
print '\nBill.bill_by_committee("Energy and Power"): '
pprint.pprint(Bill().bill_by_committee("Energy and Power"))
print '\nBill.bill_by_congress(112): '
pprint.pprint(Bill().bill_by_congress(112))
print '\nBill.bill_by_cosponsor("Barack Obama"): '
pprint.pprint(Bill().bill_by_cosponsor("Barack Obama"))
print '\nBill.bill_by_current_status("prov kill veto"): '
pprint.pprint(Bill().bill_by_current_status("prov kill veto") )
print '\nBill.bill_by_current_status_date((2016,03,14)): '
pprint.pprint(Bill().bill_by_current_status_date((2016,03,14)))
print '\nBill.bill_by_introduced_date((2016,03,14)): '
pprint.pprint(Bill().bill_by_introduced_date((2016,03,14)))
print '\nBill.bill_by_terms(5928): '
pprint.pprint(Bill().bill_by_terms(5928))
print '\nBill.bill_by_sponsor("Shelley Capito"): '
pprint.pprint(Bill().bill_by_sponsor("Shelley Capito"))

print '\nCosponsorship().cosponsorship_by_bill(6031): '
pprint.pprint(Cosponsorship().cosponsorship_by_bill(6031))
print '\nCosponsorship().cosponsorship_by_join_date((2016,03,14)): '
pprint.pprint(Cosponsorship().cosponsorship_by_join_date((2016,03,14)))
print '\nCosponsorship().cosponsorship_by_person("Shelley Capito"): '
pprint.pprint(Cosponsorship().cosponsorship_by_person("Shelley Capito"))
print '\nCosponsorship().cosponsorship_by_role(596): '
pprint.pprint(Cosponsorship().cosponsorship_by_role(596))
print '\nCosponsorship().cosponsorship_by_cosponsorshipID(734897): '
pprint.pprint(Cosponsorship().cosponsorship_by_cosponsorshipID(734897))