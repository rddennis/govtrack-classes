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

	def __init__(self, bill_id):
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
		apiCall = urllib2.urlopen("https://www.govtrack.us/api/v2/bill?committees=" + committee_name)
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




pprint.pprint(Cosponsorship().cosponsorship_by_person("Barack Obama"))
		
