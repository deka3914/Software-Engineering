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

# Testing Modularity
Application
  author.py
  author_test.py
  article.py
  article_test.py
  comments.py
  comments_test.py
  
# Testing Template
  test_one_thing
    t = test_object
    x = process(t)
    answer = correct_answer
    assert( x == answer)
    
 # Testing Exceptions
test_for_exception
  try
    t = test_object
    x = process(t)
    answer = correct_answer
    assert(False)
  catch
    pass
