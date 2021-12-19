from behave import *
from tdd_test.TDD_test import *

@given("EnteredData")
def Function(context):
    context.a = TestBot()


@when("test_Remember_Name")
def Function_1(context):
    context.a.test_1()

@when("test_Remember_Age")
def Function_2(context):
    context.a.test_2()

@then("Good job!")
def check_result(context):
    pass