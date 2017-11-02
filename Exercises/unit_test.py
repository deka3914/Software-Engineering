Create a code file called unit_test.py (or unit_test.cs, unit_test.java, etc.)

Create a function to test all the features and invoke it automatically. Name it test_user().

Create a test to verify creation of a User class object. Name it test_create(). This should fail.

Make test_create() pass by creating an object class called User.

Test for properties to be set for first name and last name. This should fail. Now add code to create and set those properties.

Test for email property. Then add it to the User class.

Create four test cases for creating user objects with different names.

Extract the duplication by creating test_a_name(first,last,name) function. Make sure that all tests still pass.

Create a function that adds a number of users from a list, verifying each one.

Test that the User creation will throw an exception when any property is missing.

Publish your results in your student directory in the Github UNC-CS350 repo.

User class
    first
    last
    email
    name()

test_one_thing
    t = test_object
    x = process(t)
    answer = correct_answer
    assert (x == answer)

test_for_exception
    try
        t = test_object
        x = process(t)
        answer = correct_answer
        assert (False)
    catch
        pass
