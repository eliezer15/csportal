from django.test import TestCase
from models import Offer, Interview, Location, Company
from django.contrib.auth.models import User
import populate


class GetHiredModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
                username='root')
##uncomment this if you want to populate the database with tons of stuff
        #populate.populate()

    def test_company_model(self):
#sanity check just to see that the Company table is empty
        self.assertFalse(Company.objects.all())

        Company.objects.create(name="Google")
        Company.objects.create(name="Microsoft")
        Company.objects.create(name="SAS")
        Company.objects.create(name="Citrix")

        self.assertTrue(len(Company.objects.all()) == 4)
        self.assertTrue(Company.objects.get(name="Google"))
        self.assertTrue(Company.objects.get(name="Microsoft"))
        self.assertTrue(Company.objects.get(name="SAS"))
        self.assertTrue(Company.objects.get(name="Citrix"))

    def test_location_model(self):
#sanity check
        self.assertFalse(Location.objects.all())

        Location.objects.create(city="Raleigh", state="NC")
        Location.objects.create(city="Mountain View", state="CA")
        Location.objects.create(city="Redmond", state="WA")
        Location.objects.create(city="Cary", state="NC")

        self.assertTrue(len(Location.objects.all()) == 4)
        self.assertTrue(len(Location.objects.filter(state="NC")) == 2)
        self.assertTrue(Location.objects.get(city="Redmond"))
        self.assertTrue(Location.objects.get(city="Mountain View"))

    def test_interview_model(self):
        self.assertFalse(Interview.objects.all())
        interview_1 = Interview.objects.create(author=self.user,
        company = Company.objects.create(name="Google"),
        location = Location.objects.create(city='Mountain View', state='CA'),
        job_title = "SE",
        job_type = "FT",
        interview_process = "Hard interviews.",
        questions_asked = "Why Google?",
        interview_source = 'CF',
        offer_status = 'RC',
        offer_details = None,
        interview_rating = 1
        )
        self.assertTrue(Interview.objects.all())
        self.assertTrue(Interview.objects.get(company__name="Google"))
        self.assertTrue(Interview.objects.get(location__city="Mountain View"))
        self.assertTrue(Interview.objects.get(job_title="SE"))
        self.assertTrue(Interview.objects.get(job_type="FT"))
        self.assertTrue(Interview.objects.get(interview_process="Hard interviews."))
        self.assertTrue(Interview.objects.get(questions_asked="Why Google?"))
        self.assertTrue(Interview.objects.get(offer_status="RC"))
        self.assertTrue(Interview.objects.get(interview_rating=1))

#Assert that Interview table now has an entry
        self.assertTrue(Interview.objects.all())

    def test_offer_model(self):
        self.assertFalse(Offer.objects.all())
        offer_1 = Offer.objects.create(
        author=self.user,
        applicant_degree = 'BS',
        company = Company.objects.create(name="Google"),
        location = Location.objects.create(city='Mountain View', state='CA'),
        job_title = "SE",
        job_type = "FT",
        salary = 80000,
        signing_bonus = 10000,
        relocation_bonus = 10000,
        offer_status = 'RC',
        other_details = "Liked the offer, good benefits",
        )
        self.assertTrue(Offer.objects.all())
        self.assertTrue(Offer.objects.get(company__name="Google"))
        self.assertTrue(Offer.objects.get(location__city="Mountain View"))
        self.assertTrue(Offer.objects.get(applicant_degree='BS'))
        self.assertTrue(Offer.objects.get(job_title="SE"))
        self.assertTrue(Offer.objects.get(job_type="FT"))
        self.assertTrue(Offer.objects.get(salary=80000))
        self.assertTrue(Offer.objects.get(signing_bonus=10000))
        self.assertTrue(Offer.objects.get(relocation_bonus=10000))
        self.assertTrue(Offer.objects.get(offer_status='RC'))
        self.assertTrue(Offer.objects.get(other_details='Liked the offer, good benefits'))
