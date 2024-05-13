import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.edge.service import Service

from Login import login

# from Pages.AddNewCoach import AddnewCoach
# from Pages.AddNewPrgmList import AddNewPrgrmlist
# from Pages.AddNewSchedulingList import AddNewSchedulingList
# from Pages.AddNewServiceProvider import AddNewServiceProvider
# from Pages.CoachList import coachList
# from Pages.CounsellingRequest import Counsellingrequest
# from Pages.CreateBatch import CreateBatch
# from Pages.LearnersPage import learnerPage
# from Pages.Login import login
# from Pages.PrgmBatchList import ProgramBatchList
# from Pages.PrmList import Programlist
# from Pages.SchedulingList import SchedulingList
# from Pages.ServiceProvider import SearchServiceProvider
# from Pages.UserCompletedTask import UserCompletedTask

driver = webdriver.Chrome(service=Service(chromedriver_autoinstaller.install()))


class Test_ibridge360:
    # Create a WebDriver instance using the Edge service
    #     driver = webdriver.Edge(service=edge_service)
    driver.get("http://dev.ibridge360.com")
    driver.maximize_window()
    time.sleep(2)


def test_login(self):
    ls = login(self.driver)
    ls.signin_btn()
    username_field = 'ibridge@gmail.com'
    ls.login_ibridge(username_field)
    password_field = 'Ibridge@2021'
    ls.pwd_ele(password_field)
    ls.click_loginBtn()


# def testLearnerPage(self):
#         #click on Learners tab
#         lp = learnerPage(self.driver)
#         lp.clickOnLearners()
#
#         # Search in Learners tab
#         lname='joel test'
#         lp.searchLname(lname)

# def testCoachList(self):
#          # Coach list tab
#         cl=coachList(self.driver)
#         cl.clickOnCoachList()

# def testAddNewCoach(self):
#         # Click on Add New coach Btn
#         Anc = AddnewCoach(self.driver)
#         Anc.clickOnAddNewCoach()

# upload file
# Anc.clickChooseFile()
# fname = 'James'
# Anc.fn(fname)
# lname = 'peterson'
# Anc.ln(lname)
# mail = 'james@gmail.com'
# Anc.email(mail)
# pwd = 'Password#12'
# Anc.password(pwd)
# ex='Python'
# Anc.expert(ex)
# ind = 'IT'
# Anc.industry(ind)
# sk = 'CSS'
# Anc.skills(sk)
# exp = '5'
# Anc.experience(exp)
# loc = 'Bangalore'
# Anc.location(loc)
# hr = '6'
# Anc.weekely_hr(hr)
# Anc.Preferred_days()
# Anc.p_d()
# time.sleep(2)
# Anc.preferred_time()
# Anc.p_t()
# tm='Asia/Kolkata'
# Anc.zone(tm)
# desc = "Python is a high-level, general-purpose programming language"
# Anc.desc(desc)
# Anc.submitNewCoach()

# def testEditCoachList(self):
# cl = coachList(self.driver)
# # Search coach list
# sname='suraj'
# cl.SearchCoachList(sname)
# cl.clicktable()
# cl.EditCoachList()
#
# # upload files
# cl.uploadCL()
# cl.SubmitEditedCoachList()

# def testPrgmList(self):
#        Pl = Programlist(self.driver)
#        Pl.clickProgramlist()

# Search
# Plname = 'React Basics'
# Pl.searchPrgmList(Plname)

# click on prgm info
# Pl.clickPrgmInfo()
# Pl.clickPIEdit()
# Pl.clickChooseFile()
# Pl.uploadProgramContentImag()
# Pl.AddProgramProfileImageself='C:/Users/91733/Desktop/py1.jpeg'
# Pl.AddProgramContentImage='C:/Users/91733/Desktop/py1.jpeg'
# self.driver.execute_script("window.scrollBy(0,1000)", "")
# Pl.submit()

# def testaddLearners(self):
# Add Learners
# Al = Programlist(self.driver)
# lname='React Basics'
# Al.SearchLname(lname)

# click on add learners
# Al.ClickAddLearner()
# user=' '
# Al.addUser(user)
# bat = ' '
# Al.Select_batch(bat)
# Al.lsubmit()

# def testAddNewPrgmList(self):
# Add New Program
# APl=AddNewPrgrmlist(self.driver)
# APl.clickAddNewProgram()
# APl.PP_img()
# APl.PC_img()
# Program_name='Cyber Security'
# APl.AddNewProgram(Program_name)

# # add program path
# APl.PrgmPath()
# APl.PPadd()
# valuePP='linux'
# APl.PP(valuePP)
# APl.PPdone()
# Total_hours = '6'
# APl.Totalhr(Total_hours)
# Courses='Power BI'
# APl.Slcourses(Courses)
# APl.LPath()
# APl.Ladd()
# Lval='React JS'
# APl.Lvalue(Lval)
# APl.Ldone()
# SCT_value=' '
# APl.cap(SCT_value)
# Prov = ' '
# APl.Service(Prov)
# p_duration='12 months'
# APl.Pdur(p_duration)
# start_date='10-September-2023'
# APl.click_sdIcon(start_date)
# APl.start_date.split("-")
# APl.date_ele()
# APl.ok()
# Program_start_date='23-04-2023'
# APl.Prgrmdate(Program_start_date)
# APl.Pdate_picker()
# APl.sok()
# Program_end_date = '30-05-2023'
# APl.prgm_end_date(Program_end_date)
# APl.pnxt_btn()
# APl.year_month()
# APl.Edate_picker()
# APl.Eok()
# ment=' '
# APl.mentor(ment)
# Price = '30000'
# APl.PricePrgm(Price)
# desc = 'JHF'
# APl.prgm_desc(desc)
# APl.submit()

# def testServiceProvider(self):
#        #Service Provider
#        SSP=SearchServiceProvider(self.driver)
#        SSP.clickServiceProvider()

# SPV = 'Aroha Technologies'
# SSP.SearchSP(SPV)
# SSP.tbody()

# Edit SP
# SSP.clickEdit()
# SSP.clicksave()

# def AddNewSP(self):
#        #Add New Service provider
#        ANSP = AddNewServiceProvider(self.driver)
#        ANSP.clickAddNewServiceProvider()
#        ANSP.Img_ele()
#        P_name='Wipro'
#        ANSP.providerName(P_name)
#        mail='wip@gmail.co.in'
#        ANSP.email(mail)
#        contact_name='Kumar'
#        ANSP.PCN(contact_name)
#        number='0123456789'
#        ANSP.ph_no(number)
#        add='RV road'
#        ANSP.address_ele(add)
#        city_name='Bangalore'
#        ANSP.city(city_name)
#        st_name='Karnataka'
#        ANSP.state_ele(st_name)
#        zc='560027'
#        ANSP.zipcode_ele(zc)
#        PGST='123-456-789'
#        ANSP.Provider_GST(PGST)
#        Pncrd='ABC-456-789'
#        ANSP.Pancard_ele(Pncrd)
#        S_desc='JHFJH'
#        ANSP.Service_desc(S_desc)
#        ANSP.submit()

# def testCR(self):
#        # Counselling Request
#        CR=Counsellingrequest(self.driver)
#        CR.clickonConsellingrequest()
#        CRV='veeranna bhrungi'
#        CR.SearchCounsellingreq(CRV)

# def testPrgmBatchList(self):
# Program batch list
# PBL=ProgramBatchList(self.driver)
# PBL.clickonPBL()
# PBl_value=' '
# PBL.SearchPB(PBl_value)
# PBL.clicktablerow()
# BUV=' '
# PBL.serchBU(BUV)
# PBL.clickRemove()

# def testAddUser(self):
# Add user
# PBL.clickABlist()
# users=' '
# PBL.Adduser(users)
# PBL.AUsubmit()
#
# def testCreateBatch(self):
#        # Create Batch
#        CB=CreateBatch(self.driver)
#        CB.clickCreateBatch()
#        B_title='testing batch'
#        CB.inputBatch(B_title)
#        program=' '
#        CB.SDD(program)
#        Batch_start_date='07-09-2023'
#        CB.batch_date(Batch_start_date)
#        CB.B_date_picker()
#        CB.bok()
#
#        Batch_end_date = '30-06-2023'
#        CB.batch_end_date(Batch_end_date)
#        CB.nxt_btn()
#        CB.year_month()
#        CB.E_date_picker()
#        CB.EOK_ele()
#        CB.submit()

# def testSchedulingList(self):
# Scheduling list
# SL=SchedulingList(self.driver)
# SL.clickSchedulinglist()
# SSL='New introduction'
# SL.searchSL(SSL)
# SL.calendaricon()
# SL.cross()
# SL.clickeditSL()
# SL.submit()

# def testCreateSchedule(self):
# Create schedule
# CSL=AddNewSchedulingList(self.driver)
# CSL.clickCreateSchedule()
# title='Angular basics'
# CSL.inputSL(title)
#
# bvalue=' '
# CSL.Sbtch(bvalue)
# Schedule_start_date='02/04/203'
# Schedule_end_date='26/05/2023'
# CSL.Schedule_date(Schedule_start_date, Schedule_end_date)
# t_value='iLearn'
# CSL.task_type(t_value)
# s_d = 'JHF'
# CSL.s_desc(s_d)
# CSL.submit()

# def testUserCompletedtask(self):
#        # User completed Task
#        UCT=UserCompletedTask(self.driver)
#        UCT.clickUCT()
#        UCTval='test123'
#        UCT.searchUCT(UCTval)


iobj = Test_ibridge360()
Test_ibridge360()
iobj.test_login()
# iobj.testLearnerPage()
# iobj.testCoachList()
# iobj.testEditCoachList()
# iobj.testAddNewCoach()
# iobj.testPrgmList()
# # iobj.testaddLearners()
# iobj.testAddNewPrgmList()
# iobj.testServiceProvider()
# iobj.AddNewSP()
# iobj.testCR()
# iobj.testPrgmBatchList()
# iobj.testAddUser()
# iobj.testCreateBatch()
# iobj.testSchedulingList()
# iobj.testCreateSchedule()
# iobj.testUserCompletedtask()
