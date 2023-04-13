import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL= ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("******* SearchCustomerByEmail_004 *********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info(" Login successful")
        time.sleep(5)
        self.logger.info("******** starting search customer by email ********")

        self.addcust= AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("********* searching customer by emailID ********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("priya@gmail.com")
        searchcust.clickSearch()
        time.sleep(10)
        status=searchcust.searchCustomerByEmail("priya@gmail.com")
        assert True==status
        print("Search customer by email status:", status)
        self.logger.info("******* TC_SearchCustomerByEmail_004 Finished *******")
        self.driver.close()