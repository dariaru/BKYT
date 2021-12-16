from behave import *
from tdd_test.TDD_test import *

@given("Service_Builder")
def first_step(context):
    context.a = Service_Builder_Test()

@when("test_AnnaLafargue_builder return OK")
def test_AnnaLafargue_builder(context):
    context.a.test_AnnaLafargue_builder()

@when("test_Luminarc_builder return OK")
def test_Luminarc_builder(context):
    context.a.test_Luminarc_builder()

@then("Good job")
def last_step(context):
    pass

