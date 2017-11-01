# Make sure that tests runs
test_runs
  assert(False)
  
# Make sure libraries load
test_load_csv_lib
  import csv
  
# Unit testing run function
test_all
  test_thing_1()
  test_thing_2()
  test_thing_3()
  
test_thing_1
  assert(thing(object),answer)
test_thing_2
  assert(thing(object),answer)
test_thing_3
  assert(thing(object),answer)
  
test_all()

