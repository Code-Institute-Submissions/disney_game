import unittest

from run import app

class test(unittest.TestCase):

   
        
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
    
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
    
        
    def test_user_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/user') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_game_code(self):
        # sends HTTP GET request to the application
        # should fail without defined user name
      
        result = self.app.get('/user/simon') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 404)
     
    
  
  

 

  
         
    