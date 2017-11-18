from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from .models import KeyTypes, Keys, Affiliations, Departments, Customers, LoanExceptions, LoanTerms, Records

class KeyTypesTests(TestCase):
    def setUp(self):
        KeyTypes.objects.create(
            key_type="Test Type 1",
            description="Description for Test Type 1"
        )
        KeyTypes.objects.create(
            key_type="Test Type 2",
            description="Description for Test Type 2"
        )

    def test_key_added_unique(self):
        """KeyTypes added are creating separate items, and autoincrementing PK"""
        type1id = KeyTypes.objects.filter(key_type__iexact="Test Type 1").get().id
        type2id = KeyTypes.objects.filter(key_type__iexact="Test Type 2").get().id
        self.assertNotEqual(type1id, type2id)

    def test_str(self):
        # KeyTypes.objects.create(
        #     key_type="Test Type 1",
        #     description="Description for Test Type 1"
        # )
        keytype = KeyTypes.objects.filter(key_type__iexact="Test type 1").get()
        self.assertEqual(keytype.__str__(), "Test Type 1")

class KeysTests(TestCase):
    def setUp(self):
        type1 = KeyTypes.objects.create(
            key_type="Test Type 1",
            description="Description for Test Type 1"
        )
        Keys.objects.create(
            key_type=type1,
            number=1,
        )

    def test_new_key_states_and_properties(self):
        """Check to make sure that all the states for a new key are working properly"""
        key = Keys.objects.filter(number__exact=1).get()
        self.assertEqual(key.is_retired, False)
        self.assertIsNone(key.retirement_type)
        self.assertEqual(key.is_returned, True)
        self.assertEqual(key.__str__(), "Test Type 1 1")

class ModelInteractionTests(TestCase):
    @classmethod
    def setUpClass(cls):
        key_type = KeyTypes.objects.create(key_type="Type", description="Key Type Test Description")
        key1 = Keys.objects.create(key_type=key_type, number=1234)
        key2 = Keys.objects.create(key_type=key_type, number=5678)
        affiliation = Affiliations.objects.create(affiliation="Test Affiliation 1")
        affiliation2 = Affiliations.objects.create(affiliation="Test Affiliation 2", customer_user_id_reqd=False)
        department = Departments.objects.create(dept_name="Test Department", box_number=123456)
        customer1 = Customers.objects.create(
            user_id="testid",
            last_name="Lastname",
            first_name="Firstname",
            phone_number="206-123-4567",
            email_address="test@test.net",
            department=department,
            affiliation=affiliation
        )
        customer2 = Customers.objects.create(
            user_id="testid2",
            last_name="Lastname2",
            first_name="Firstname2",
            phone_number="206-123-4567",
            email_address="test2@test.net",
            department=department,
            affiliation=affiliation2
        )
        loan_exception = LoanExceptions.objects.create(
            customer=customer1,
            key_type=key_type,
            date_expires=timezone.now() + timedelta(days=2),
            limit=2,
            granted_by="Exception Grantor",
            admin_comment="No commentary here."
        )
        loan_term = LoanTerms.objects.create(term_desc="test term desc.", term_length=2)
        record = Records.objects.create(
            customer=customer1,
            key=key1,
            date_out=timezone.now(),
            date_due=timezone.now() + timedelta(days=2),
            loan_term=loan_term
        )
        # Validate test model before proceeding with tests
        key_type.full_clean()
        key1.full_clean()
        key2.full_clean()
        affiliation.full_clean()
        affiliation2.full_clean()
        department.full_clean()
        customer1.full_clean()
        customer2.full_clean()
        loan_exception.full_clean()
        loan_term.full_clean()
        record.full_clean()

    def test_cannot_check_out_checked_out_key(self):
        """If this works correctly, a ValidationError should be raised, indicating that the key in question 
        is already checked out to someone else, and cannot be checked out by this other person."""
        with self.assertRaisesRegex(ValidationError, r"(.)*(Key %\(key\)s is already checked out to someone else){1}(.)*"):
            duplicate_checkout = Records.objects.create(
                customer=Customers.objects.create(
                    user_id="testid3",
                    last_name="Lastname3",
                    first_name="Firstname3",
                    phone_number="206-234-5678",
                    email_address="test3@test.net",
                    department=Departments.objects.filter(dept_name__iexact="Test Department").get(),
                    affiliation=Affiliations.objects.filter(affiliation__iexact="Test Affiliation 1").get()
                ),
                key=Keys.objects.filter(number__exact=1234).get(),
                date_out=timezone.now(),
                date_due=timezone.now() + timedelta(days=1),
                loan_term=LoanTerms.objects.filter(term_desc__iexact="test term desc.").get()
            )
            duplicate_checkout.full_clean()

    def test_key_retirement_rules_no_type_and_no_comment(self):
        """Ensure that retirement rules are being enforced: if both type and comment are left out"""
        with self.assertRaisesRegex(ValidationError, r"test"):
            key = Keys.objects.filter(number__exact=5678).get()
            key.is_retired = True
            key.full_clean()

    def test_key_retirement_rules_no_type_only(self):
        """Ensure that retirement rules are being enforced: if type is left out"""
        with self.assertRaisesRegex(ValidationError, r"test"):
            key = Keys.objects.filter(number__exact=5678).get()
            key.is_retired = True
            key.retirement_comment = "retirement comment"
            key.full_clean()
    
    def test_key_retirement_rules_no_comment_only(self):
        """Ensure that retirement rules are being enforced: if comment is left out"""
        with self.assertRaisesRegex(ValidationError, r"test"):
            key = Keys.objects.filter(number__exact=5678).get()
            key.is_retired = True
            key.retirement_type = 2
            key.full_clean()

    def test_cannot_check_out_retired_key(self):
        """Checks to ensure that validation disallows retired keys to be checked out."""
        key3 = Keys.objects.create(
            key_type=KeyTypes.objects.filter(key_type__iexact="Type").get(),
            number=1111,
            is_retired=True,
            retirement_type=2,
            retirement_comment="lock type retired"
        )
        with self.assertRaisesRegex(ValidationError, r"test"):
            retired_key_checkout = Records.objects.create(
                customer=Customers.objects.filter(email_address__contains="test2").get(),
                key=key3,
                date_out=timezone.now(),
                date_due=timezone.now() + timedelta(days=1),
                loan_term=LoanTerms.objects.filter(term_desc__iexact="test term desc.").get()
            )
            retired_key_checkout.full_clean()

    @classmethod
    def tearDownClass(cls):
        pass
