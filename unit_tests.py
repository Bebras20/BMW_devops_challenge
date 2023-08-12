import unittest
from parser import validate_mail


class Testing_functions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def testing_validate_mail(self):
        """ make sure the shuffled sequence does not lose any elements """
        mail1="ksldkqsd@bwm.de"
        mail2="ksldkqsd@bwmds.de"
        
        self.assertTrue(validate_mail(mail1))

    


if __name__=="__main__":
    unittest.main()
        