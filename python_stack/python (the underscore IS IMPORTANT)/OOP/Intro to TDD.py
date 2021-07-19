
import unittest


# def reverseList (list1):
#     for i in range(int( len(list1)/2)):
#         list1[i],list1[len(list1)-i-1]=list1[len(list1)-i-1],list1[i]
#     return list1
# class IsREVERSETests(unittest.TestCase):
  
#     def testTwo(self):
#         self.assertEqual(reverseList ([1,3,5]), [5,3,1])
        
       
#     def testThree(self):
#         self.assertNotEqual(reverseList ([1,3,5]), [5,3,1])

#     def testFour(self):
#         self.assertTrue(reverseList ([1,3,5]), [5,3,1])
     
 
#     def setUp(self):
#         # add the setUp tasks
#         print("running setUp")
#     # any task you want run after the tests are executed, put them in the tearDown method
#     def tearDown(self):
#         # add the tearDown tasks
#         print("running tearDown tasks")
# if __name__ == '__main__':
#     unittest.main() # this runs our 
    
def isPalindrome (list1):
    if(list1==list1[::-1]):
        return True
    else:
        return False



class Ispalindrome (unittest.TestCase):

    def testTwo(self):
        self.assertTrue(isPalindrome("racecar"))
        
       
    def testThree(self):
        self.assertTrue(isPalindrome("ABA"))

    def testFour(self):
        self.assertFalse(isPalindrome("ABABArabcrBABABAB"))

    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our 
     
