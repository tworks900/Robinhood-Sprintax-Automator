from selenium import webdriver
import pandas as pd
import time
sec_trades = pd.read_csv('trades_robinhood.csv')

#cryp_trades = pd.read_csv('trades_cryp.csv')
#cryp_trades['sell_date'] = cryp_trades['sell_date'].astype(str) + '20'
#cryp_trades['buy_date'] = cryp_trades['buy_date'].astype(str) + '20'

payers_name = 'Robinhood Securities LLC'
payers_name_cryp = 'Robinhood Crypto LLC'
address = '85 Willow Road'
address_cryp = '85 Willow Road'
city = 'Menlo Park'
city_cryp = 'Menlo Park'
state = 'CA'
state_cryp = 'CA'
zip = '94025'
zip_cryp = '94025'
payers_tin = '46-4364776'
payers_tin_cryp = '46-4364776'
state_tax_widthheld = '0'
fed_tax_widthheld = '0'


def openChrome():
    global driver
    driver = webdriver.Chrome()
    website="https://www1.columbia.edu/pamacea/login.shtml?target=https://www.sprintax.com/uni-lp.html?utm_ref=columbialp&pamservice=krb&userfile=" # Change this you school's portal to sprintax or just google.com
    driver.get(website)
    time.sleep(10)

def trades():
    number_of_trades=sec_trades.shape[0]
    print(f"Number of Robinhood Trades on-record = {number_of_trades}")
    return number_of_trades
def date_format(date):
    # YYYYMMDD -> MMDDYYYY
    updated_date=date[4:6]+'/'+date[6:]+'/'+date[:4]
    return updated_date

def setupInfo():
    global payers_name_el
    payers_name_el = driver.find_element("xpath",'//*[@id="__employer_details_employer_name"]')
    global address_el
    address_el = driver.find_element("xpath",'//*[@id="__employer_details_employer_address"]')
    global city_el
    city_el = driver.find_element("xpath",'//*[@id="__employer_details_employer_city"]')
    global state_el
    state_el = driver.find_element("xpath",'//*[@id="__employer_details_employer_state"]')
    global zip_el
    zip_el = driver.find_element("xpath",'//*[@id="__employer_details_employer_zip_code"]')
    global payers_tin_el
    payers_tin_el = driver.find_element("xpath",'//*[@id="payers_federal_id"]')
    global state_select_el
    state_select_el = driver.find_element("xpath",'//*[@id="statecode"]/option[22]') #hardwired to MA, use element inspect to find your state's exact xpath and copy and paste here
    global state_tax_widthheld_el
    state_tax_widthheld_el = driver.find_element("xpath",'//*[@id="state_income_tax"]')
    global next_btn 
    next_btn = driver.find_element("xpath",'//*[@id="footer"]/div[1]/div[3]/a')

def runInfo(crypto=False):
    state_tax_widthheld_el.send_keys(state_tax_widthheld)
    state_select_el.click()
    if crypto:
        raise Exception(
            "Crypto Module is currently un-verified/non-functional on this script.Please add crypto== False ")
        payers_name_el.send_keys(payers_name_cryp)
        address_el.send_keys(address_cryp)
        city_el.send_keys(city_cryp)
        state_el.send_keys(state_cryp)
        zip_el.send_keys(zip_cryp)
        payers_tin_el.send_keys(payers_tin_cryp)
    else:
        payers_name_el.clear()
        address_el.clear()
        city_el.clear()
        state_el.clear()
        zip_el.clear()
        payers_tin_el.clear()

        payers_name_el.send_keys(payers_name)
        address_el.send_keys(address)
        city_el.send_keys(city)
        state_el.send_keys(state)
        zip_el.send_keys(zip)
        payers_tin_el.send_keys(payers_tin)

def setupTrade():
    global descp_el
    descp_el = driver.find_element("xpath",'//*[@id="description"]')
    global buy_date_el
    buy_date_el = driver.find_element("xpath",'//*[@id="date_of_acquistion"]')
    global sell_date_el
    sell_date_el =  driver.find_element("xpath",'//*[@id="date_of_sale"]')
    global proceeds_el
    proceeds_el = driver.find_element("xpath",'//*[@id="stocks_bonds"]')
    global cost_el
    cost_el = driver.find_element("xpath",'//*[@id="costs_other_basic"]')
    global fed_tax_widthheld_el
    fed_tax_widthheld_el = driver.find_element("xpath",'//*[@id="federal_income_tax"]')
    global gross_rep_el
    gross_rep_el = driver.find_element("xpath",'//*[@id="sim_reported_irs1"]/a')
    global short_trm_el
    short_trm_el = driver.find_element("xpath",'//*[@id="sim_gain_or_lost1"]/a')
    global long_trm_el
    long_trm_el = driver.find_element("xpath", '//*[@id="sim_gain_or_lost2"]/a')
    global wash_sale_el
    wash_sale_el = driver.find_element("xpath",'//*[@id="wash_sale_loss"]')
    global trade_property_sale_el
    trade_property_sale_el = driver.find_element("xpath", '// *[ @ id = "reported_gain_or_loss2"]')

def runTrade(index, crypto = False):
    gross_rep_el.click()
    trade_property_sale_el.click()
    fed_tax_widthheld_el.clear()
    fed_tax_widthheld_el.send_keys(fed_tax_widthheld)

    if "SHORT" == str(sec_trades.iloc[index]['TERM']):
        short_trm_el.click()
    else:
        long_trm_el.click()
    if crypto:
        raise Exception("Crypto Module is currently un-verified/non-functional on this script.Please add crypto== False ")
        #descp_el.send_keys(str(cryp_trades.iloc[index]['descp']))
        #buy_date_el.send_keys(str(cryp_trades.iloc[index]['buy_date']))
        #sell_date_el.send_keys(str(cryp_trades.iloc[index]['sell_date']))
        #proceeds_el.send_keys(str(cryp_trades.iloc[index]['proceeds']))
        #cost_el.send_keys(str(cryp_trades.iloc[index]['cost']))
    else:
        descp_el.clear()
        buy_date_el.clear()
        sell_date_el.clear()
        proceeds_el.clear()
        cost_el.clear()
        wash_sale_el.clear()
        descp_el.send_keys(str(sec_trades.iloc[index]['DESCRIPTION']))
        buy_date_el.send_keys(date_format(str(sec_trades.iloc[index]['DATE ACQUIRED'])))
        sell_date_el.send_keys(date_format(str(sec_trades.iloc[index]['SALE DATE'])))
        wash_sale_el.send_keys(str(sec_trades.iloc[index]['WASH AMT DISALLOWED']))
        if (int(sec_trades.iloc[index]['SALES PRICE']) < 0):
            cost_el.send_keys(str(abs(sec_trades.iloc[index]['SALES PRICE'])))
            proceeds_el.send_keys(str(0))
        else:
            proceeds_el.send_keys(str(sec_trades.iloc[index]['SALES PRICE']))
            cost_el.send_keys(str(sec_trades.iloc[index]['COST BASIS']))


def execute(index,cryp=False):
    setupInfo()                                          
    runInfo(cryp)
    setupTrade()                                         
    runTrade(index,cryp)

def loop(start, end, cryp=False):
    while start <= end:
        execute(start-1,cryp)
        start+=1
        next_btn.click()
        time.sleep(5)